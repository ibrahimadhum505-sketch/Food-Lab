import os
import re

directory = r'c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab'
target_pattern = r'<a href="#" class="nav-link">Contacts</a>'
replacement = r'<a href="contacts.html" class="nav-link">Contacts</a>'

target_pattern_mob = r'<a href="#" class="mobile-nav-link">Contacts</a>'
replacement_mob = r'<a href="contacts.html" class="mobile-nav-link">Contacts</a>'

# For shop.html specifically which uses uppercase
target_pattern_shop = r'<a href="#" class="nav-link">CONTACTS</a>'
replacement_shop = r'<a href="contacts.html" class="nav-link">CONTACTS</a>'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(target_pattern, replacement)
        new_content = new_content.replace(target_pattern_mob, replacement_mob)
        new_content = new_content.replace(target_pattern_shop, replacement_shop)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
