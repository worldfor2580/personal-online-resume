with open(r'K:\AI_Test\zip\public\admin.html', 'rb') as f:
    content = f.read()
content = content.replace(b"const ADMIN_PASSWORD = 'admin123';", b"const ADMIN_PASSWORD = 'Li@2026Chance';")
with open(r'K:\AI_Test\zip\public\admin.html', 'wb') as f:
    f.write(content)
print('done')
