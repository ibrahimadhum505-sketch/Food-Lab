import os

# Absolute path to the Food Lab directory
directory = r'c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab'

replacements = [
    ('<a href="#" class="nav-link">Contacts</a>', '<a href="contacts.html" class="nav-link">Contacts</a>'),
    ('<a href="#" class="mobile-nav-link">Contacts</a>', '<a href="contacts.html" class="mobile-nav-link">Contacts</a>'),
    ('<a href="#" class="nav-link">About Us</a>', '<a href="about.html" class="nav-link">About Us</a>'),
    ('<a href="#" class="mobile-nav-link">About Us</a>', '<a href="about.html" class="mobile-nav-link">About Us</a>'),
    # Case variants
    ('<a href="#" class="nav-link">CONTACTS</a>', '<a href="contacts.html" class="nav-link">CONTACTS</a>'),
]

files_updated = 0

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements:
                new_content = new_content.replace(old, new)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f'Updated: {filename}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

print(f'Done. Total files updated: {files_updated}')
