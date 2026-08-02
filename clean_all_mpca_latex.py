import os
import glob
import re

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

def clean_content(text):
    # Fix control characters introduced by python string escaping (\x0c, \t, \a, \b)
    text = text.replace('\x0c', '\\f').replace('\a', '\\a')
    
    # Specific common replacements
    text = text.replace('\\frac', 'frac')
    text = text.replace('rac', 'frac')
    text = text.replace('\\times', '×')
    text = text.replace('	imes', '×')
    text = text.replace('\\cdot', '×')
    text = text.replace('	ext', '')
    text = text.replace('\\text', '')
    text = text.replace('{', '').replace('}', '')
    text = text.replace('\\overline', '').replace('\\bar', '')
    text = text.replace('\\to', '->').replace('	o', '->')
    text = text.replace('\\infty', '∞')
    text = text.replace('\\approx', '≈')
    text = text.replace('\\mathbf', '')
    text = text.replace('\\tau', 'τ')
    
    # Clean up dollar signs
    lines = text.split('\n')
    cleaned_lines = []
    in_block = False
    
    for line in lines:
        if line.strip().startswith('$$') and line.strip().endswith('$$') and len(line.strip()) > 4:
            content = line.strip()[2:-2].strip()
            # Clean content inside block
            content = content.replace('frac', '').replace('\\', '').strip()
            cleaned_lines.append(f"```\n{content}\n```")
        elif '$$' in line:
            line = line.replace('$$', '')
            cleaned_lines.append(line)
        else:
            # Clean inline $...$
            line = re.sub(r'\$([^$]+)\$', r'**\1**', line)
            cleaned_lines.append(line)
            
    res = '\n'.join(cleaned_lines)
    # Post cleaning polish
    res = res.replace('****', '').replace('** **', ' ')
    res = res.replace('MN/MX', 'MN/MX#')
    res = res.replace('MN/MX#', 'MN/MX (Pin 33)')
    res = res.replace('AD_0 - AD_15', 'AD0 - AD15')
    res = res.replace('A_16/S_3 - A_19/S_6', 'A16/S3 - A19/S6')
    res = res.replace('BHE', 'BHE#')
    return res

md_files = glob.glob(os.path.join(MPCA_DIR, "**", "*.md"), recursive=True)
count = 0
for fpath in md_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = clean_content(content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Cleaned: {os.path.basename(fpath)}")

print(f"Cleaned {count} MPCA files successfully!")
