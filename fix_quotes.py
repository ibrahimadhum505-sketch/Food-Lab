base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

with open(base_dir + r"\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix escaped quotes: onclick="window.location.href=\'filename\'" -> onclick="window.location.href='filename'"
import re
content = re.sub(r"window\.location\.href=\\'([^']+)\\'", r"window.location.href='\1'", content)

with open(base_dir + r"\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed escaped quotes in index.html!")

# Count how many onclick handlers were fixed
count = len(re.findall(r"window\.location\.href='[^']+'", content))
print(f"Total onclick handlers now: {count}")
