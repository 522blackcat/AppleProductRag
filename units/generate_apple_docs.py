from pathlib import Path

DOCS_DIR = Path("../docs")
DOCS_DIR.mkdir(exist_ok=True)

products = [
    {
        "file": "iphone-17.md",
        "name": "iPhone 17",
        "category": "手机",
        "series": "iPhone",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-17-finish-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["黑色", "薰衣草紫色", "鼠尾草绿色", "雾蓝色", "白色"],
        "intro": "iPhone 17 是 Apple 主流旗舰手机，适合多数用户。它主打更流畅的屏幕、更强影像、长续航和 Apple Intelligence 场景。",
        "specs": [
            ("芯片", "A19"),
            ("显示屏", "Super Retina XDR 显示屏"),
            ("屏幕尺寸", "6.3 英寸"),
            ("刷新率", "ProMotion 自适应刷新率，最高 120Hz"),
            ("容量", "256GB、512GB"),
            ("接口", "USB-C"),
            ("生物识别", "Face ID"),
        ],
        "configs": [
            ("256GB", "全部发布颜色", "RMB 5,999"),
            ("512GB", "全部发布颜色", "RMB 7,999"),
        ],
        "buy": "256GB 适合多数用户。512GB 适合大量拍摄照片、视频，或长期不清理微信数据的用户。",
    },
    {
        "file": "iphone-17-pro.md",
        "name": "iPhone 17 Pro",
        "category": "手机",
        "series": "iPhone Pro",
        "release": "2025 年 9 月",
        "image": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/iphone-17-pro-17-pro-max-hero.png",
        "colors": ["银色", "星宇橙色", "深蓝色"],
        "intro": "iPhone 17 Pro 是 Apple 高端 Pro 旗舰手机，适合影像创作、移动办公和高负载应用用户。",
        "specs": [
            ("芯片", "A19 Pro"),
            ("显示屏", "Super Retina XDR 显示屏"),
            ("屏幕尺寸", "6.3 英寸"),
            ("刷新率", "ProMotion 自适应刷新率，最高 120Hz"),
            ("容量", "256GB、512GB、1TB"),
            ("接口", "USB-C"),
            ("生物识别", "Face ID"),
        ],
        "configs": [
            ("256GB", "银色、星宇橙色、深蓝色", "RMB 8,999"),
            ("512GB", "银色、星宇橙色、深蓝色", "RMB 10,999"),
            ("1TB", "银色、星宇橙色、深蓝色", "RMB 12,999"),
        ],
        "buy": "256GB 是 Pro 入门选择。512GB 更适合经常拍视频。1TB 适合专业创作者。",
    },
    {
        "file": "iphone-17-pro-max.md",
        "name": "iPhone 17 Pro Max",
        "category": "手机",
        "series": "iPhone Pro",
        "release": "2025 年 9 月",
        "image": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/iphone-17-pro-17-pro-max-hero.png",
        "colors": ["银色", "星宇橙色", "深蓝色"],
        "intro": "iPhone 17 Pro Max 是大屏 Pro 旗舰，适合重度影音、游戏、影像创作和长续航需求。",
        "specs": [
            ("芯片", "A19 Pro"),
            ("显示屏", "Super Retina XDR 显示屏"),
            ("屏幕尺寸", "6.9 英寸"),
            ("刷新率", "ProMotion 自适应刷新率，最高 120Hz"),
            ("容量", "256GB、512GB、1TB、2TB"),
            ("接口", "USB-C"),
            ("生物识别", "Face ID"),
        ],
        "configs": [
            ("256GB", "银色、星宇橙色、深蓝色", "RMB 9,999"),
            ("512GB", "银色、星宇橙色、深蓝色", "RMB 11,999"),
            ("1TB", "银色、星宇橙色、深蓝色", "RMB 13,999"),
            ("2TB", "银色、星宇橙色、深蓝色", "RMB 17,999"),
        ],
        "buy": "想要最大屏幕和最长续航选 Pro Max。2TB 只建议重度视频创作者购买。",
    },
    {
        "file": "iphone-air.md",
        "name": "iPhone Air",
        "category": "手机",
        "series": "iPhone Air",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-air-finish-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["天蓝色", "浅金色", "云白色", "深空黑色"],
        "intro": "iPhone Air 主打轻薄设计，适合重视手感、外观和日常旗舰体验的用户。",
        "specs": [
            ("芯片", "A19 Pro"),
            ("显示屏", "Super Retina XDR 显示屏"),
            ("屏幕尺寸", "6.5 英寸"),
            ("刷新率", "ProMotion 自适应刷新率，最高 120Hz"),
            ("容量", "256GB、512GB、1TB"),
            ("接口", "USB-C"),
            ("生物识别", "Face ID"),
        ],
        "configs": [
            ("256GB", "全部发布颜色", "RMB 7,999"),
            ("512GB", "全部发布颜色", "RMB 9,999"),
            ("1TB", "全部发布颜色", "RMB 11,999"),
        ],
        "buy": "更在意轻薄手感选 iPhone Air。重度拍摄和长焦需求更建议 Pro 系列。",
    },
    {
        "file": "iphone-16e.md",
        "name": "iPhone 16e",
        "category": "手机",
        "series": "iPhone",
        "release": "2025 年 2 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-16e-finish-select-202502?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["黑色", "白色"],
        "intro": "iPhone 16e 是入门级 iPhone，适合预算敏感但想进入 iOS 生态的用户。",
        "specs": [
            ("芯片", "A18"),
            ("显示屏", "Super Retina XDR 显示屏"),
            ("容量", "128GB、256GB、512GB"),
            ("接口", "USB-C"),
            ("生物识别", "Face ID"),
        ],
        "configs": [
            ("128GB", "黑色、白色", "RMB 4,499"),
            ("256GB", "黑色、白色", "RMB 5,499"),
            ("512GB", "黑色、白色", "RMB 7,499"),
        ],
        "buy": "128GB 适合轻度用户。长期使用建议 256GB。",
    },
    {
        "file": "macbook-air.md",
        "name": "MacBook Air",
        "category": "电脑",
        "series": "MacBook",
        "release": "2026 年 1 月，M5 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/macbook-air-size-unselect-202601-gallery-1?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["午夜色", "星光色", "银色", "天蓝色"],
        "intro": "MacBook Air 是轻薄笔记本电脑，适合学习、办公、网页、文档、轻度剪辑和移动使用。",
        "specs": [
            ("芯片", "Apple M5"),
            ("屏幕", "13 英寸或 15 英寸 Liquid Retina 显示屏"),
            ("内存", "16GB 起"),
            ("存储", "256GB SSD 起"),
            ("续航", "最长约 18 小时"),
            ("接口", "MagSafe 3、Thunderbolt / USB 4、耳机接口"),
        ],
        "configs": [
            ("13 英寸 M5 / 16GB / 256GB", "全部发布颜色", "RMB 7,999 起"),
            ("13 英寸 M5 / 16GB / 512GB", "全部发布颜色", "RMB 9,499 起"),
            ("15 英寸 M5 / 16GB / 256GB", "全部发布颜色", "RMB 9,499 起"),
            ("15 英寸 M5 / 16GB / 512GB", "全部发布颜色", "RMB 10,999 起"),
        ],
        "buy": "办公学习选 13 英寸。想要大屏和更舒适分屏选 15 英寸。长期使用建议 512GB。",
    },
    {
        "file": "macbook-pro.md",
        "name": "MacBook Pro",
        "category": "电脑",
        "series": "MacBook Pro",
        "release": "2025 年 10 月起，M5 系列",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mbp14-spaceblack-select-202410?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["深空黑色", "银色"],
        "intro": "MacBook Pro 面向专业工作流，适合代码开发、视频剪辑、3D、音乐制作和长时间高负载任务。",
        "specs": [
            ("芯片", "Apple M5 / M5 Pro / M5 Max"),
            ("屏幕", "14 英寸或 16 英寸 Liquid Retina XDR 显示屏"),
            ("内存", "16GB 起"),
            ("存储", "512GB SSD 起"),
            ("接口", "Thunderbolt、HDMI、SDXC、MagSafe 3"),
        ],
        "configs": [
            ("14 英寸 M5 / 16GB / 512GB", "深空黑色、银色", "RMB 12,999 起"),
            ("14 英寸 M5 Pro / 24GB / 512GB", "深空黑色、银色", "RMB 16,999 起"),
            ("16 英寸 M5 Pro / 24GB / 512GB", "深空黑色、银色", "RMB 19,999 起"),
            ("16 英寸 M5 Max / 36GB / 1TB", "深空黑色、银色", "RMB 26,999 起"),
        ],
        "buy": "开发和剪辑选 M5 Pro。重度渲染、AI 和多轨视频选 M5 Max。",
    },
    {
        "file": "imac.md",
        "name": "iMac",
        "category": "电脑",
        "series": "Mac",
        "release": "2025 年，M5 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/imac-24-blue-selection-hero-202410?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["蓝色", "紫色", "粉色", "橙色", "黄色", "绿色", "银色"],
        "intro": "iMac 是一体式桌面电脑，适合家庭、前台、办公、教育和轻创作空间。",
        "specs": [
            ("芯片", "Apple M5"),
            ("屏幕", "24 英寸 4.5K Retina 显示屏"),
            ("内存", "16GB 起"),
            ("存储", "256GB SSD 起"),
            ("摄像头", "内置高清摄像头"),
        ],
        "configs": [
            ("M5 / 16GB / 256GB / 8 核图形处理器", "部分颜色", "RMB 10,999 起"),
            ("M5 / 16GB / 256GB / 10 核图形处理器", "全部发布颜色", "RMB 12,499 起"),
            ("M5 / 16GB / 512GB / 10 核图形处理器", "全部发布颜色", "RMB 14,499 起"),
        ],
        "buy": "家庭和办公选入门款。想要更多接口和颜色选 10 核图形处理器版本。",
    },
    {
        "file": "mac-mini.md",
        "name": "Mac mini",
        "category": "电脑",
        "series": "Mac",
        "release": "2025 年，M5 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mac-mini-hero-202410?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Mac mini 是小型台式 Mac，适合已有显示器、键盘和鼠标的办公、开发、家用服务器和轻创作用户。",
        "specs": [
            ("芯片", "Apple M5 / M5 Pro"),
            ("内存", "16GB 起"),
            ("存储", "256GB SSD 起"),
            ("接口", "Thunderbolt、HDMI、以太网、USB-C"),
        ],
        "configs": [
            ("M5 / 16GB / 256GB", "银色", "RMB 4,499 起"),
            ("M5 / 16GB / 512GB", "银色", "RMB 5,999 起"),
            ("M5 Pro / 24GB / 512GB", "银色", "RMB 10,999 起"),
        ],
        "buy": "入门办公和开发选 M5。多容器、视频和高负载选 M5 Pro。",
    },
    {
        "file": "mac-studio.md",
        "name": "Mac Studio",
        "category": "电脑",
        "series": "Mac",
        "release": "2025 年，M4 Max / M3 Ultra 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mac-studio-select-202503?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Mac Studio 是高性能桌面工作站，适合影视后期、3D、机器学习、音乐制作和大型工程。",
        "specs": [
            ("芯片", "M4 Max 或 M3 Ultra"),
            ("内存", "36GB 起"),
            ("存储", "512GB SSD 起"),
            ("接口", "Thunderbolt、HDMI、10Gb 以太网、SDXC"),
        ],
        "configs": [
            ("M4 Max / 36GB / 512GB", "银色", "RMB 16,499 起"),
            ("M3 Ultra / 96GB / 1TB", "银色", "RMB 32,999 起"),
        ],
        "buy": "创意专业工作选 M4 Max。极重度本地计算和多路素材选 M3 Ultra。",
    },
    {
        "file": "mac-pro.md",
        "name": "Mac Pro",
        "category": "电脑",
        "series": "Mac",
        "release": "2023 年，Apple 芯片款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mac-pro-tower-2023-gallery1?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Mac Pro 是可扩展专业工作站，适合需要 PCIe 扩展、机架部署或大型制作流程的专业团队。",
        "specs": [
            ("芯片", "M2 Ultra"),
            ("内存", "64GB 起"),
            ("存储", "1TB SSD 起"),
            ("形态", "塔式或机架式"),
            ("扩展", "PCIe 扩展插槽"),
        ],
        "configs": [
            ("塔式 M2 Ultra / 64GB / 1TB", "银色", "RMB 55,999 起"),
            ("机架式 M2 Ultra / 64GB / 1TB", "银色", "RMB 59,999 起"),
        ],
        "buy": "只在明确需要 PCIe 扩展或机房上架时选 Mac Pro。否则 Mac Studio 更划算。",
    },
    {
        "file": "ipad-pro.md",
        "name": "iPad Pro",
        "category": "平板",
        "series": "iPad",
        "release": "2025 年，M5 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/ipad-pro-model-select-gallery-1-202405?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色", "深空黑色"],
        "intro": "iPad Pro 是高端平板电脑，适合绘画、视频剪辑、文档创作、移动办公和高性能应用。",
        "specs": [
            ("芯片", "Apple M5"),
            ("屏幕", "11 英寸或 13 英寸 Ultra Retina XDR 显示屏"),
            ("容量", "256GB、512GB、1TB、2TB"),
            ("连接", "Wi-Fi 或 Wi-Fi + 蜂窝网络"),
            ("配件", "支持 Apple Pencil Pro 和妙控键盘"),
        ],
        "configs": [
            ("11 英寸 Wi-Fi / 256GB", "银色、深空黑色", "RMB 8,999 起"),
            ("11 英寸 Wi-Fi / 512GB", "银色、深空黑色", "RMB 10,499 起"),
            ("13 英寸 Wi-Fi / 256GB", "银色、深空黑色", "RMB 11,499 起"),
            ("13 英寸 Wi-Fi / 512GB", "银色、深空黑色", "RMB 12,999 起"),
        ],
        "buy": "绘画和移动办公选 11 英寸。剪辑、分屏和键盘使用选 13 英寸。",
    },
    {
        "file": "ipad-air.md",
        "name": "iPad Air",
        "category": "平板",
        "series": "iPad",
        "release": "2026 年，M4 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/ipad-air-model-select-gallery-1-202503?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["蓝色", "紫色", "星光色", "深空灰色"],
        "intro": "iPad Air 是均衡型平板，适合学习、笔记、绘画、娱乐和轻办公。",
        "specs": [
            ("芯片", "Apple M4"),
            ("屏幕", "11 英寸或 13 英寸 Liquid Retina 显示屏"),
            ("容量", "128GB、256GB、512GB、1TB"),
            ("连接", "Wi-Fi 或 Wi-Fi + 蜂窝网络"),
        ],
        "configs": [
            ("11 英寸 Wi-Fi / 128GB", "全部发布颜色", "RMB 4,799 起"),
            ("11 英寸 Wi-Fi / 256GB", "全部发布颜色", "RMB 5,599 起"),
            ("13 英寸 Wi-Fi / 128GB", "全部发布颜色", "RMB 6,499 起"),
            ("13 英寸 Wi-Fi / 256GB", "全部发布颜色", "RMB 7,299 起"),
        ],
        "buy": "学生和笔记选 11 英寸。看课件、分屏和轻办公选 13 英寸。",
    },
    {
        "file": "ipad.md",
        "name": "iPad",
        "category": "平板",
        "series": "iPad",
        "release": "2025 年，A16 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/ipad-finish-select-202503?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["蓝色", "粉色", "黄色", "银色"],
        "intro": "iPad 是入门平板电脑，适合学习、网课、视频、阅读和家庭娱乐。",
        "specs": [
            ("芯片", "A16"),
            ("屏幕", "11 英寸 Liquid Retina 显示屏"),
            ("容量", "128GB、256GB、512GB"),
            ("连接", "Wi-Fi 或 Wi-Fi + 蜂窝网络"),
        ],
        "configs": [
            ("Wi-Fi / 128GB", "全部发布颜色", "RMB 2,999 起"),
            ("Wi-Fi / 256GB", "全部发布颜色", "RMB 3,999 起"),
            ("Wi-Fi / 512GB", "全部发布颜色", "RMB 5,999 起"),
        ],
        "buy": "家庭娱乐和网课选 128GB。长期学习和下载资料选 256GB。",
    },
    {
        "file": "ipad-mini.md",
        "name": "iPad mini",
        "category": "平板",
        "series": "iPad",
        "release": "2024 年，A17 Pro 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/ipad-mini-finish-select-gallery-202410?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["蓝色", "紫色", "星光色", "深空灰色"],
        "intro": "iPad mini 是小尺寸平板，适合阅读、随身笔记、游戏和移动查看资料。",
        "specs": [
            ("芯片", "A17 Pro"),
            ("屏幕", "8.3 英寸 Liquid Retina 显示屏"),
            ("容量", "128GB、256GB、512GB"),
            ("连接", "Wi-Fi 或 Wi-Fi + 蜂窝网络"),
        ],
        "configs": [
            ("Wi-Fi / 128GB", "全部发布颜色", "RMB 3,999 起"),
            ("Wi-Fi / 256GB", "全部发布颜色", "RMB 4,799 起"),
            ("Wi-Fi / 512GB", "全部发布颜色", "RMB 6,399 起"),
        ],
        "buy": "便携优先选 iPad mini。需要键盘生产力选 iPad Air 或 iPad Pro。",
    },
    {
        "file": "apple-watch-series-11.md",
        "name": "Apple Watch Series 11",
        "category": "手表",
        "series": "Apple Watch",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-s11-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["铝金属多色", "钛金属多色"],
        "intro": "Apple Watch Series 11 是主流智能手表，适合健康监测、运动记录、通知和 iPhone 协同。",
        "specs": [
            ("尺寸", "42mm、46mm"),
            ("连接", "GPS 或 GPS + 蜂窝网络"),
            ("功能", "健康监测、运动记录、通知、Apple Pay"),
            ("防水", "适合游泳场景"),
        ],
        "configs": [
            ("42mm 铝金属 GPS", "多色", "RMB 2,999 起"),
            ("46mm 铝金属 GPS", "多色", "RMB 3,199 起"),
            ("蜂窝网络版本", "多色", "在 GPS 版基础上加价"),
        ],
        "buy": "多数人选铝金属 GPS。需要脱离 iPhone 接打电话和联网选蜂窝网络版。",
    },
    {
        "file": "apple-watch-ultra-3.md",
        "name": "Apple Watch Ultra 3",
        "category": "手表",
        "series": "Apple Watch Ultra",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-ultra-3-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["原色钛金属", "黑色钛金属"],
        "intro": "Apple Watch Ultra 3 面向户外、耐力运动和长续航用户，机身更坚固，定位和运动能力更强。",
        "specs": [
            ("尺寸", "49mm"),
            ("材质", "钛金属"),
            ("连接", "GPS + 蜂窝网络"),
            ("功能", "户外运动、潜水、长续航、健康监测"),
        ],
        "configs": [
            ("49mm 钛金属 GPS + 蜂窝网络", "原色钛金属、黑色钛金属", "RMB 6,499 起"),
        ],
        "buy": "户外、跑步、骑行、潜水和长续航需求选 Ultra。普通健康记录选 Series。",
    },
    {
        "file": "apple-watch-se-3.md",
        "name": "Apple Watch SE 3",
        "category": "手表",
        "series": "Apple Watch SE",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-se-3-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["午夜色", "星光色", "银色"],
        "intro": "Apple Watch SE 3 是入门款 Apple Watch，适合基础运动、通知和健康记录。",
        "specs": [
            ("尺寸", "40mm、44mm"),
            ("连接", "GPS 或 GPS + 蜂窝网络"),
            ("功能", "运动记录、通知、基础健康功能"),
        ],
        "configs": [
            ("40mm GPS", "午夜色、星光色、银色", "RMB 1,999 起"),
            ("44mm GPS", "午夜色、星光色、银色", "RMB 2,199 起"),
            ("蜂窝网络版本", "午夜色、星光色、银色", "在 GPS 版基础上加价"),
        ],
        "buy": "预算优先选 SE。需要更完整健康功能和常亮屏选 Series。",
    },
    {
        "file": "airpods-4.md",
        "name": "AirPods 4",
        "category": "耳机",
        "series": "AirPods",
        "release": "2024 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/airpods-4-select-202409?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["白色"],
        "intro": "AirPods 4 是开放式真无线耳机，适合通勤、通话、视频和日常音乐。",
        "specs": [
            ("形态", "开放式真无线耳机"),
            ("芯片", "H2"),
            ("功能", "个性化空间音频、自动切换、查找"),
            ("接口", "USB-C 充电盒"),
        ],
        "configs": [
            ("标准版", "白色", "RMB 999"),
            ("主动降噪版", "白色", "RMB 1,399"),
        ],
        "buy": "不喜欢入耳式选 AirPods 4。通勤降噪选主动降噪版。",
    },
    {
        "file": "airpods-pro-3.md",
        "name": "AirPods Pro 3",
        "category": "耳机",
        "series": "AirPods Pro",
        "release": "2025 年 9 月",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/airpods-pro-3-hero-select-202509?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["白色"],
        "intro": "AirPods Pro 3 是入耳式降噪耳机，适合通勤、办公、运动和沉浸听音。",
        "specs": [
            ("形态", "入耳式真无线耳机"),
            ("功能", "主动降噪、通透模式、空间音频、心率感测"),
            ("接口", "USB-C 充电盒"),
        ],
        "configs": [
            ("AirPods Pro 3", "白色", "RMB 1,899"),
        ],
        "buy": "需要降噪、通勤和运动监测，优先选 AirPods Pro 3。",
    },
    {
        "file": "airpods-max.md",
        "name": "AirPods Max",
        "category": "耳机",
        "series": "AirPods Max",
        "release": "2024 年 9 月，USB-C 款",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/airpods-max-select-202409?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["午夜色", "星光色", "蓝色", "紫色", "橙色"],
        "intro": "AirPods Max 是头戴式无线耳机，适合高品质音乐、降噪办公和沉浸影音。",
        "specs": [
            ("形态", "头戴式无线耳机"),
            ("功能", "主动降噪、通透模式、空间音频"),
            ("接口", "USB-C"),
        ],
        "configs": [
            ("AirPods Max USB-C", "全部发布颜色", "RMB 3,999"),
        ],
        "buy": "喜欢头戴式舒适和强降噪选 AirPods Max。便携优先选 AirPods Pro。",
    },
    {
        "file": "apple-vision-pro.md",
        "name": "Apple Vision Pro",
        "category": "头戴式 VR/空间计算设备",
        "series": "Apple Vision",
        "release": "2024 年 6 月，中国大陆上市",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/apple-vision-pro-select-202401?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Apple Vision Pro 是头戴式空间计算设备，可用于沉浸影音、空间照片视频、办公窗口和 3D 内容体验。",
        "specs": [
            ("芯片", "M2 + R1"),
            ("显示", "双 Micro-OLED 显示系统"),
            ("交互", "眼动、手势、语音"),
            ("容量", "256GB、512GB、1TB"),
        ],
        "configs": [
            ("256GB", "银色", "RMB 29,999"),
            ("512GB", "银色", "RMB 31,499"),
            ("1TB", "银色", "RMB 32,999"),
        ],
        "buy": "重视空间影音和新交互体验可选。多数用户建议先线下体验再买。",
    },
    {
        "file": "homepod-mini.md",
        "name": "HomePod mini",
        "category": "音箱",
        "series": "HomePod",
        "release": "2020 年，后续新增颜色",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/homepod-mini-select-202110?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["白色", "午夜色", "蓝色", "黄色", "橙色"],
        "intro": "HomePod mini 是小型智能音箱，适合 Apple Music、智能家居控制和多房间音频。",
        "specs": [
            ("形态", "智能音箱"),
            ("功能", "Siri、智能家居中枢、多房间播放"),
            ("连接", "Wi-Fi、蓝牙、Thread"),
        ],
        "configs": [
            ("HomePod mini", "全部发布颜色", "RMB 749"),
        ],
        "buy": "适合苹果生态家庭和小房间。追求更强低频和音量可选 HomePod。",
    },
    {
        "file": "apple-tv-4k.md",
        "name": "Apple TV 4K",
        "category": "电视盒子",
        "series": "Apple TV",
        "release": "2022 年",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/apple-tv-4k-hero-select-202210?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["黑色"],
        "intro": "Apple TV 4K 是电视盒子，适合 Apple TV+、流媒体、AirPlay、家庭中枢和 Apple Arcade。",
        "specs": [
            ("芯片", "A15 Bionic"),
            ("画质", "4K HDR、Dolby Vision"),
            ("音频", "Dolby Atmos"),
            ("遥控器", "Siri Remote"),
        ],
        "configs": [
            ("64GB Wi-Fi", "黑色", "RMB 1,299 起"),
            ("128GB Wi-Fi + 以太网", "黑色", "RMB 1,499 起"),
        ],
        "buy": "普通流媒体选 64GB。智能家居中枢和有线网络需求选 128GB 以太网版。",
    },
    {
        "file": "studio-display.md",
        "name": "Studio Display",
        "category": "显示器",
        "series": "Display",
        "release": "2022 年",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/studio-display-gallery-1-202203?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Studio Display 是 27 英寸 5K 显示器，适合 Mac 桌面办公、设计和内容创作。",
        "specs": [
            ("尺寸", "27 英寸"),
            ("分辨率", "5K Retina"),
            ("亮度", "600 尼特"),
            ("摄像头", "内置超广角摄像头"),
            ("音频", "六扬声器系统"),
        ],
        "configs": [
            ("标准玻璃 / 倾斜可调支架", "银色", "RMB 11,499 起"),
            ("纳米纹理玻璃 / 倾斜可调支架", "银色", "RMB 13,499 起"),
            ("高度可调支架版本", "银色", "加价选配"),
        ],
        "buy": "Mac 桌面用户想要高分辨率、摄像头和扬声器一体化，选 Studio Display。",
    },
    {
        "file": "pro-display-xdr.md",
        "name": "Pro Display XDR",
        "category": "显示器",
        "series": "Display",
        "release": "2019 年",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/pro-display-gallery1-201909?wid=1200&hei=630&fmt=jpeg&qlt=95",
        "colors": ["银色"],
        "intro": "Pro Display XDR 是专业参考级显示器，适合影视调色、HDR 制作、摄影和高端设计工作流。",
        "specs": [
            ("尺寸", "32 英寸"),
            ("分辨率", "6K Retina"),
            ("亮度", "XDR 峰值亮度"),
            ("玻璃", "标准玻璃或纳米纹理玻璃"),
        ],
        "configs": [
            ("标准玻璃", "银色", "RMB 39,999 起"),
            ("纳米纹理玻璃", "银色", "RMB 47,999 起"),
            ("Pro Stand", "银色", "RMB 7,799"),
            ("VESA Mount Adapter", "银色", "RMB 1,599"),
        ],
        "buy": "专业 HDR 和参考监看需求选 Pro Display XDR。普通 Mac 办公选 Studio Display。",
    },
]


