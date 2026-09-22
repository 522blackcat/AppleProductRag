from pathlib import Path
from urllib.parse import urljoin
import html
import re

import requests

DOCS_DIR = Path("../docs")
IMAGES_DIR = DOCS_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

PAGE_BY_FILE = {
    "airpods-max.md": "https://www.apple.com.cn/shop/buy-airpods/airpods-max",
    "apple-vision-pro.md": "https://www.apple.com.cn/shop/buy-vision/apple-vision-pro",
    "apple-watch-se-3.md": "https://www.apple.com.cn/shop/buy-watch/apple-watch-se",
    "apple-watch-series-11.md": "https://www.apple.com.cn/shop/buy-watch/apple-watch",
    "apple-watch-ultra-3.md": "https://www.apple.com.cn/shop/buy-watch/apple-watch-ultra",
    "imac.md": "https://www.apple.com.cn/shop/buy-mac/imac",
    "ipad-air.md": "https://www.apple.com.cn/shop/buy-ipad/ipad-air",
    "ipad-mini.md": "https://www.apple.com.cn/shop/buy-ipad/ipad-mini",
    "ipad.md": "https://www.apple.com.cn/shop/buy-ipad/ipad",
    "iphone-16e.md": "https://www.apple.com.cn/shop/buy-iphone/iphone-16e",
    "iphone-17.md": "https://www.apple.com.cn/shop/buy-iphone/iphone-17",
    "iphone-air.md": "https://www.apple.com.cn/shop/buy-iphone/iphone-air",
}

IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\((https?://[^)]+)\)")
OG_IMAGE_PATTERN = re.compile(r'<meta property="og:image" content="([^"]+)"')

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})

done = []
failed = []

for file_name, page_url in PAGE_BY_FILE.items():
    md_path = DOCS_DIR / file_name
    text = md_path.read_text(encoding="utf-8")
    image_match = IMAGE_PATTERN.search(text)
    if not image_match:
        continue

    try:
        page = session.get(page_url, timeout=30)
        page.raise_for_status()
        og_match = OG_IMAGE_PATTERN.search(page.text)
        if not og_match:
            raise RuntimeError("未找到 og:image")

        image_url = urljoin(page_url, html.unescape(og_match.group(1)))
        image = session.get(image_url, timeout=30)
        image.raise_for_status()

        image_path = IMAGES_DIR / f"{md_path.stem}.jpg"
        image_path.write_bytes(image.content)

        local_markdown = f"![{image_match.group(1)}](images/{image_path.name})"
        text = text.replace(image_match.group(0), local_markdown)
        md_path.write_text(text, encoding="utf-8")
        done.append((file_name, image_url, len(image.content)))
    except Exception as exc:
        failed.append((file_name, str(exc)))

print(f"done={len(done)}")
for item in done:
    print(item)

print(f"failed={len(failed)}")
for item in failed:
    print(item)
