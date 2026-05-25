import os
import re

css_content = """
        /* ========== CART NOTIFICATION ========== */
        .cart-notification {
            position: fixed;
            top: -100px;
            right: 30px;
            background-color: #4b4b4b;
            border-radius: 12px;
            padding: 15px 50px 15px 25px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            z-index: 10000;
            opacity: 0;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }
        @keyframes popDownDesktop {
            0% { top: -100px; opacity: 0; }
            50% { opacity: 0.7; }
            100% { top: 25px; opacity: 1; }
        }
        @keyframes popDownMobile {
            0% { top: -100px; opacity: 0; }
            50% { opacity: 0.7; }
            100% { top: 60px; opacity: 1; }
        }
        .cart-notification.show {
            animation: popDownDesktop 0.4s forwards;
        }
        .cart-notification-content {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        .cart-notification-text {
            color: #fff;
            font-family: 'Lato', sans-serif;
            font-size: 1.1rem;
            font-weight: 400;
            white-space: nowrap;
        }
        .cart-notification-view-cart {
            background-color: #fff;
            color: #2a9d42;
            border: none;
            border-radius: 20px;
            padding: 6px 16px;
            font-family: 'Lato', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
        }
        .cart-notification-view-cart:hover {
            transform: scale(1.05);
            opacity: 0.9;
        }
        .cart-notification-close {
            position: absolute;
            top: -12px;
            right: -12px;
            background: none;
            border: none;
            cursor: pointer;
            padding: 0;
            transition: transform 0.2s;
            width: 34px;
            height: 34px;
        }
        .cart-notification-close:hover {
            transform: scale(1.15);
        }
        @media (max-width: 768px) {
            .cart-notification {
                right: 0;
                left: 0;
                border-radius: 0;
                width: 100%;
                padding: 15px 20px;
                top: -100px;
            }
            .cart-notification.show {
                animation: popDownMobile 0.4s forwards;
            }
            .cart-notification-close {
                top: 8px;
                right: 10px;
            }
            .cart-notification-text {
                font-size: 0.95rem;
            }
            .cart-notification-view-cart {
                padding: 6px 12px;
                font-size: 0.9rem;
            }
        }
"""

html_js_content = """
    <!-- Add to Cart Notification -->
    <div id="cart-notification" class="cart-notification">
        <div class="cart-notification-content">
            <span class="cart-notification-text" id="cart-notification-text">• 1X Product Added to your Cart</span>
            <button class="cart-notification-view-cart">View Cart</button>
        </div>
        <button class="cart-notification-close" id="cart-notification-close" aria-label="Close">
            <svg width="100%" height="100%" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <filter id="crumpled-paper">
                        <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="5" result="noise" />
                        <feDiffuseLighting in="noise" lighting-color="#fff" surfaceScale="2" result="light">
                            <feDistantLight azimuth="45" elevation="60" />
                        </feDiffuseLighting>
                        <feBlend mode="multiply" in="SourceGraphic" in2="light" />
                    </filter>
                    <filter id="brush-stroke-black">
                        <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" result="noise" />
                        <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" xChannelSelector="R" yChannelSelector="G" />
                    </filter>
                </defs>
                <path d="M10 10 L90 5 L95 90 L5 95 Z" fill="#f4f4f4" filter="url(#crumpled-paper)" />
                <path d="M25 25 C 35 30, 65 70, 75 75 M75 25 C 65 30, 35 70, 25 75" stroke="#111" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" style="filter: url(#brush-stroke-black);" />
            </svg>
        </button>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const notification = document.getElementById('cart-notification');
            const notifText = document.getElementById('cart-notification-text');
            const closeBtn = document.getElementById('cart-notification-close');
            let hideTimeout;

            function showNotification(productName, qty) {
                notifText.innerText = `• ${qty}X ${productName} Added to your Cart`;
                
                // Reset animation by triggering reflow
                notification.classList.remove('show');
                void notification.offsetWidth;
                notification.classList.add('show');
                
                clearTimeout(hideTimeout);
                hideTimeout = setTimeout(() => {
                    notification.classList.remove('show');
                }, 2000);
            }

            if (closeBtn) {
                closeBtn.addEventListener('click', () => {
                    notification.classList.remove('show');
                    clearTimeout(hideTimeout);
                });
            }

            // Main Product page Add to Cart
            const mainAddBtn = document.getElementById('addToCartBtn');
            if (mainAddBtn) {
                mainAddBtn.addEventListener('click', () => {
                    const qtyInput = document.getElementById('qtyVal');
                    const qty = qtyInput ? qtyInput.value : 1;
                    const nameEl = document.querySelector('.product-name');
                    const name = nameEl ? nameEl.innerText.trim() : 'Product';
                    showNotification(name, qty);
                });
            }

            // Category/Related product cards Add to Cart
            const cardAddBtns = document.querySelectorAll('.custom-card-cart-btn');
            cardAddBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation(); // prevent card click navigation
                    const card = btn.closest('.custom-card');
                    const nameEl = card ? card.querySelector('.custom-card-name') : null;
                    const name = nameEl ? nameEl.innerText.trim() : 'Product';
                    showNotification(name, 1);
                });
            });
        });
    </script>
"""

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

# 1. Update style.css
style_css_path = os.path.join(base_dir, "style.css")
if os.path.exists(style_css_path):
    with open(style_css_path, "r", encoding="utf-8") as f:
        content = f.read()
    if ".cart-notification" not in content:
        with open(style_css_path, "a", encoding="utf-8") as f:
            f.write(css_content)
        print("Updated style.css")

# 2. Update all .html files
for file in os.listdir(base_dir):
    if file.endswith(".html"):
        filepath = os.path.join(base_dir, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated = False
        
        # Inject CSS
        if "</style>" in content and ".cart-notification" not in content:
            content = content.replace("</style>", css_content + "\n</style>")
            updated = True
            
        # Inject HTML/JS
        if "</body>" in content and 'id="cart-notification"' not in content:
            content = content.replace("</body>", html_js_content + "\n</body>")
            updated = True
            
        if updated:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file}")

print("Injection complete!")
