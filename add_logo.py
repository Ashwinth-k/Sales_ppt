import os
import re

base_path = "c:/Users/Dell/Desktop/Sales PPT"
logo_html = '<img src="logo.png" alt="Logo" style="position: absolute; top: 20px; left: 20px; width: 30px; height: 30px; z-index: 1000; object-fit: contain;">'

for i in range(2, 13):
    filename = f"slide{i}.html"
    filepath = os.path.join(base_path, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: File not found")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if logo already exists in this position to avoid duplicates
    if 'style="position: absolute; top: 20px; left: 20px;' in content:
        print(f"Skipping {filename}: Logo likely already present")
        continue

    # Insert logo after <div class="slide-container">
    # We use regex to handle potential attributes in the div tag if any, though usually it's just class="slide-container"
    pattern = re.compile(r'(<div\s+class=["\']slide-container["\']\s*>)')
    
    if pattern.search(content):
        new_content = pattern.sub(r'\1\n        ' + logo_html, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Warning: Could not find slide-container in {filename}")
