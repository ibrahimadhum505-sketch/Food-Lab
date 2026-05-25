import os

def update_shop_links():
    root_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"
    for filename in os.listdir(root_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(root_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update desktop nav links
            new_content = content.replace('<a href="index.html" class="nav-link">Shop</a>', '<a href="shop.html" class="nav-link">Shop</a>')
            new_content = new_content.replace('<a href="index.html" class="nav-link">SHOP</a>', '<a href="shop.html" class="nav-link">SHOP</a>')
            
            # Update mobile sidebar links
            new_content = new_content.replace('<a href="index.html" class="mobile-nav-link">Shop</a>', '<a href="shop.html" class="mobile-nav-link">Shop</a>')
            new_content = new_content.replace('<a href="index.html" class="mobile-nav-link">SHOP</a>', '<a href="shop.html" class="mobile-nav-link">SHOP</a>')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

if __name__ == "__main__":
    update_shop_links()
