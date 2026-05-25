import os
import re

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

badge_html = """
                    <span class="cart-badge" style="display:none; position:absolute; top:-8px; right:-10px; background:#fff; color:#2a9d42; font-size:16px; font-family:'Canva Student Font', 'Caveat', cursive; font-weight:bold; width:22px; height:22px; border-radius:50%; align-items:center; justify-content:center; box-shadow:0 2px 4px rgba(0,0,0,0.2);">0</span>
"""

# Pattern to find the Cart icon block
pattern = r'(<!-- Shopping Cart -->\s*<a href=")(#[^"]*)(" class="header-icon-btn" aria-label="Cart">)(\s*<svg.*?</svg>\s*)(</a>)'

for file in os.listdir(base_dir):
    if file.endswith(".html") and file != "cart.html":
        filepath = os.path.join(base_dir, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        updated = False
        
        # We need to change href="#" to href="cart.html" and add style="position:relative" to the <a>
        # and insert the badge_html before </a>
        
        def replace_func(match):
            return match.group(1) + "cart.html" + '" class="header-icon-btn" aria-label="Cart" style="position:relative; display:inline-block;">' + match.group(4) + badge_html + match.group(5)
            
        new_content, count = re.subn(pattern, replace_func, content, flags=re.DOTALL)
        
        if count > 0 and 'class="cart-badge"' not in content:
            updated = True
            content = new_content
            
        if updated:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file}")

print("Fix complete!")
