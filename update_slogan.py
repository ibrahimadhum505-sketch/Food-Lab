import os
import re

# Directory containing the files
directory = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

replacement_html = '''<div class="slogan-wrapper">
                        <div class="slogan slogan-text-container" id="food-lab-slogan">
                            <span class="slogan-part-1">GET A NEW EXPERIENCE OF</span>
                            <span class="slogan-part-2">
                                <span class="stagger-letter high">T</span>
                                <span class="stagger-letter low">A</span>
                                <span class="stagger-letter high">S</span>
                                <span class="stagger-letter low">T</span>
                            </span>
                        </div>
                    </div>'''

# Update all HTML files
html_count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the slogan is in the file
        if 'id="food-lab-slogan"' in content and '<div class="slogan-wrapper">' in content:
            new_content = re.sub(
                r'<div class="slogan-wrapper">.*?id="food-lab-slogan".*?</div>',
                replacement_html,
                content,
                flags=re.DOTALL
            )
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated HTML: {filename}")
                html_count += 1

# Update style.css
css_path = os.path.join(directory, "style.css")
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 1. Add Google Font @import
    css_import = "@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap');\n"
    if "Cormorant+Garamond" not in css_content:
        css_content = css_import + css_content
        print("Added Google Font import to style.css")
        
    # 2. Append Custom Styles
    css_styles = """
/* ========== CSS SLOGAN TAGLINE STYLING ========== */
.slogan-text-container {
    width: auto !important;
    height: auto !important;
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    text-transform: uppercase;
    color: #ff5722;
    -webkit-text-stroke: 1px #800c0c;
    text-stroke: 1px #800c0c;
    font-size: clamp(14px, 1.65vw, 24px);
    letter-spacing: 0.08em;
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    text-shadow: 1px 1px 0px #800c0c;
    line-height: 1.2;
    margin-top: 4px;
}

.slogan-part-1 {
    display: inline-block;
    margin-right: 0.35em;
}

.slogan-part-2 {
    display: inline-flex;
    gap: 0.25em;
}

.stagger-letter {
    display: inline-block;
    will-change: transform;
}

.stagger-letter.high {
    transform: translateY(-0.18em);
}

.stagger-letter.low {
    transform: translateY(0.18em);
}

@media (max-width: 768px) {
    .slogan-text-container {
        font-size: clamp(10px, 2.8vw, 12px) !important;
        letter-spacing: 0.05em !important;
        margin-top: 8px !important;
    }
    
    .slogan-part-2 {
        gap: 0.18em !important;
    }
    
    .header-center {
        margin-top: 4px;
    }
}
"""
    if ".slogan-text-container" not in css_content:
        css_content += css_styles
        print("Appended custom CSS tagline styles to style.css")
        
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

print(f"Update complete! Total HTML files updated: {html_count}")
