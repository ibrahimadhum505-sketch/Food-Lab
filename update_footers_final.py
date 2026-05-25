import os
import re

# Directory containing the HTML files
directory = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

# Content to insert
fa_link = '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n'

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

# Pattern to find the static image footer section
footer_pattern = r'<!-- Right: Elements Image -->\s*<div class="footer-right">.*?</div>'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Add Font Awesome link to <head> if missing
    if 'font-awesome' not in content:
        # Try to find style.css link as anchor
        if '<link rel="stylesheet" href="style.css">' in content:
            content = content.replace('<link rel="stylesheet" href="style.css">', 
                                     '<link rel="stylesheet" href="style.css">\n' + fa_link)
        # Fallback to other variants
        elif '<link rel="stylesheet" href="index.css">' in content:
            content = content.replace('<link rel="stylesheet" href="index.css">', 
                                     '<link rel="stylesheet" href="index.css">\n' + fa_link)
        elif '</head>' in content:
            content = content.replace('</head>', fa_link + '</head>')

    # 2. Replace static footer image with interactive footer
    if re.search(footer_pattern, content, flags=re.DOTALL):
        content = re.sub(footer_pattern, interactive_footer, content, flags=re.DOTALL)
    elif '<div class="footer-right">' in content and 'footer-elements-img' in content:
        # More aggressive fallback
        aggressive_pattern = r'<div class="footer-right">.*?</div>'
        content = re.sub(aggressive_pattern, interactive_footer, content, flags=re.DOTALL, count=1)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Iterate through all HTML files
count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "index.html":
        if update_file(os.path.join(directory, filename)):
            print(f"Updated: {filename}")
            count += 1

print(f"Total files updated: {count}")
