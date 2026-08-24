import os
import glob
import re
from fpdf import FPDF

BASE_DIR = r"S:\B.Tech Data Science Notes"
PDF_DIR = os.path.join(BASE_DIR, "PDF_Notes")
os.makedirs(PDF_DIR, exist_ok=True)

class AcademicPDF(FPDF):
    def __init__(self, title_text="DataSci Notes Studio"):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.doc_title = title_text
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font('helvetica', 'B', 8.5)
        self.set_text_color(169, 14, 2) # Crimson Red
        self.cell(0, 6, 'DataSci Notes Studio - B.Tech Data Science & Core CS Study Notes', border=0, align='R')
        self.ln(6)
        self.set_draw_color(169, 14, 2)
        self.set_line_width(0.4)
        self.line(10, 13, 200, 13)
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_font('helvetica', 'I', 7.5)
        self.set_text_color(100, 116, 139) # Slate Grey
        self.cell(0, 8, f'Page {self.page_no()}/{{nb}} | Created by Suraj (B.Tech DS) | GATE 2028', border=0, align='C')

def sanitize_text(text):
    if not text:
        return ""
    replacements = {
        '📌': '[DEF]', '⭐': '[MUST-WRITE]', '⚡': '[RECALL]', '🚀': '[CPP]', '🔹': '[C]',
        '💡': '[TIP]', '⚠️': '[NOTE]', '✅': '[OK]', '❌': '[X]', '🔑': '[KEY]',
        '•': '-', '—': '--', '–': '-', '“': '"', '”': '"', '‘': "'", '’': "'",
        '→': '->', '←': '<-', '⇒': '=>', '↔': '<->', '≤': '<=', '≥': '>=', '≠': '!=',
        '×': 'x', '÷': '/', 'µ': 'u', 'α': 'alpha', 'β': 'beta', 'π': 'pi', 'σ': 'sigma',
        '∪': 'U', '∩': 'n', '⋈': 'JOIN', '∞': 'inf', '°': ' deg', '…': '...'
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    return text.encode('latin-1', 'replace').decode('latin-1').replace('?', ' ')

def render_markdown_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    pdf = AcademicPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    in_code_block = False
    code_buffer = []
    in_table = False
    table_rows = []

    for raw_line in lines:
        line = raw_line.rstrip('\r\n')
        line_clean = sanitize_text(line).strip()

        # Code Blocks (```)
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_buffer = []
            else:
                in_code_block = False
                if code_buffer:
                    pdf.set_fill_color(248, 250, 252)
                    pdf.set_draw_color(203, 213, 225)
                    pdf.set_line_width(0.3)
                    pdf.set_font('courier', '', 7.5)
                    pdf.set_text_color(15, 23, 42)
                    
                    full_code = "\n".join(code_buffer)
                    pdf.multi_cell(190, 4.2, full_code, border=1, fill=True)
                    pdf.ln(2.5)
                code_buffer = []
            continue

        if in_code_block:
            code_buffer.append(sanitize_text(line))
            continue

        # Markdown Tables (| col | col |)
        if line_clean.startswith('|') and line_clean.endswith('|'):
            if re.match(r'^\|[\s\-\:\#\|\+]+\|$', line_clean):
                continue
            cells = [c.strip() for c in line_clean.split('|')[1:-1]]
            if cells:
                table_rows.append(cells)
            in_table = True
            continue
        elif in_table:
            if table_rows:
                num_cols = max(len(r) for r in table_rows)
                col_width = 190.0 / max(num_cols, 1)
                is_header = True
                for row in table_rows:
                    if is_header:
                        pdf.set_fill_color(169, 14, 2)
                        pdf.set_text_color(255, 255, 255)
                        pdf.set_font('helvetica', 'B', 7.5)
                        is_header = False
                    else:
                        pdf.set_fill_color(248, 250, 252)
                        pdf.set_text_color(30, 41, 59)
                        pdf.set_font('helvetica', '', 7.5)
                    
                    pdf.set_draw_color(203, 213, 225)
                    for col_idx in range(num_cols):
                        cell_val = row[col_idx] if col_idx < len(row) else ""
                        pdf.cell(col_width, 6, cell_val[:38], border=1, fill=True, align='L')
                    pdf.ln(6)
                pdf.ln(3)
            table_rows = []
            in_table = False

        if not line_clean:
            pdf.ln(1.5)
            continue

        # H1 Title
        if line_clean.startswith('# '):
            title = line_clean[2:].strip()
            pdf.set_font('helvetica', 'B', 14)
            pdf.set_text_color(169, 14, 2)
            pdf.multi_cell(190, 7.5, title)
            pdf.set_draw_color(169, 14, 2)
            pdf.set_line_width(0.6)
            pdf.line(10, pdf.get_y() + 1, 200, pdf.get_y() + 1)
            pdf.ln(4)

        # H2 Section Header
        elif line_clean.startswith('## '):
            heading = line_clean[3:].strip()
            pdf.ln(2)
            pdf.set_font('helvetica', 'B', 11)
            pdf.set_text_color(15, 23, 42)
            pdf.multi_cell(190, 6, heading)
            pdf.set_draw_color(226, 232, 240)
            pdf.set_line_width(0.3)
            pdf.line(10, pdf.get_y() + 0.5, 200, pdf.get_y() + 0.5)
            pdf.ln(2.5)

        # H3 Subsection Header
        elif line_clean.startswith('### '):
            subheading = line_clean[4:].strip()
            pdf.set_font('helvetica', 'B', 9.5)
            pdf.set_text_color(169, 14, 2)
            pdf.multi_cell(190, 5.5, subheading)
            pdf.ln(1)

        # Blockquote / Callout
        elif line_clean.startswith('>'):
            quote_text = line_clean[1:].strip()
            clean_quote = quote_text.replace('**', '').replace('`', '')
            pdf.set_fill_color(255, 251, 212)
            pdf.set_draw_color(169, 14, 2)
            pdf.set_line_width(0.8)
            pdf.set_font('helvetica', 'B' if any(k in clean_quote for k in ['Definition', 'Must-Write', 'Quick Recall']) else '', 8.5)
            pdf.set_text_color(51, 65, 85)
            pdf.multi_cell(190, 4.8, f"   {clean_quote}", border='L', fill=True)
            pdf.ln(2)

        # List Items
        elif line_clean.startswith('- ') or line_clean.startswith('* '):
            item_text = line_clean[2:].strip().replace('**', '').replace('`', '')
            pdf.set_font('helvetica', '', 8.5)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(190, 4.5, f"   *  {item_text}")

        elif re.match(r'^\d+\.\s', line_clean):
            item_text = line_clean.replace('**', '').replace('`', '')
            pdf.set_font('helvetica', '', 8.5)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(190, 4.5, f"   {item_text}")

        elif line_clean in ['---', '***', '___']:
            pdf.set_draw_color(226, 232, 240)
            pdf.set_line_width(0.2)
            pdf.line(10, pdf.get_y() + 1, 200, pdf.get_y() + 1)
            pdf.ln(3)

        else:
            para_text = line_clean.replace('**', '').replace('`', '')
            pdf.set_font('helvetica', '', 8.5)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(190, 4.5, para_text)

    if in_table and table_rows:
        num_cols = max(len(r) for r in table_rows)
        col_width = 190.0 / max(num_cols, 1)
        for row in table_rows:
            pdf.set_fill_color(248, 250, 252)
            pdf.set_text_color(30, 41, 59)
            pdf.set_font('helvetica', '', 7.5)
            pdf.set_draw_color(203, 213, 225)
            for col_idx in range(num_cols):
                cell_val = row[col_idx] if col_idx < len(row) else ""
                pdf.cell(col_width, 6, cell_val[:38], border=1, fill=True, align='L')
            pdf.ln(6)

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    pdf.output(pdf_path)

def main():
    md_files = glob.glob(os.path.join(BASE_DIR, "Semester 3", "**", "*.md"), recursive=True)
    count = 0
    errors = 0
    print(f"Generating structured & flat academic PDFs for all {len(md_files)} markdown files...")

    for md in md_files:
        rel_path = os.path.relpath(md, BASE_DIR).replace('\\', '/')
        
        # 1. Structured PDF: PDF_Notes/Semester 3/.../file.pdf (guarantees 100% uniqueness for every file)
        structured_pdf_path = os.path.join(BASE_DIR, "PDF_Notes", rel_path[:-3] + ".pdf")
        
        # 2. Flat PDF: PDF_Notes/filename.pdf
        flat_pdf_path = os.path.join(PDF_DIR, os.path.basename(md)[:-3] + ".pdf")

        try:
            render_markdown_to_pdf(md, structured_pdf_path)
            render_markdown_to_pdf(md, flat_pdf_path)
            count += 1
            if count % 30 == 0 or count == len(md_files):
                print(f"Rendered {count}/{len(md_files)} notes to PDF...")
        except Exception as e:
            errors += 1
            print(f"Error converting {rel_path}: {e}")

    print(f"\n=======================================================")
    print(f"SUCCESS: Generated all {count}/{len(md_files)} PDFs in structured and flat formats! (Errors: {errors})")
    print(f"=======================================================\n")

if __name__ == '__main__':
    main()
