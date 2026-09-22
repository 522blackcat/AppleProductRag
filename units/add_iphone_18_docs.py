from pathlib import Path
from urllib.parse import urljoin
import html
import re
import requests

DOCS = Path('../docs')
IMAGES = DOCS / 'images'
DOCS.mkdir(exist_ok=True)
IMAGES.mkdir(exist_ok=True)

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

def get_og_image(page_url, name):
    page = session.get(page_url, timeout=30)
    page.raise_for_status()
    m = re.search(r'<meta property="og:image" content="([^"]+)"', page.text)
    if not m:
        raise RuntimeError(f'no og:image: {page_url}')
    url = urljoin(page_url, html.unescape(m.group(1)))
    r = session.get(url, timeout=30)
    r.raise_for_status()
    suffix = '.png' if '.png' in url.lower() else '.jpg'
    path = IMAGES / f'{name}{suffix}'
    path.write_bytes(r.content)
    return f'images/{path.name}'

images = {}
for key, url in {
    'iphone-18-pro': 'https://www.apple.com.cn/shop/buy-iphone/iphone-18-pro',
    'iphone-duo': 'https://www.apple.com.cn/shop/buy-iphone/iphone-duo',
}.items():
    try:
        images[key] = get_og_image(url, key)
    except Exception as exc:
        print(key, exc)
        images[key] = 'images/iphone-17-pro.png'

products = [
    {
        'file': 'iphone-18-pro.md',
        'name': 'iPhone 18 Pro',
        'image': images['iphone-18-pro'],
        'category': '手机',
        'series': 'iPhone Pro',
        'release': '2026 年 9 月 9 日发布，9 月 12 日预购，9 月 18 日发售',
        'colors': ['黑色', '银色', '冰川蓝色', '勃艮第酒红色'],
        'intro': 'iPhone 18 Pro 是 Apple 2026 年 Pro 旗舰手机，主打 A20 Pro 芯片、专业影像、可变光圈主摄、增强散热和 Apple Intelligence。',
        'specs': [('芯片','A20 Pro'),('屏幕','6.3 英寸 Super Retina XDR 显示屏'),('刷新率','ProMotion 自适应刷新率，最高 120Hz'),('摄像头','Pro 级融合式摄像头系统，可变光圈主摄'),('容量','256GB、512GB、1TB、2TB'),('接口','USB-C'),('系统','iOS 27')],
        'configs': [('256GB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 9,999'),('512GB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 11,999'),('1TB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 13,999'),('2TB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 15,999')],
        'buy': '多数 Pro 用户选 256GB 或 512GB。长期拍摄 ProRes、4K 视频或本地素材多，选 1TB/2TB。'
    },
    {
        'file': 'iphone-18-pro-max.md',
        'name': 'iPhone 18 Pro Max',
        'image': images['iphone-18-pro'],
        'category': '手机',
        'series': 'iPhone Pro',
        'release': '2026 年 9 月 9 日发布，9 月 12 日预购，9 月 18 日发售',
        'colors': ['黑色', '银色', '冰川蓝色', '勃艮第酒红色'],
        'intro': 'iPhone 18 Pro Max 是 Apple 2026 年大屏 Pro 旗舰，适合重度影音、游戏、创作和长续航需求。',
        'specs': [('芯片','A20 Pro'),('屏幕','6.9 英寸 Super Retina XDR 显示屏'),('刷新率','ProMotion 自适应刷新率，最高 120Hz'),('摄像头','Pro 级融合式摄像头系统，可变光圈主摄'),('容量','256GB、512GB、1TB、2TB'),('接口','USB-C'),('系统','iOS 27')],
        'configs': [('256GB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 10,999'),('512GB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 12,999'),('1TB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 14,999'),('2TB','黑色、银色、冰川蓝色、勃艮第酒红色','RMB 16,999')],
        'buy': '想要最大屏幕和最长续航选 Pro Max。512GB 是更稳妥容量，2TB 面向专业视频用户。'
    },
    {
        'file': 'iphone-duo.md',
        'name': 'iPhone Duo',
        'image': images['iphone-duo'],
        'category': '手机 / 折叠屏手机',
        'series': 'iPhone Duo',
        'release': '2026 年 9 月 9 日发布，10 月 16 日预购，10 月 23 日发售',
        'colors': ['星白色', '夜空色'],
        'intro': 'iPhone Duo 是 Apple 首款折叠屏 iPhone，适合想要手机和平板体验合一、重视大屏多任务和新形态体验的用户。',
        'specs': [('芯片','A20 Pro'),('内屏','7.6 英寸折叠式 Super Retina XDR 显示屏'),('外屏','5.4 英寸外屏'),('摄像头','双 48MP 后置摄像头'),('容量','256GB、512GB、1TB、2TB'),('连接','eSIM'),('系统','iOS 27')],
        'configs': [('256GB','星白色、夜空色','RMB 15,999'),('512GB','星白色、夜空色','RMB 17,999'),('1TB','星白色、夜空色','RMB 21,499'),('2TB','星白色、夜空色','RMB 26,499')],
        'buy': '尝鲜折叠屏和大屏多任务选 iPhone Duo。价格高，建议先线下体验铰链、重量和应用适配。'
    }
]

def table(rows, headers=('项目','内容')):
    a,b=headers
    return '\n'.join([f'| {a} | {b} |','|---|---|']+[f'| {x} | {y} |' for x,y in rows])

def config(rows):
    return '\n'.join(['| 配置 | 可选颜色 | 中国价格 |','|---|---|---:|']+[f'| {a} | {b} | {c} |' for a,b,c in rows])

for p in products:
    colors = '、'.join(p['colors'])
    content = f'''# {p['name']}

![{p['name']} 官方产品图]({p['image']})

## 基本信息

{table([('产品名',p['name']),('品牌','Apple'),('分类',p['category']),('系列',p['series']),('发布时间',p['release']),('同期发布颜色',colors)])}

## 产品介绍

{p['intro']}

## 同期发布颜色

| 颜色 | 说明 |
|---|---|
{chr(10).join(f'| {c} | 官方发布配色 |' for c in p['colors'])}

## 核心卖点

- 新一代 Apple 芯片，面向高性能、影像和 Apple Intelligence 场景。
- 中国大陆官方渠道支持分期、送货、到店取货和 Apple Trade In 换购。
- 适合看重长期系统更新、硬件做工和 Apple 生态协同的用户。

## 参数

{table(p['specs'])}

## 可选配置及中国价格

> 价格口径：中国大陆官方发售信息，单位为人民币。实际成交价可能因渠道、促销、以旧换新、分期和库存变化。

{config(p['configs'])}

## 电商式购买建议

{p['buy']}

## 适合人群

- 已在 Apple 生态内，想要最新 iPhone 体验的用户。
- 重视影像、性能、系统更新和售后服务的用户。
- 想按容量和预算清晰选购的用户。

## 数据来源

- Apple 中国大陆官网产品页、在线商店页面和新闻稿。
- Apple 官方技术规格页面。
- 中国大陆公开发售信息。
'''
    (DOCS / p['file']).write_text(content, encoding='utf-8')

print('added', len(products))
