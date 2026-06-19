#!/usr/bin/env python3
import os
old = 'http://example.com'
new = 'https://studynavi.co.kr'
changed = []

for root, dirs, files in os.walk('.'):
    for fn in files:
        lower = fn.lower()
        path = os.path.join(root, fn)
        if lower in ('robots.txt','sitemap.xml') or lower.endswith(('.html','.htm')):
            try:
                with open(path, 'rb') as f:
                    data = f.read()
            except Exception:
                continue
            try:
                s = data.decode('utf-8')
            except Exception:
                try:
                    s = data.decode('cp949')
                except Exception:
                    s = data.decode('utf-8', errors='ignore')
            if old in s:
                s2 = s.replace(old, new)
                try:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(s2)
                    changed.append(path.replace('\\','/'))
                except Exception as e:
                    print('WRITE ERROR', path, e)

print('CHANGED_COUNT:', len(changed))
for p in changed:
    print(p)
