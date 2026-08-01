import os
import glob
from fpdf import FPDF

PDF_DIR = r"S:\B.Tech Data Science Notes\PDF_Notes"
os.makedirs(PDF_DIR, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(169, 14, 2) # Crimson Red
        self.cell(0, 8, 'DataSci Notes Studio - B.Tech Data Science Study Notes', border=0, align='R')
        self.ln(8)
        self.set_draw_color(169, 14, 2)
        self.line(10, 16, 200, 16)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Created by Suraj (B.Tech DS)', border=0, align='C')

def sanitize(text):
    return text.encode('ascii', 'ignore').decode('ascii')

def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    lines = content.split('\n')
    for line in lines:
        line_clean = sanitize(line).strip()
        if not line_clean:
            pdf.ln(3)
            continue

        if line_clean.startswith('# '):
            pdf.set_font('Helvetica', 'B', 15)
            pdf.set_text_color(169, 14, 2)
            pdf.multi_cell(190, 8, line_clean[2:])
            pdf.ln(2)
        elif line_clean.startswith('## '):
            pdf.set_font('Helvetica', 'B', 12)
            pdf.set_text_color(26, 26, 26)
            pdf.multi_cell(190, 7, line_clean[3:])
            pdf.ln(2)
        elif line_clean.startswith('### '):
            pdf.set_font('Helvetica', 'B', 10)
            pdf.set_text_color(169, 14, 2)
            pdf.multi_cell(190, 6, line_clean[4:])
            pdf.ln(2)
        elif line_clean.startswith('- ') or line_clean.startswith('* '):
            pdf.set_font('Helvetica', '', 9)
            pdf.set_text_color(40, 40, 40)
            pdf.multi_cell(190, 5, f"   - {line_clean[2:]}")
        else:
            pdf.set_font('Helvetica', '', 9)
            pdf.set_text_color(40, 40, 40)
            pdf.multi_cell(190, 5, line_clean)

    pdf.output(pdf_path)

md_files = glob.glob(r"S:\B.Tech Data Science Notes\Semester 3\**\*.md", recursive=True)
count = 0
for md in md_files:
    fname = os.path.splitext(os.path.basename(md))[0] + ".pdf"
    pdf_out = os.path.join(PDF_DIR, fname)
    try:
        md_to_pdf(md, pdf_out)
        count += 1
    except Exception as e:
        print(f"Error PDF {fname}: {e}")

print(f"Generated {count} PDFs successfully in PDF_Notes!")
