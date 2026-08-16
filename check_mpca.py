import json

with open('notes_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_text = text.replace('window.NOTES_DATA = ', '').strip().rstrip(';')
data = json.loads(json_text)

mpca_notes = [d for d in data if d['subject'] == 'MPCA' and d['module'] != 'Question & Answers Bank']
mpca_qa = [d for d in data if d['subject'] == 'MPCA' and d['module'] == 'Question & Answers Bank']

print(f"Total MPCA Notes (Lecture Notes): {len(mpca_notes)}")
for d in mpca_notes:
    print(f"  [{d['module']}] {d['filename']} -> {d['title']}")

print(f"\nTotal MPCA QA (Question Banks): {len(mpca_qa)}")
for d in mpca_qa:
    print(f"  [{d['relPath']}] -> {d['title']}")
