with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('// Videos')
if idx != -1:
    with open(r'K:\AI_Test\zip\videos_section.txt', 'w', encoding='utf-8') as out:
        out.write(content[idx:idx+800])
    print('Written to videos_section.txt')
else:
    print('Not found')
