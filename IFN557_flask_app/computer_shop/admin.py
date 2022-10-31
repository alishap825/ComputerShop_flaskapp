from .models import Brand, Product
from .enums import ProductCategory

# Creates test data for the web app


def create_data(db):
    # Create Brands
    apple = Brand(name='Apple', description='Apple manufactures Macbooks and accessories.', logo='https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?202210240635')
    dell = Brand(name='Dell', description='Dell manufactures Laptops and Desktops.', logo='xx')
    logitech = Brand(name='Logitech', description='Logitech manufactures computer accessories.', logo='xx')
    lenovo = Brand(name='Lenovo', description='Lenovo manufactures Laptops, Desktops and Computer accessories.', logo='xx')
    seagate = Brand(name='Seagate', description='Seagate manufactures Computer accessories like Hard Disk Drives(HDDs) and Solid State Drives(SSDs).', logo='xx')

    print(str(logitech))

    # Create Products
    dell_product_1 = Product(
        name='DELL 27 Inch Gaming Monitor, QHD (2560 x 1440) up to 165Hz, 1ms Response Time, AMD FreeSync Premium Pro, VESA HDR400, Colour Grey',
        description="""
        27 inch Gaming Monitor features In-Plane Switching (IPS) technology for incredible speed and amazing colour performance from every angle.
        Quick native 165Hz refresh rate allows fast-moving visuals to be seen with incredible clarity so you can react quicker. True 1ms GtG response time eliminates motion blur.
        NVIDIA G-SYNC Technology and AMD FreeSync Premium Pro technology adds another layer of seamless, low latency HDR gaming.
        """,
        specifications="""
        Style Name: S2721DGF|
        Screen size:27 Inches|
        Display resolution maximum:2560 x 1440 Pixels|
        Special feature:Height Adjustment, Adaptive Sync, Blue Light Filter, Tilt Adjustment, Flicker-Free|
        Refresh rate:165 Hz
        """,
        category=ProductCategory.ACCESSORY,
        original_price=749.00,
        discount_price=549.00,
        image='https://m.media-amazon.com/images/I/71U9XYFbR0L._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/61Nbvk-GkuL._AC_SX679_.jpg',
        brand=dell
    )

    dell_product_2 = Product(
        name='Inspiron 27 All-in-One',
        description="""
        The choice between a sleek, slim do-it-all PC in Dark Shadow Gray or Pearl White is yours. The whole family will be competing for screen time, thanks to it's near narrow 4-sided borders and a FHD IPS display with 99% sRGB coverage and blue light reducing ComfortView Plus.
        """,
        specifications="""
        Processor:12 Gen Intel® Core™ i7-1255U (12 MB cache, 10 cores, 12 threads, up to 4.70 GHz Turbo)|
        Operating System(Dell Technologies recommends Windows 11 Pro for business):Windows 11 Home, English|
        Video Card:Intel® Iris® Xe Graphics|
        Monitor:27", FHD 1920 x 1080, 60Hz, WVA, Touch, InfinityEdge, Narrow Border|
        Memory:16GB, 2x8GB, DDR4, 3200MHz|
        Hard Drive:512GB Solid State Drive (Boot) + 1TB 5400RPM Hard Drive (Storage)
        """,
        category=ProductCategory.DESKTOP,
        original_price=2028.00,
        discount_price=1999.00,
        image='https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/desktops/inspiron-desktops/27-7710/media-gallery/gray/aio-desktop-inspiron-27-7710-gray-gallery-4.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=529&qlt=100,1&resMode=sharp2&size=529,402&chrss=full',
        image_2='https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/desktops/inspiron-desktops/27-7710/media-gallery/gray/aio-desktop-inspiron-27-7710-gray-gallery-8.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=290&qlt=100,1&resMode=sharp2&size=290,402&chrss=full',
        brand=dell
    )

    dell_product_3 = Product(
        name='Inspiron 24 All-in-One',
        description="""
        The choice between a sleek, slim do-it-all PC in Dark Shadow Gray or Pearl White is yours. The whole family will be competing for screen time, thanks to it's near narrow 4-sided borders and a FHD IPS display with 99% sRGB coverage and blue light reducing ComfortView Plus.
        """,
        specifications="""
        Processor:12 Gen Intel® Core™ i3-1215U (10 MB cache, 6 cores, 8 threads, up to 4.40 GHz Turbo)|
        Operating System(Dell Technologies recommends Windows 11 Pro for business):Windows 11 Home, English|
        Video Card:Intel® UHD Graphics|
        Monitor:23.8-inch FHD (1920 x 1080) Anti-Glare Narrow Border AIT Infinity Non-Touch Display|
        Memory:8GB, 1x8GB, DDR4, 3200MHz|
        Hard Drive:256 GB, M.2, PCIe NVMe, SSD
        """,
        category=ProductCategory.DESKTOP,
        original_price=1228.00,
        discount_price=1099.00,
        image='https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/desktops/inspiron-desktops/24-5410/media-gallery/gray/aio-desktop-inspiron-24-5410-gray-gallery-3.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=541&qlt=100,1&resMode=sharp2&size=541,402&chrss=full',
        image_2='https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/desktops/inspiron-desktops/24-5410/media-gallery/gray/aio-desktop-inspiron-24-5410-gray-gallery-10.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=1105&qlt=100,1&resMode=sharp2&size=1105,402&chrss=full',
        brand=dell
    )

    dell_product_4 = Product(
        name='DELL Gaming G15 Ryzen Edition, 15.6 inch FHD (1920 x 1080) 120Hz Laptop - AMD Ryzen 5 6600H , 16GB, 512GB SSD, NVIDIA GeForce RTX 3050 , Windows 11 Home - Dark Shadow Grey Model (RNG55251000AU)',
        description="""Model_Year: 2022
        Total_Usb_Ports: 4
        Connectivity_Technology: Hdmi
        Wireless_Comm_Standard: 802_11_Ax
        15.6 inch FHD (1920 x 1080) 120Hz 250 nits WVA Anti- Glare LED Backlit Narrow Border Display
        AMD Ryzen 5 6600H Mobile
        16GB, 2x8GB, DDR5, 4800MHz
        """,
        specifications="""
        Screen size:15 Inches|
        Colour:Gray|
        CPU model:Ryzen 5|
        RAM memory installed size:16 GB|
        Operating System:Windows 11 Home
        """,
        category=ProductCategory.LAPTOP,
        original_price=749.00,
        discount_price=549.00,
        image='https://m.media-amazon.com/images/I/71EAPm12rIL._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/61RX97mwZ3L._AC_SX679_.jpg',
        brand=dell
    )
    dell_product_5 = Product(
        name='Dell Wireless Keyboard and Mouse, Multi-Device Connectivity, Programmable Buttons, Regarchable 36 Month Battery Life, Titan Gray, KM7120W',
        description="""Seamlessly connect your wireless keyboard and mouse combo to three PCs. Bluetooth 5.0 and 2.4GHz wireless connections let you switch across multiple devices with one click.
        Multi-Device compatibility with Windows, Chrome, Android and Mac provide maximum flexibility across devices. Pair each device with your compatible system without configuring settings.
        Rapid responses via the 1600 DPI sensory. Optical sensors offer accurate tracking on most surfaces. Rechargeable 36 months of battery life lasts 3 times longer than its previous generation.
        """,
        specifications="""
        Colour:Titan Gray|
        Connectivity technology:Bluetooth|
        Compatible devices:Laptop, Personal Computer|
        Keyboard description:Multi Functional""",
        category=ProductCategory.ACCESSORY,
        original_price=149.00,
        discount_price=119.00,
        image='https://m.media-amazon.com/images/I/8159u0zcFBL._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/71K3WiskeoL._AC_SX679_.jpg',
        brand=dell
    )
    seagate_product_1 = Product(
        name='Seagate 2TB Expansion Portable HDD',
        description="""Sleek and simple portable drive design for taking photos, movies, music, and more on-the-go
        Enjoy peace of mind with the Rescue Data Recovery Services
        Automatic recognition of Windows and Mac computers for simple setup (Reformatting required for use with Time Machine)
        Take advantage of the fast data transfer speeds by connecting to a USB 3.0 port.""",
        specifications="""Digital storage capacity:2 TB|
        Hard disk interface:USB 3.0|
        Connectivity technology:USB|
        Special feature:Portable|
        Hard disk form factor:2.5 Inches|
        Hard disk description:Hybrid Drive|
        Compatible devices:Laptop, Desktop|
        Installation type:External Hard Drive|
        Colour:Black Expansion""",
        category=ProductCategory.ACCESSORY,
        original_price=99.00,
        discount_price=79.00,
        image='https://m.media-amazon.com/images/I/81pAOJFcsFS._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/81TNgX5KgOS._AC_SX679_.jpg',
        brand=seagate
    )

    seagate_product_2 = Product(
        name='Seagate BarraCuda',
        description="""3.5" 2TB SATA Internal Desktop Hard Drive HDD 256MB ST2000DM008.""",
        specifications="""
        Digital storage capacity:2 TB|
        Connector Type:SATA|
        Special feature:For Gaming|
        Hard disk form factor:2.5 Inches|
        Compatible Devices:Laptop, Desktop|
        Hard disk size:2 TB|
        Hard disk rotational speed:7200 RPM|
        Specific uses for product:Personal, Gaming|
        Read speed:180 Megabytes Per Second
        """,
        category=ProductCategory.ACCESSORY,
        original_price=89.00,
        discount_price=59.00,
        image='https://m.media-amazon.com/images/I/614AgguDz9L._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/71XFaoMUMWL._AC_SX679_.jpg',
        brand=seagate
    )

    seagate_product_3 = Product(
        name='Seagate 16TB HDD Exos X16 7200 RPM 512e/4Kn SATA 6Gb/s 256MB Cache 3.5-Inch Enterprise Hard Drive (ST16000NM001G)',
        description="""Industry's lowest power and weight for optimum data center TCO
        PowerBalance feature optimizes IOPS/Watt
        Proven enterprise-class reliability backed by 2. 5M-hr MTBF rating
        Helium sealed-drive design with no porosity and uniform density
        Seagate Secure models provide hardware-based security to help protect data-at-rest. With Instant Secure Erase, drive retirement is safe, affordable, fast and easy.""",
        specifications="""
        Digital storage capacity:16 TB|
        Hard disk interface:Serial ATA|
        Connectivity technology:SATA|
        Special feature:512e/4Kn format support|
        Hard disk form factor:2.5 Inches|
        Hard disk description:Mechanical Hard Disk|
        Compatible devices:Storage System|
        Installation type:Internal Hard Drive|
        Colour:Silver
        """,
        category=ProductCategory.ACCESSORY,
        original_price=689.00,
        discount_price=659.00,
        image='https://m.media-amazon.com/images/I/712S0gBsC5L._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/81Trg+Ef-OL._AC_SX679_.jpg',
        brand=seagate
    )

    apple_product_1 = Product(
        name='MacBook Air - M2 chip',
        description="""M2 is the next generation of Apple silicon. Its 8-core CPU lets you zip through everyday
        tasks like creating documents and presentations, or take on more intensive workflows like developing in Xcode or mixing tracks in Logic Pro.
        M2 features up to a 10-core GPU,
        resulting in a big boost in graphics performance. 
        And its media engine lets you play and edit up to 11 streams of 4K and up to two streams of 8K ProRes video.""",
        specifications="""Display:13-inch Retina display with True Tone|
        Memory:8GB unified memory|
        Storage:256GB|
        Storage type:SSD storage|
        USB:Three Thunderbolt/USB 4 ports|
        Adapter:140W USB-C Power Adapter|
        Additional:Magic Keyboard with Touch Bar and Touch ID""",
        category=ProductCategory.LAPTOP,
        original_price=1999.00,
        discount_price=1799.00,
        image='https://cdn.shopify.com/s/files/1/0024/9803/5810/products/494995-Product-0-I-637406991736141585_467x.jpg?v=1649907466',
        image_2='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/mbp-spacegray-select-202206?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1664497359481',
        brand=apple
    )
    apple_product_2 = Product(
        name='24″ iMac',
        description="""Apple M1 Chip 8-Core CPU 8-Core GPU 256GB""",
        specifications="""Display:24-inch 4.5K Retina display|
        Memory:8GB unified memory|
        Storage:256GB|
        Storage type:SSD storage|
        USB:Two Thunderbolt/USB 4 ports, Two USB 3 ports|
        Adapter:30W USB-C Power Adapter|
        Additional:Magic Keyboard with Touch ID""",
        category=ProductCategory.DESKTOP,
        original_price=2199.00,
        discount_price=1999.00,
        image='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/imac-24-blue-selection-hero-202104?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1617492405000',
        brand=apple
    )
    apple_product_3 = Product(
        name='24″ iMac',
        description="""Apple M1 Chip 8-Core CPU 8-Core GPU 512GB""",
        specifications="""Display:24-inch 4.5K Retina display|
        Memory:8GB unified memory|
        Storage:512GB|
        Storage type:SSD storage|
        USB:Two Thunderbolt/USB 4 ports, Two USB 3 ports|
        Adapter:30W USB-C Power Adapter|
        Additional:Magic Keyboard with Touch ID""",
        category=ProductCategory.DESKTOP,
        original_price=2499.00,
        discount_price=2299.00,
        image='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/imac-24-blue-selection-hero-202104?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1617492405000',
        brand=apple
    )
    apple_product_4 = Product(
        name='Apple Watch - Midnight Aluminium Case with Sport Band',
        description="""The aluminium case is lightweight and made from 100 per cent recycled aerospace-grade alloy.
        The Sport Band is made from a durable yet surprisingly soft high-performance fluoroelastomer, with 
        an innovative pin-and-tuck closure.""",
        specifications="""Case Size:45-mm|
        Connectivity:GPS+Cellular|
        Ban Size:Regular|
        Compatibility:iPhone 8 or later with iOS 16 or later|
        Water-Resistant:Yes""",
        category=ProductCategory.ACCESSORY,
        original_price=679.00,
        discount_price=599.00,
        image='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MKU83_VW_34FR+watch-41-alum-midnight-nc-8s_VW_34FR_WF_CO_GEO_AU?wid=1400&hei=1400&trim=1%2C0&fmt=p-jpg&qlt=95&.v=1632171038000%2C1661971864111',
        image_2='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MKU83_VW_PF+watch-41-alum-midnight-nc-8s_VW_PF_WF_CO_GEO_AU?wid=1400&hei=1400&trim=1%2C0&fmt=p-jpg&qlt=95&.v=1632171035000%2C1661972060316',
        brand=apple
    )

    apple_product_5 = Product(
        name='MacBook Pro',
        description="""M1 Pro delivers game-changing performance with amazing battery life. It features up to 10
        CPU cores and up to 16 GPU cores, as well as a 16-core Neural Engine,
        and a powerful media engine that can play as many as four streams of 8K video. 
        Delivering 200GB/s of memory bandwidth, M1 Pro can be configured with up to 32GB of unified memory to 
        handle complex professional workflows.""",
        specifications="""Display:26-inch Retina display|
        Memory:16GB unified memory|
        Storage:512GB|
        Storage type:SSD storage|
        USB:Three Thunderbolt/USB 4 ports, Two USB 3 ports, 1 HDMI port|
        Adapter:140W USB-C Power Adapter|
        Additional:Magic Keyboard with Touch ID""",
        category=ProductCategory.LAPTOP,
        original_price=3749.00,
        discount_price=3549.00,
        image='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/mbp16-spacegray-select-202110?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1632788574000',
        image_2='https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/mbp16-silver-select-202110?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1632788573000',
        brand=apple
    )

    lenovo_product_1 = Product(
        name='Lenovo IdeaCentre 3i 24" Pentium Gold',
        description="""Lenovo desktop's 2 GHz Intel Pentium dual-core processor. Its 8 GB of memory lets you improve 
        your computer's performance. Plus, the Lenovo F0G000TJAU has a 24-inch display, 
        so you can focus on clear graphics""",
        specifications='Display:14-inch|RAM:8 GB|Storage:1 TB|OS:Windows 11|Series:F0G000TJAU',
        category=ProductCategory.DESKTOP,
        original_price=899.00,
        discount_price=749.00,
        image='https://thegoodguys.sirv.com/products/50079260/50079260_802365.PNG?scale.height=505&scale.width=773&canvas.height=505&canvas.width=773&canvas.opacity=0&q=90',
        brand=lenovo
    )

    lenovo_product_2 = Product(
        name='Lenovo HDMI to VGA Adapter (Male to Female) with 3.5mm Audio Jack for Computer, Desktop, Laptop, PC, Monitor, Projector, HDTV, Chromebook, Raspberry Pi, Roku, Xbox and More',
        description="""
        HDMI to VGA with audio converter support Video output in VGA: 1920*1080@60Hz(Max).
        VGA can only process Video signal, but this adapter additionally provids with a 
        3.5mm line-out jack. Let you connect this adapter to your TV or external speakers through a 3.5mm 
        jack audio cable
        """,
        specifications="""
        Compatible Devices:Projector, Laptop, TV, Monitor, PC, Xbox|
        Connector type:VGA, Auxiliary, Micro USB, HDMI|
        Connector gender:Male-to-Female|
        Series:Thinkpad|
        Number of ports:4
        """,
        category=ProductCategory.ACCESSORY,
        original_price=59.00,
        discount_price=39.00,
        image='https://m.media-amazon.com/images/I/51FoWmYbqhL._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/512cPtUne5L._AC_SX679_.jpg',
        brand=lenovo
    )

    lenovo_product_3 = Product(
        name='Lenovo Legion Star Y660 Pro Stereo Gaming Headset, 7.1 Surround Sound Capable, 50mm Drivers, Memory Foam Cushion, Over Ear USB Wired Headphones with Mic and LED Light, Competible with PC, PS4 and More',
        description="""
        Legion Star Y660 Pro gaming headset equip built-in USB audio sound chip with 7.1 
        surround sound. Combine with 50mm magnetic neodymium driver, create an immersive 
        gaming experience with stereo surround sound in the game. More clear sound gaming 
        headset, acoustic positioning precision, Glaring LED lights are designed on the 
        earcups , highlighting the atmosphere of the game.
        """,
        specifications="""
        Form factor:Over Ear|
        Connector Type:Wired|
        Special feature:Game, Lightweight, Volume_control, Noise-cancellation|
        Age range (description):Adult""",
        category=ProductCategory.ACCESSORY,
        original_price=93.00,
        discount_price=69.00,
        image='https://m.media-amazon.com/images/I/51uFhxcHXzL._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/41aqnzFOF2L._AC_.jpg',
        brand=lenovo
    )

    lenovo_product_4 = Product(
        name='Lenovo IdeaPad Duet 5 Chromebook, Snapdragon 7c Gen 2, 8GB RAM, 256GB eMMC, 13.3 Inch FHD, Detachable Keyboard, USI Pen, Chrome OS, Storm Grey, 82QS000AAU',
        description="""
        13.3 inch FHD OLED 1920 x 1080 resolution display
        Detachable design with detachable keybaord and Lenovo USI Pen
        Memory and Storage : 8GB RAM and 256GB eMMC
        Processor and Battery life: Qualcomm Snapdragon SC7180 and up to 15 hours of battery life
        Google Chrome OS: Chrome OS is the speedy, simple and secure operating system that powers every Chromebook; Chromebooks start fast and stay fast with automatic updates, built in virus protection and up to 10hrs of battery life.
        """,
        specifications="""
        Series:82QS000AAU|
        Screen size:13.3 Inches|
        Colour:Grey|
        CPU model:Snapdragon|
        RAM memory installed size:8 GB
        """,
        category=ProductCategory.LAPTOP,
        original_price=893.00,
        discount_price=769.00,
        image='https://m.media-amazon.com/images/I/71QmbnaW75L._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/816lgtAdh3L._AC_SX679_.jpg',
        brand=lenovo
    )

    lenovo_product_5 = Product(
        name='Lenovo Webcam HD 1080p Web Camera, USB PC Computer Webcam with Microphone, Laptop Desktop Full HD Camera Video Webcam, Pro Streaming Webcam for Recording, Calling, Conferencing, Gaming',
        description="""
        080P Full HD Webcam:This 1080P webcam supply crisp image and crystal clear video. Enjoy razor sharp high Def in every environment. 5 M pixels, high definition and true color images.Web camera with fixed focus allows you to find the fit angle in your live streaming or video conferencing. Make sure you look your best during video calls and live streaming.
        """,
        specifications="""
        Series:Thinkpad|
        Connector Type:USB|
        Special feature:Low_light, Anti_shake|
        Video capture resolution:1080p|
        Lens type:Wide Angle
        """,
        category=ProductCategory.ACCESSORY,
        original_price=93.00,
        discount_price=69.00,
        image='https://m.media-amazon.com/images/I/415MQlG1JNL._AC_SX679_.jpg',
        image_2='https://m.media-amazon.com/images/I/61ukRYw-HiL._AC_SY879_.jpg',
        brand=lenovo
    )

    logitech_product_1 = Product(
        name='Logitech G G733 Lightspeed Wireless RGB Gaming Headset',
        description="""Total freedom with up to 20 m wireless range and LIGHTSPEED wireless audio transmission. Keep playing for up to 29 hours of battery life.
    Colourful, reversible suspension headbands are designed for comfort during long play sessions.
    The colourful, reversible suspension headband is designed for comfort during long play sessions""",
        specifications='Series:G733|Colour:BLACK|Connectivity technology:Wireless|Special features:gaming, wireless',
        category=ProductCategory.ACCESSORY,
        original_price=199.00,
        discount_price=149.00,
        image='https://m.media-amazon.com/images/I/71xNjrzG69L._AC_SX522_.jpg',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1560/3259/g73305__09370.1608252378.jpg?c=2',
        brand=logitech
    )
    logitech_product_2 = Product(
        name='Logitech G G733 Lightspeed Wireless RGB Gaming Headset',
        description="""Total Freedom With Up To 20 M Range And Lightspeed Wireless Audio Transmission
    Keep Playing For Up To 29 Hours Of Battery Life
    Rgb Lighting – Personalise Your Headset Lighting Across The Full Spectrum Of 16.8M Colours""",
        specifications='Series:G733|Colour:WHITE|Form factor:Over Ear|Connectivity technology:Wireless',
        category=ProductCategory.ACCESSORY,
        original_price=199.00,
        discount_price=149.00,
        image='https://m.media-amazon.com/images/I/71RSZdY7pJL._AC_SX522_.jpg',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1559/3247/g733white05__87161.1608251177.jpg?c=2',
        brand=logitech
    )
    logitech_product_3 = Product(
        name='Logitech MK550 Comfort Wave Wireless Keyboard & Mouse Combo',
        description="""A mouse-and-keyboard combo that gives you a comfort curve without the learning curve. No messy 
        cables to untangle and save on desk space with the Logitech MK550 Wireless Keyboard and Mouse Wave Combo.""",
        specifications="""Serial Number:920-002555|Colour:BLACK|Unifying receiver Port:USB|
        Compatible with:Windows XP, Windows Vista, Windows 7, Windows 8, Windows 10, Linux|Warranty: 3 Years|
        Package Contents: Wireless Keyboard K350, Wireless Mouse M510, User Documentation""",
        category=ProductCategory.ACCESSORY,
        original_price=219.00,
        discount_price=169.00,
        image='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1365/1689/mk550comfortwavekeyboardmicecombo03__65264.1520238120.jpg?c=2',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1365/1688/mk550comfortwavekeyboardmicecombo02__73466.1520238113.jpg?c=2',
        brand=logitech
    )
    logitech_product_4 = Product(
        name='Logitech M238 Wireless Mouse Doodle Collection- Skateburger',
        description="""Small and portable, making this the perfect mouse to pick-up-and-go
        Up to 12 months battery life with pre-installed battery
        Includes Nano receiver which allows connection up to 10m away
        Comes with a sheet of 15 premium stickers.""",
        specifications="""Serial Number:910-005060|Colour:cyan|Battery Life:12 months|
        Compatible with:Windows 10, Windows 8, Windows 7, Windows Vista, MacOS, Linux|Warranty: 1 Years|
        Package Contents: Wireless Mouse, User Documentation""",
        category=ProductCategory.ACCESSORY,
        original_price=28.99,
        discount_price=16.99,
        image='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1473/2605/m238skateburger01__95354.1549850619.jpg?c=2',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1473/2606/m238skateburger02__48494.1549850629.jpg?c=2',
        brand=logitech
    )

    logitech_product_5 = Product(
        name='Logitech G920 Racing Wheel Xbox One and PC',
        description="""Driving Force is designed for the latest Xbox One™ console racing game titles. 
        You may never race with a regular controller again after you experience G920 Driving Force.
        G920 Driving Force also works on PC with select titles using Logitech Gaming Software.
        DUAL-MOTOR FORCE FEEDBACK.""",
        specifications="""Software Support (at release): Logitech Gaming Software|
        Connection Type: USB|
        USB VID_PID: 046D_C262|
        USB Protocol: USB 2.0|
        USB Speed: Full Speed|
        Compatible with:Xbox One|Warranty: 2 Years Limited|
        Package Contents: Steering wheel, Pedals, Power adaptor, User documentation""",
        category=ProductCategory.ACCESSORY,
        original_price=499.00,
        discount_price=459.00,
        image='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/947/1408/g9202__82185.1515132500.jpg?c=2',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/947/1409/g9201__05457.1513585656.jpg?c=2',
        brand=logitech
    )

    logitech_product_6 = Product(
        name='Ultimate Ears Boom 3 - Unicorn',
        description="""Super-portable wireless Bluetoothspeaker: balanced 360° sound, deep bass,
        one-touch music control, water, dust & drop proof, and stunning high-performance fabric.
        It’s the ultimate go-anywhere speaker.""",
        specifications="""Serial Number: 984-001644|
        Maximum Sound Level: 90dBA|
        Frequency Range: 90Hz - 20kHz|
        Drivers: Two 2” drivers and two 2” x 4” Passive Radiators|
        WIRELESS CAPABILITIES: 8 Bluetooth enabled source devices - Connect up to two source devices at the same time|
        Warranty: 2 Years Limited""",
        category=ProductCategory.ACCESSORY,
        original_price=199.00,
        discount_price=159.00,
        image='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1524/2967/boom3unicorn01__00679.1576665292.jpg?c=2',
        image_2='https://cdn11.bigcommerce.com/s-e2161/images/stencil/608x608/products/1524/2976/boom3unicorn__79503.1576668757.jpg?c=2',
        brand=logitech
    )

    db.session.add_all([
        logitech_product_1, logitech_product_2, logitech_product_3, logitech_product_4, logitech_product_5,
        logitech_product_6, lenovo_product_1, lenovo_product_2, lenovo_product_3, lenovo_product_4, lenovo_product_5,
        apple_product_1, apple_product_2, apple_product_3, apple_product_4, apple_product_5,
        seagate_product_3, seagate_product_2, seagate_product_1,
        dell_product_1, dell_product_2, dell_product_3, dell_product_4, dell_product_5
    ])
    db.session.commit()
    return "SUCCESS"
