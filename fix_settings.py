#!/usr/bin/env python3
import re

path = '/var/www/katokz/core/settings.py'

with open(path, 'r') as f:
    content = f.read()

# Fix CSRF_TRUSTED_ORIGINS
old = '''CSRF_TRUSTED_ORIGINS = [
    "https://katokz.kz",
    "https://www.katokz.kz",
    "https://kato-web-665424752344.europe-west1.run.app"
]'''

new = '''CSRF_TRUSTED_ORIGINS = [
    "https://katokz.kz",
    "https://www.katokz.kz",
    "http://katokz.kz",
    "http://www.katokz.kz",
    "http://89.35.125.232",
]'''

if old in content:
    content = content.replace(old, new)
    print("CSRF_TRUSTED_ORIGINS updated")
else:
    # Try to find partial match and replace
    pattern = r'CSRF_TRUSTED_ORIGINS\s*=\s*\[.*?\]'
    replacement = new
    content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count:
        print(f"CSRF_TRUSTED_ORIGINS replaced via regex ({count} occurrences)")
    else:
        print("WARNING: CSRF_TRUSTED_ORIGINS not found!")

# Fix ALLOWED_HOSTS to add VPS IP
old_hosts = 'ALLOWED_HOSTS = ["katokz.kz", "www.katokz.kz", "kato-web-665424752344.europe-west1.run.app", "localhost", "127.0.0.1"]'
new_hosts = 'ALLOWED_HOSTS = ["katokz.kz", "www.katokz.kz", "89.35.125.232", "localhost", "127.0.0.1"]'

if old_hosts in content:
    content = content.replace(old_hosts, new_hosts)
    print("ALLOWED_HOSTS updated")
else:
    print("ALLOWED_HOSTS already correct or not found")

with open(path, 'w') as f:
    f.write(content)

print("Done. Verifying...")
with open(path, 'r') as f:
    for i, line in enumerate(f, 1):
        if 'CSRF_TRUSTED' in line or 'ALLOWED_HOSTS' in line or '89.35' in line or 'http://' in line:
            print(f"  {i}: {line.rstrip()}")
