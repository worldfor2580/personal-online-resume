import re

# Check index.html
with open(r'K:\AI_Test\zip\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'href=' in line and ('="/' in line or "='/'" in line):
            print('index Line ' + str(i) + ': ' + line.rstrip())

# Check admin.html
with open(r'K:\AI_Test\zip\public\admin.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'href=' in line and ('="/' in line or "='/'" in line):
            print('admin Line ' + str(i) + ': ' + line.rstrip())
