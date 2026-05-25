import os

# The Font Awesome link to be added to the <head>
fa_link = '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n'

# The interactive HTML footer to be inserted
interactive_footer = """                <!-- Right: Business Info & Newsletter -->
                <div class="footer-right">
                    <!-- Newsletter Form -->
                    <div class="footer-newsletter">
                        <div class="newsletter-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00c853"
                                stroke-width="2">
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                                <polyline points="22,6 12,13 2,6" />
                            </svg>
                        </div>
                        <input type="email" class="newsletter-input" placeholder="Your Email">
                        <button class="newsletter-btn">Subscribe</button>
                    </div>

                    <!-- Social Media Links -->
                    <div class="footer-social-links">
                        <a href="https://facebook.com" class="social-icon-link" target="_blank">
                            <i class="fa-brands fa-facebook" style="color: rgb(69, 12, 233);"></i>
                        </a>
                        <a href="https://twitter.com" class="social-icon-link" target="_blank">
                            <i class="fa-brands fa-square-x-twitter" style="color: rgb(6, 12, 16);"></i>
                        </a>
                        <a href="https://whatsapp.com" class="social-icon-link" target="_blank">
                            <i class="fa-brands fa-square-whatsapp" style="color: hsl(136, 74%, 52%);"></i>
                        </a>
                    </div>

                    <!-- Payment Accept Section -->
                    <div class="footer-payment-section">
                        <h3 class="payment-title">Payment Accept</h3>
                        <div class="payment-logos">
                            <img src="https://i.imgur.com/78kr3Ek.png" alt="bKash" class="payment-logo-img">
                            <img src="https://i.imgur.com/i3sv8EW.png" alt="Rocket" class="payment-logo-img">
                            <img src="https://i.imgur.com/YyPMeYi.png" alt="Nagad" class="payment-logo-img">
                        </div>
                    </div>
                </div>"""

# The target image section to be replaced
target_footer_image = """            <!-- Right: Elements Image -->
            <div class="footer-right">
                <img src="https://i.imgur.com/LGkQxgX.png" alt="Footer Elements" class="footer-elements-img">
            </div>"""

directory = r"c:\\Users\\DELL\\OneDrive\\Desktop\\Ibrahim A\\Food Lab"

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "index.html":
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add Font Awesome link if not present
        if 'font-awesome' not in content:
            content = content.replace('<link rel="stylesheet" href="style.css">', 
                                     '<link rel="stylesheet" href="style.css">\n' + fa_link)
        
        # Replace static footer image with interactive footer
        if target_footer_image in content:
            new_content = content.replace(target_footer_image, interactive_footer)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filename}")
        else:
            # Fallback for slight variations in spacing
            if '<div class="footer-right">' in content and 'footer-elements-img' in content:
                print(f"Found partial match in {filename}, attempting more flexible replacement...")
                import re
                flexible_pattern = r'<!-- Right: Elements Image -->\s*<div class="footer-right">.*?</div>'
                new_content = re.sub(flexible_pattern, interactive_footer, content, flags=re.DOTALL)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated (flexible): {filename}")
            else:
                print(f"Skipped: {filename} (Footer image container not found)")
