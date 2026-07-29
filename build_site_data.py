import os
import json
import re
import markdown

BASE_DIR = r"S:\B.Tech Data Science Notes"
DATA_FILE = os.path.join(BASE_DIR, "notes_data.js")

def parse_markdown_file(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
    pdf_rel_path = f"PDF_Notes/{rel_path[:-3]}.pdf"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)

    # Extract Title from first line or filename
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title = filename.replace('.md', '').replace('_', ' ')

    # Path decomposition
    parts = rel_path.split('/')
    semester = parts[0] if len(parts) > 0 and 'Semester' in parts[0] else "General"
    subject = parts[1] if len(parts) > 1 else "General"
    module = parts[2] if len(parts) > 2 else "General"

    # Extract Definition block
    def_match = re.search(r'>\s*📌\s*\*\*Definition to Remember\*\*\s*\n>\s*(.+?)(?=\n\n|\n>|\n---|\Z)', content, re.DOTALL)
    definition = def_match.group(1).replace('\n>', ' ').strip() if def_match else ""

    # Extract Must Write Points
    must_write_match = re.search(r'>\s*⭐\s*\*\*Must-Write Points[^\n]*\*\*\s*\n((?:>\s*.*?\n)+)', content)
    must_write = []
    if must_write_match:
        lines = must_write_match.group(1).split('\n')
        for line in lines:
            cleaned = re.sub(r'^>\s*\d+\.\s*', '', line).strip()
            if cleaned and not cleaned.startswith('>'):
                must_write.append(cleaned)

    # Extract Quick Recall
    quick_match = re.search(r'>\s*⚡\s*\*\*Quick Recall\*\*\s*\n>\s*`?(.+?)`?\s*(?=\n|\Z)', content)
    quick_recall = quick_match.group(1).strip() if quick_match else ""

    # Render HTML
    html = markdown.markdown(content, extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists'])

    return {
        "id": rel_path.replace('/', '-').replace('.md', ''),
        "relPath": rel_path,
        "pdfPath": check_pdf_exists(pdf_rel_path),
        "filename": filename,
        "semester": semester,
        "subject": subject,
        "module": module,
        "title": title,
        "content": content,
        "html": html,
        "definition": definition,
        "mustWrite": must_write,
        "quickRecall": quick_recall
    }

def check_pdf_exists(pdf_rel_path):
    full_pdf = os.path.join(BASE_DIR, pdf_rel_path.replace('/', '\\'))
    if os.path.exists(full_pdf):
        return pdf_rel_path
    return ""

def get_file_sort_key(item):
    filename = item['filename']
    
    # 1. Question Bank files come after topic notes (e.g. 2_Mark, 3_Mark, 5_Mark, 10_Mark)
    q_match = re.search(r'(\d+)\s*Mark', filename, re.IGNORECASE) or re.search(r'(\d+)_Mark', filename, re.IGNORECASE)
    if q_match:
        mark_num = int(q_match.group(1))
        return (item['semester'], item['subject'], item['module'], 1, mark_num, filename)

    # 2. Topic notes with letter-number prefixes (e.g. A1_, A2_, B1_, B2_)
    alpha_num_match = re.match(r'^([A-Za-z]+)(\d+)_', filename)
    if alpha_num_match:
        letter = alpha_num_match.group(1).upper()
        num = int(alpha_num_match.group(2))
        return (item['semester'], item['subject'], item['module'], 0, letter, num, filename)

    # 3. Topic notes with standard numeric prefixes (e.g. 1_, 2_, 10_, 12_)
    num_match = re.match(r'^(\d+)_', filename)
    if num_match:
        num = int(num_match.group(1))
        return (item['semester'], item['subject'], item['module'], 0, "", num, filename)

    return (item['semester'], item['subject'], item['module'], 2, "", 0, filename)

def main():
    items = []
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in dirs:
            dirs.remove('.git')
        if 'PDF_Notes' in dirs:
            dirs.remove('PDF_Notes')
        if '.github' in dirs:
            dirs.remove('.github')
            
        for file in files:
            if file.endswith('.md') and not file.lower().startswith('readme'):
                full_path = os.path.join(root, file)
                items.append(parse_markdown_file(full_path))

    # Sort items strictly by numerical curriculum sequence
    items.sort(key=get_file_sort_key)

    js_code = "window.NOTES_DATA = " + json.dumps(items, indent=2, ensure_ascii=False) + ";"
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    print(f"Successfully indexed {len(items)} notes files across all semesters in strict numerical sequence into notes_data.js")

if __name__ == "__main__":
    main()
