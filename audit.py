import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab"

all_files = {
    "malai-doi.html":      {"name": "Malai Doi",        "category": "Signature Yogurts"},
    "Premium-doi.html":    {"name": "Premium doi",       "category": "Signature Yogurts"},
    "Cup-malai-doi.html":  {"name": "Cup Malai doi",     "category": "Signature Yogurts"},
    "Cup-doi.html":        {"name": "Cup doi",           "category": "Signature Yogurts"},
    "Sada-doi.html":       {"name": "Sada doi",          "category": "Signature Yogurts"},
    "Lachcha-Semai-200gm.html":   {"name": "Lachcha Semai 200gm (Ghee fry)", "category": "Semai Symphony"},
    "Vermicelli-Semai.html":      {"name": "Vermicelli Semai",                "category": "Semai Symphony"},
    "Lachcha-Semai-300gm-Box.html":{"name": "Lachcha Semai 300gm Box",       "category": "Semai Symphony"},
    "Bhaja-Semai.html":           {"name": "Bhaja Semai",                     "category": "Semai Symphony"},
    "Lachcha-Semai-white.html":   {"name": "Lachcha Semai white",             "category": "Semai Symphony"},
    "Chanar-Murki.html":  {"name": "Chanar Murki",  "category": "Sweets & Desserts"},
    "Shornomukhi.html":   {"name": "Shornomukhi",   "category": "Sweets & Desserts"},
    "Pera-Sandesh.html":  {"name": "Pera Sandesh",  "category": "Sweets & Desserts"},
    "Dudhmon.html":       {"name": "Dudhmon",        "category": "Sweets & Desserts"},
    "Lalmon.html":        {"name": "Lalmon",         "category": "Sweets & Desserts"},
    "Special-Jhal-Chanachur.html": {"name": "Special Jhal Chanachur 250gm", "category": "Bakery Delights"},
    "Premium-Toast.html":  {"name": "Premium Toast  ( 500 gm )", "category": "Bakery Delights"},
    "Classic-Toast.html":  {"name": "Classic Toast ( 500 gm )",  "category": "Bakery Delights"},
    "Shanpapri.html":      {"name": "Shanpapri ( 500gm )",       "category": "Bakery Delights"},
    "Chanachur.html":      {"name": "Chanachur 250gm",           "category": "Bakery Delights"},
}

errors = []
ok = []

for filename, info in all_files.items():
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        errors.append(f"MISSING: {filename}")
        continue
    size = os.path.getsize(path)
    if size < 1000:
        errors.append(f"EMPTY ({size}B): {filename}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    issues = []
    if info["name"] not in content:
        issues.append(f"name missing")
    if info["category"] not in content:
        issues.append(f"category missing")
    if info["category"] != "Signature Yogurts":
        if "355px" not in content or "319px" not in content:
            issues.append("image size 355x319 missing")
    links = re.findall(r"onclick=\"window\.location\.href='([^']+)'\"", content)
    html_links = [l for l in links if l.endswith('.html')]
    if issues:
        errors.append(f"ISSUES in {filename}: {'; '.join(issues)}")
    else:
        ok.append(f"OK ({size//1024}KB, {len(html_links)} onclick): {filename}")

print("PASSING:")
for line in ok:
    print(f"  + {line}")
print(f"\nERRORS ({len(errors)}):")
if errors:
    for line in errors:
        print(f"  ! {line}")
else:
    print("  None! All files are good.")
print(f"\nResult: {len(ok)}/{len(all_files)} files passing")
