import os
import glob
import re

PROJECT_DIR = r"S:\B.Tech Data Science Notes\Semester 3"

def clean_file_content(content):
    original = content
    
    # 1. Fix control characters & raw escape corruption
    content = content.replace('\x0c', '').replace('\a', '').replace('\b', '')
    content = content.replace('rac', 'frac').replace('\\frac', 'frac')
    text_replacements = [
        ('	ext', ''),
        ('\\text', ''),
        ('	imes', '×'),
        ('\\times', '×'),
        ('\\cdot', '×'),
        ('	o', '->'),
        ('\\to', '->'),
        ('\\infty', '∞'),
        ('\\approx', '≈'),
        ('\\mathbf', ''),
        ('\\tau', 'τ'),
        ('\\sum', 'Sum'),
        ('\\Big[', '['),
        ('\\Big]', ']'),
        ('\\Big', ''),
        ('\\big', '')
    ]
    for old, new in text_replacements:
        content = content.replace(old, new)

    # 2. Convert latex fraction patterns like frac{A}{B} to (A / B)
    content = re.sub(r'frac\{([^}]+)\}\{([^}]+)\}', r'(\1 / \2)', content)
    
    # 3. Clean up curly braces around simple identifiers like {DS}, {10H}, etc.
    content = re.sub(r'\{([A-Za-z0-9_+\- ]+)\}', r'\1', content)

    # 4. Clean dollar signs
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            expr = stripped[2:-2].strip()
            expr = expr.replace('\\', '').strip()
            cleaned_lines.append(f"```\n{expr}\n```")
        elif '$$' in line:
            line = line.replace('$$', '')
            cleaned_lines.append(line)
        else:
            # Inline $...$ to bold text
            line = re.sub(r'\$([^$]+)\$', r'**\1**', line)
            cleaned_lines.append(line)

    result = '\n'.join(cleaned_lines)
    # Final cleanup of double bolds
    result = re.sub(r'\*\*\*\*+', '', result)
    result = result.replace('** **', ' ')
    return result

md_files = glob.glob(os.path.join(PROJECT_DIR, "**", "*.md"), recursive=True)
modified_count = 0

print(f"Scanning {len(md_files)} markdown files in {PROJECT_DIR}...")

for fpath in md_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        cleaned_text = clean_file_content(raw_text)
        
        if cleaned_text != raw_text:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)
            modified_count += 1
            print(f"Cleaned & Formatted: {os.path.relpath(fpath, PROJECT_DIR)}")
    except Exception as e:
        print(f"Error processing {fpath}: {e}")

print(f"\nCompleted! Cleaned and perfected {modified_count} files out of {len(md_files)} total files.")
