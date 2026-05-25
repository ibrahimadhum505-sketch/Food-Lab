import os
import re

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

# 1. Update style.css
style_css_path = os.path.join(base_dir, "style.css")
new_css = """
        /* ========== CART PAGE ========== */
        .cart-page-wrapper {
            background-color: #fff;
            border-radius: 20px;
            max-width: 1100px;
            margin: 40px auto;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            display: grid;
            grid-template-columns: 1fr 350px;
            gap: 40px;
            position: relative;
        }
        .cart-page-close {
            position: absolute;
            top: 20px;
            right: 20px;
            background: none;
            border: none;
            cursor: pointer;
            transition: transform 0.2s;
            width: 40px;
            height: 40px;
        }
        .cart-page-close:hover {
            transform: scale(1.1);
        }
        .cart-page-left {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .cart-page-right {
            border-left: 2px dashed #333;
            padding-left: 40px;
            display: flex;
            flex-direction: column;
        }
        .cart-headers {
            display: grid;
            grid-template-columns: 3fr 1fr 1fr;
            align-items: center;
            border-bottom: 1px dashed #333;
            padding-bottom: 10px;
            font-family: 'Copperplate Gothic Bold', Copperplate, serif;
            font-size: 1.1rem;
            text-transform: uppercase;
        }
        .cart-item {
            display: grid;
            grid-template-columns: 3fr 1fr 1fr;
            align-items: center;
            border-bottom: 1px dashed #333;
            padding: 15px 0;
            font-family: 'Caveat', 'Student', cursive;
            font-size: 1.5rem;
        }
        .cart-item-product {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        .cart-item-img-wrap {
            position: relative;
        }
        .cart-item-logo {
            position: absolute;
            top: -15px;
            left: 0;
            width: 40px;
        }
        .cart-item-img {
            width: 80px;
            height: 80px;
            object-fit: cover;
            border-radius: 50%;
            background: #f9f9f9;
        }
        .cart-item-details {
            display: flex;
            flex-direction: column;
        }
        .cart-item-price {
            font-size: 1.4rem;
        }
        .cart-qty-control {
            display: flex;
            align-items: center;
            border: 1px solid #333;
            border-radius: 20px;
            padding: 2px 10px;
            width: fit-content;
        }
        .cart-qty-btn {
            background: none;
            border: none;
            font-size: 1.2rem;
            cursor: pointer;
            padding: 0 5px;
        }
        .cart-qty-val {
            margin: 0 10px;
            font-family: 'Caveat', 'Student', cursive;
            font-size: 1.5rem;
        }
        .cart-subtotal-val {
            font-size: 1.6rem;
            text-align: left;
        }
        .cart-summary-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Caveat', 'Student', cursive;
            font-size: 2rem;
            margin-bottom: 20px;
            border-bottom: 1px dashed #333;
            padding-bottom: 10px;
        }
        .cart-summary-ship {
            display: flex;
            flex-direction: column;
            gap: 10px;
            font-family: 'Caveat', 'Student', cursive;
            font-size: 1.6rem;
            border-bottom: 1px dashed #333;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        .cart-ship-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #000;
        }
        .cart-ship-label {
            color: #ff3b30;
            font-size: 1.8rem;
        }
        .cart-summary-total {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Caveat', 'Student', cursive;
            font-size: 2.5rem;
            color: #ff3b30;
            margin-bottom: 30px;
        }
        .cart-checkout-btn {
            background-color: #ffb6c1;
            color: #fff;
            border: none;
            border-radius: 30px;
            padding: 15px 0;
            font-family: 'Copperplate Gothic Bold', Copperplate, serif;
            font-size: 1.5rem;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            transition: opacity 0.2s;
            width: 100%;
            display: block;
        }
        .cart-checkout-btn:hover {
            opacity: 0.9;
        }
        @media (max-width: 768px) {
            .cart-page-wrapper {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px;
                margin: 20px;
            }
            .cart-page-right {
                border-left: none;
                border-top: 2px dashed #333;
                padding-left: 0;
                padding-top: 30px;
            }
            .cart-headers {
                display: none;
            }
            .cart-item {
                grid-template-columns: 1fr;
                gap: 15px;
            }
            .cart-item-product {
                flex-direction: row;
            }
            .cart-subtotal-val {
                text-align: right;
            }
        }
"""
if os.path.exists(style_css_path):
    with open(style_css_path, "r", encoding="utf-8") as f:
        style_content = f.read()
    if ".cart-page-wrapper" not in style_content:
        with open(style_css_path, "a", encoding="utf-8") as f:
            f.write(new_css)
        print("Updated style.css")

old_script_snippet = r"""    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const notification = document.getElementById('cart-notification');"""

