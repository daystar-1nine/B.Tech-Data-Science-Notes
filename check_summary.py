import json

with open('notes_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_text = text.replace('window.NOTES_DATA = ', '').strip().rstrip(';')
data = json.loads(json_text)

print(f"Total entries in database: {len(data)}")
subs = {}
for d in data:
    s = d['subject']
    ct = d['contentType']
    subs.setdefault(s, {'notes': 0, 'qa': 0})[ct] += 1

for s, counts in sorted(subs.items()):
    print(f"  {s}: {counts['notes']} Lecture Notes + {counts['qa']} Q&A Banks (Total = {counts['notes'] + counts['qa']})")
