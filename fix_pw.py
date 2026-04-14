with open(r'K:\AI_Test\zip\public\admin.html', 'rb') as f:
    content = f.read()

# The exact string with \r\n
old_line = b'<p style="color: var(--text-tertiary); margin-bottom: 2rem; font-size: 0.9rem;">\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xae\xbf\xe9\x97\xae\xe5\xaf\x86\xe7\xa0\x81 (\xe9\xbb\x98\xe8\xae\xa4 admin123)</p>\r\n'

# Replace with just asking for password without hint
new_line = b'<p style="color: var(--text-tertiary); margin-bottom: 2rem; font-size: 0.9rem;">\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe7\xAE\xa1\xe7\x90\x86\xe5\x91\x98\xe5\xaf\x86\xe7\xa0\x81</p>\r\n'

if old_line in content:
    content = content.replace(old_line, new_line)
    print('Replaced successfully')
else:
    print('Pattern not found')

with open(r'K:\AI_Test\zip\public\admin.html', 'wb') as f:
    f.write(content)