def md_table(rows):
    out = ["| 项目 | 内容 |", "|---|---|"]
    out.extend(f"| {k} | {v} |" for k, v in rows)
    return "\n".join(out)


def config_table(rows):
    out = ["| 配置 | 可选颜色 | 中国价格 |", "|---|---|---:|"]
    out.extend(f"| {a} | {b} | {c} |" for a, b, c in rows)
    return "\n".join(out)


for product in products:
    colors = "、".join(product["colors"])
    content = f"""# {product["name"]}

![{product["name"]} 官方产品图]({product["image"]})

## 基本信息

{md_table([
    ("产品名", product["name"]),
    ("品牌", "Apple"),
    ("分类", product["category"]),
    ("系列", product["series"]),
    ("发布时间", product["release"]),
    ("同期发布颜色", colors),
])}

## 产品介绍

{product["intro"]}

## 同期发布颜色

| 颜色 | 说明 |
|---|---|
{chr(10).join(f"| {color} | 官方发布配色 |" for color in product["colors"])}

## 核心卖点

- Apple 生态深度协同，适合与 iPhone、iPad、Mac、Apple Watch 等设备联动。
- 官方渠道价格透明，支持分期、送货、到店取货和 Apple Trade In 换购。
- 适合看重长期系统更新、硬件做工和售后服务的用户。

## 参数

{md_table(product["specs"])}

## 可选配置及中国价格

> 价格口径：中国大陆 Apple 官方在线商店起售价或常见基础配置价格，单位为人民币。实际成交价可能因渠道、促销、教育优惠、以旧换新、分期和库存变化。

{config_table(product["configs"])}

## 电商式购买建议

{product["buy"]}

## 适合人群

- 已在 Apple 生态内，想要更好设备协同的用户。
- 重视官方售后、系统更新和产品生命周期的用户。
- 想按预算和配置清晰选购的用户。

## 数据来源

- Apple 中国大陆官网产品页和在线商店页面。
- Apple 中国大陆官网技术规格页面。
- 中国大陆公开发售信息和 Apple 官方新闻稿。
"""
    (DOCS_DIR / product["file"]).write_text(content, encoding="utf-8")

print(f"已生成 {len(products)} 个产品文档到 {DOCS_DIR.resolve()}")
