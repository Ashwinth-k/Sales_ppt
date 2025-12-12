import os

base_path = "c:/Users/Dell/Desktop/Sales PPT"
# The string we added previously
old_style = 'style="position: absolute; top: 20px; left: 20px; width: 30px; height: 30px; z-index: 1000; object-fit: contain;"'
# The new string we want
new_style = 'style="position: absolute; top: 20px; right: 20px; width: 30px; height: 30px; z-index: 1000; object-fit: contain;"'

for i in range(2, 13):
    filename = f"slide{i}.html"
    filepath = os.path.join(base_path, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: File not found")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_style in content:
        new_content = content.replace(old_style, new_style)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    elif new_style in content:
        print(f"Skipping {filename}: Already updated")
    else:
        print(f"Warning: Logo style not found exactly as expected in {filename}")
