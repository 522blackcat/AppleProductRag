from pathlib import Path
import re
from urllib.parse import urlparse
import requests

DOCS_DIR = Path('../docs')
IMAGES_DIR = DOCS_DIR / 'images'
IMAGES_DIR.mkdir(exist_ok=True)

pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^)]+)\)')
updated = 0
failed = []

for md_path in sorted(DOCS_DIR.glob('*.md')):
    text = md_path.read_text(encoding='utf-8')
    matches = list(pattern.finditer(text))
    for match in matches:
        alt, url = match.group(1), match.group(2)
        suffix = Path(urlparse(url).path).suffix
        if not suffix or len(suffix) > 8:
            suffix = '.jpg'
        image_name = f'{md_path.stem}{suffix}'
        image_path = IMAGES_DIR / image_name
        try:
            if not image_path.exists() or image_path.stat().st_size == 0:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
                image_path.write_bytes(resp.content)
            local_ref = f'images/{image_name}'
            text = text.replace(match.group(0), f'![{alt}]({local_ref})')
            updated += 1
        except Exception as exc:
            failed.append((md_path.name, url, str(exc)))
    md_path.write_text(text, encoding='utf-8')

print(f'updated_images={updated}')
print(f'failed={len(failed)}')
for item in failed:
    print(item)
