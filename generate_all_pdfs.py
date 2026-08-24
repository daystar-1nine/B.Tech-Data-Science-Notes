import os
import glob
import re
import uuid
import shutil
import subprocess
import markdown
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = r"S:\B.Tech Data Science Notes"
PDF_DIR = os.path.join(BASE_DIR, "PDF_Notes")
os.makedirs(PDF_DIR, exist_ok=True)

def find_browser_executable():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe")
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

BROWSER_PATH = find_browser_executable()
if not BROWSER_PATH:
    raise RuntimeError("No Chromium-based browser (Chrome/Edge) found for PDF generation.")

print(f"Using Browser Engine for PDF Rendering: {BROWSER_PATH}")

CSS_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');

@page {
    size: A4 portrait;
    margin: 18mm 14mm 18mm 14mm;
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.8pt;
    line-height: 1.6;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
}

.pdf-header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #A90E02;
    padding-bottom: 5px;
    margin-bottom: 16px;
}

.pdf-header-title {
    font-weight: 800;
    font-size: 8.5pt;
    color: #A90E02;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.pdf-header-sub {
    font-size: 8pt;
    font-weight: 600;
    color: #64748b;
}

h1 {
    font-size: 17.5pt;
    font-weight: 900;
    color: #0f172a;
    line-height: 1.28;
    margin-top: 0;
    margin-bottom: 12px;
}

h2 {
    font-size: 12.5pt;
    font-weight: 800;
    color: #0f172a;
    margin-top: 20px;
    margin-bottom: 8px;
    padding-bottom: 3px;
    border-bottom: 1px solid #e2e8f0;
    page-break-after: avoid;
}

h3 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #A90E02;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

p {
    margin: 0 0 10px 0;
}

strong {
    color: #0f172a;
    font-weight: 700;
}

/* Callout Blocks */
blockquote {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #f59e0b;
    border-radius: 8px;
    padding: 10px 14px;
    margin: 14px 0;
    color: #334155;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

blockquote strong {
    color: #b45309;
}

/* Code Blocks */
pre {
    background: #0f172a;
    color: #e2e8f0;
    border-radius: 8px;
    padding: 12px 14px;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 8.5pt;
    line-height: 1.5;
    overflow-x: auto;
    margin: 12px 0;
    page-break-inside: avoid;
    border: 1px solid #1e293b;
    white-space: pre-wrap;
    word-break: break-word;
}

code {
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    background: #f1f5f9;
    color: #A90E02;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 8.5pt;
    font-weight: 600;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    font-weight: normal;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
}

th {
    background: #A90E02;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 7px 10px;
    border: 1px solid #A90E02;
}

td {
    padding: 6px 10px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

ul, ol {
    margin: 0 0 10px 0;
    padding-left: 20px;
}

li {
    margin-bottom: 4px;
}

hr {
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 16px 0;
}

.pdf-footer-bar {
    margin-top: 28px;
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    font-size: 7.5pt;
    color: #94a3b8;
    page-break-inside: avoid;
}
"""

def convert_single_note(md_path):
    rel_path = os.path.relpath(md_path, BASE_DIR).replace('\\', '/')
    fname = os.path.splitext(os.path.basename(md_path))[0]
    
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        md_content = f.read()

    # Convert markdown to html
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists']
    )

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{fname}</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>
<div class="pdf-header-bar">
    <div class="pdf-header-title">DataSci Notes Studio &bull; B.Tech Data Science</div>
    <div class="pdf-header-sub">GATE 2028 CSE &amp; DS Academic Ecosystem</div>
</div>

{html_body}

<div class="pdf-footer-bar">
    <div>DataSci Notes Studio &bull; Created by Suraj (B.Tech DS)</div>
    <div>University Exam &amp; Interview Ready &bull; Offline Study Edition</div>
</div>
</body>
</html>
"""

    temp_id = uuid.uuid4().hex
    temp_html = os.path.join(PDF_DIR, f"_tmp_{temp_id}.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(full_html)

    # 1. Output to structured directory path: PDF_Notes/Semester 3/.../file.pdf
    structured_pdf = os.path.join(PDF_DIR, rel_path[:-3] + ".pdf")
    os.makedirs(os.path.dirname(structured_pdf), exist_ok=True)

    # 2. Output to flat directory: PDF_Notes/filename.pdf
    flat_pdf = os.path.join(PDF_DIR, f"{fname}.pdf")

    cmd = [
        BROWSER_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={structured_pdf}",
        temp_html
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Fast copy for flat pdf
    if flat_pdf != structured_pdf:
        shutil.copy2(structured_pdf, flat_pdf)

    if os.path.exists(temp_html):
        try:
            os.remove(temp_html)
        except Exception:
            pass

    return rel_path

def main():
    md_files = glob.glob(os.path.join(BASE_DIR, "Semester 3", "**", "*.md"), recursive=True)
    total = len(md_files)
    print(f"\n=======================================================")
    print(f"[START] Starting High-Precision Chrome PDF Generation for {total} files...")
    print(f"=======================================================\n")

    completed = 0
    errors = 0

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(convert_single_note, md) for md in md_files]
        for f in futures:
            try:
                rel = f.result()
                completed += 1
                if completed % 25 == 0 or completed == total:
                    print(f"[PROGRESS] Converted {completed}/{total} notes to publication-grade PDFs...")
            except Exception as e:
                errors += 1
                print(f"[ERROR] Error converting note: {e}")

    print(f"\n=======================================================")
    print(f"[SUCCESS] ALL DONE: {completed}/{total} Magazine-Grade PDFs Generated Successfully! (Errors: {errors})")
    print(f"=======================================================\n")

if __name__ == '__main__':
    main()
