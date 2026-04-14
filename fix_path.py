import re

# Fix index.html
with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("fetch('/personal-online-resume/data.json", "fetch('/personal-online-resume/data.json")
# Already fixed from previous step

# Fix public/admin.html
with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("fetch('/data.json'", "fetch('/personal-online-resume/data.json'")
with open(r'K:\AI_Test\zip\public\admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
