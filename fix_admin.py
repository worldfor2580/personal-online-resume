with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('href="/" ', 'href="/personal-online-resume/" ')
with open(r'K:\AI_Test\zip\public\admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