new_script = """    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const notification = document.getElementById('cart-notification');
            const notifText = document.getElementById('cart-notification-text');
            const closeBtn = document.getElementById('cart-notification-close');
            let hideTimeout;

            function showNotification(productName, qty) {
                notifText.innerText = `• ${qty}X ${productName} Added to your Cart`;
                notification.classList.remove('show');
                void notification.offsetWidth;
                notification.classList.add('show');
                clearTimeout(hideTimeout);
                hideTimeout = setTimeout(() => { notification.classList.remove('show'); }, 2000);
            }

            if (closeBtn) {
                closeBtn.addEventListener('click', () => { notification.classList.remove('show'); clearTimeout(hideTimeout); });
            }

            const mainAddBtn = document.getElementById('addToCartBtn');
            if (mainAddBtn) {
                mainAddBtn.addEventListener('click', () => {
                    const qtyInput = document.getElementById('qtyVal');
                    const qty = qtyInput ? parseInt(qtyInput.value) : 1;
                    const nameEl = document.querySelector('.product-name');
                    const name = nameEl ? nameEl.innerText.trim() : 'Product';
                    const priceEl = document.querySelector('.product-price');
                    let price = 0;
                    if(priceEl) price = parseInt(priceEl.innerText.replace(/[^0-9]/g, ''));
                    const imgEl = document.querySelector('.card-crop');
                    let image = 'https://i.imgur.com/BSt2lzH.png';
                    if (imgEl && window.getComputedStyle(imgEl).backgroundImage !== 'none') {
                        image = window.getComputedStyle(imgEl).backgroundImage.slice(4, -1).replace(/"/g, "");
                    }
                    if (typeof addToCart === 'function') { addToCart({ name, price, qty, image }); }
                    showNotification(name, qty);
                });
            }

            const cardAddBtns = document.querySelectorAll('.custom-card-cart-btn');
            cardAddBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const card = btn.closest('.custom-card');
                    const nameEl = card ? card.querySelector('.custom-card-name') : null;
                    const name = nameEl ? nameEl.innerText.trim() : 'Product';
                    const priceEl = card ? card.querySelector('.custom-card-price') : null;
                    let price = 0;
                    if(priceEl) price = parseInt(priceEl.innerText.replace(/[^0-9]/g, ''));
                    const imgEl = card ? card.querySelector('.custom-card-img') : null;
                    let image = 'https://i.imgur.com/BSt2lzH.png';
                    if (imgEl && imgEl.src) image = imgEl.src;
                    if (typeof addToCart === 'function') { addToCart({ name, price, qty: 1, image }); }
                    showNotification(name, 1);
                });
            });

            const viewCartBtn = document.querySelector('.cart-notification-view-cart');
            if(viewCartBtn) {
                viewCartBtn.addEventListener('click', () => { window.location.href = 'cart.html'; });
            }
        });
    </script>"""

new_cart_icon = """<a href="cart.html" style="position:relative; display:inline-block;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24">
                        <circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                    </svg>
                    <span class="cart-badge" style="display:none; position:absolute; top:-8px; right:-10px; background:#fff; color:#2a9d42; font-size:12px; font-family:sans-serif; font-weight:bold; width:20px; height:20px; border-radius:50%; align-items:center; justify-content:center; box-shadow:0 2px 4px rgba(0,0,0,0.2);">0</span>
                </a>"""

for file in os.listdir(base_dir):
    if file.endswith(".html") and file != "cart.html":
        filepath = os.path.join(base_dir, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        updated = False
        
        # 1. Update Cart SVG
        pattern = r'<a href="checkout\.html">\s*<svg[^>]*>.*?<\/svg>\s*<\/a>'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_cart_icon, content, flags=re.DOTALL)
            updated = True
            
        # 2. Update Mobile Link
        pattern2 = r'<a href="#" class="mobile-nav-link">Cart<\/a>'
        if re.search(pattern2, content):
            content = re.sub(pattern2, r'<a href="cart.html" class="mobile-nav-link">Cart</a>', content)
            updated = True
            
        # 3. Add cart.js script tag before </body>
        if "cart.js" not in content and "</body>" in content:
            content = content.replace("</body>", '<script src="cart.js"></script>\n</body>')
            updated = True
            
        # 4. Replace old notification script with new one
        if "document.getElementById('cart-notification');" in content and "addToCart({" not in content:
            # We use regex to find the old script block
            script_pattern = r'<script>\s*document\.addEventListener\("DOMContentLoaded", function\(\) \{\s*const notification = document\.getElementById\(\'cart-notification\'\);.*?</script>'
            content = re.sub(script_pattern, new_script, content, flags=re.DOTALL)
            updated = True

        if updated:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file}")

print("Injection complete!")
