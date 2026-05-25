import os
import re

sweets = [
    {"filename": "Chanar-Murki.html", "name": "Chanar Murki", "price": 250, "image": "https://i.imgur.com/YeCcuUw.png", "category": "Sweets & Desserts"},
    {"filename": "Shornomukhi.html", "name": "Shornomukhi", "price": 300, "image": "https://i.imgur.com/UgcfVUo.png", "category": "Sweets & Desserts"},
    {"filename": "Pera-Sandesh.html", "name": "Pera Sandesh", "price": 350, "image": "https://i.imgur.com/XyziBDl.png", "category": "Sweets & Desserts"},
    {"filename": "Dudhmon.html", "name": "Dudhmon", "price": 280, "image": "https://i.imgur.com/glh0jMk.png", "category": "Sweets & Desserts"},
    {"filename": "Lalmon.html", "name": "Lalmon", "price": 320, "image": "https://i.imgur.com/hHbo3eB.png", "category": "Sweets & Desserts"}
]

bakery = [
    {"filename": "Special-Jhal-Chanachur.html", "name": "Special Jhal Chanachur 250gm", "price": 150, "image": "https://i.imgur.com/vDeIccH.png", "category": "Bakery Delights"},
    {"filename": "Premium-Toast.html", "name": "Premium Toast  ( 500 gm )", "price": 180, "image": "https://i.imgur.com/WOe0tSw.png", "category": "Bakery Delights"},
    {"filename": "Classic-Toast.html", "name": "Classic Toast ( 500 gm )", "price": 160, "image": "https://i.imgur.com/Dl2cVNq.png", "category": "Bakery Delights"},
    {"filename": "Shanpapri.html", "name": "Shanpapri ( 500gm )", "price": 220, "image": "https://i.imgur.com/Cg2ojKv.png", "category": "Bakery Delights"},
    {"filename": "Chanachur.html", "name": "Chanachur 250gm", "price": 140, "image": "https://i.imgur.com/gJEM0HB.png", "category": "Bakery Delights"}
]

def generate_related_grid(items, exclude_name):
    html = '<div class="related-grid">\n'
    for item in items:
        if item["name"] == exclude_name:
            continue
        
        # Format the name for font-size adjustments if needed
        name_style = ""
        if len(item["name"]) > 20:
            name_style = ' style="font-size: 1.2rem;"'
        
        card = f'''                <div class="custom-card" onclick="window.location.href='{item["filename"]}'">
                    <div class="custom-card-body">
                        <img src="https://i.imgur.com/BSt2lzH.png" alt="Food Hustle Logo" class="custom-card-logo">
                        <div class="custom-card-img-wrapper">
                            <img src="{item["image"]}" alt="{item["name"]}" class="custom-card-img">
                        </div>
                        <div class="custom-card-name"{name_style}>{item["name"]}</div>
                    </div>
                    <div class="custom-card-footer">
                        <div class="custom-card-price">৳ {item["price"]}</div>
                        <div class="custom-card-cart-btn">
                            <svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="2"></circle><circle cx="20" cy="21" r="2"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                        </div>
                    </div>
                </div>\n'''
        html += card
    # Intentionally do not add '</div>' here because the lookahead preserves the original closing </div>
    return html.rstrip()

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"
with open(os.path.join(base_dir, "malai-doi.html"), "r", encoding="utf-8") as f:
    template = f.read()

def process_category(category_items):
    for item in category_items:
        content = template
        
        # Title
        content = re.sub(r'<title>Malai Doi - Food Lab</title>', f'<title>{item["name"]} - Food Lab</title>', content)
        
        # Image CSS
        old_css = r'''        .product-image-col .card-crop \{
            width: 340px;
            height: 300px;
            background-image: url\('https://i.imgur.com/WhsikT5.png'\);
            background-size: 105%;
            background-position: center 42%;
            background-repeat: no-repeat;
        \}'''
        new_css = f'''        .product-image-col .card-crop {{
            width: 355px;
            height: 319px;
            background-image: url('{item["image"]}');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
        }}'''
        content = re.sub(old_css, new_css, content)
        
        # Breadcrumbs
        content = re.sub(r'<span class="current">Malai Doi</span>', f'<span class="current">{item["name"]}</span>', content)
        
        # Product details
        content = re.sub(r'<h1 class="product-name">Malai Doi</h1>', f'<h1 class="product-name">{item["name"]}</h1>', content)
        content = re.sub(r'<div class="product-price">\s*<span class="taka-sign">৳</span> 400\s*</div>', f'<div class="product-price">\n                        <span class="taka-sign">৳</span> {item["price"]}\n                    </div>', content)
        
        # Category link
        content = re.sub(r'Category: <a href="index.html">Signature Yogurts</a>', f'Category: <a href="index.html">{item["category"]}</a>', content)
        
        # Reviews title
        content = re.sub(r'<div class="reviews-subtitle">Review our Malai Doi</div>', f'<div class="reviews-subtitle">Review our {item["name"]}</div>', content)
        
        # Related Grid
        related_html = generate_related_grid(category_items, item["name"])
        # We replace the content from <div class="related-grid"> down to but not including the first </div> that matches the closing tag sequence.
        content = re.sub(r'<div class="related-grid">.*?(?=            </div>\s*</div>\s*</div>\s*<script>)', related_html + '\n', content, flags=re.DOTALL)
        
        with open(os.path.join(base_dir, item["filename"]), "w", encoding="utf-8") as f:
            f.write(content)
        print(f'Created {item["filename"]}')

process_category(sweets)
process_category(bakery)

print("Fixed closing tags!")
