# pdf_writer.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def text_to_pdf(input_file, output_file):
    page_width, page_height = letter
    margin = 1 * inch
    usable_width = page_width - 2 * margin
    usable_height = page_height - 2 * margin

    c = canvas.Canvas(output_file, pagesize=letter)
    c.setFont("Helvetica", 12)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    x = margin
    y = page_height - margin
    line_height = 14

    for line in lines:
        words = line.strip().split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if c.stringWidth(test_line, "Helvetica", 12) <= usable_width:
                current_line = test_line
            else:
                c.drawString(x, y, current_line)
                y -= line_height
                if y < margin:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y = page_height - margin
                current_line = word

        if current_line:
            c.drawString(x, y, current_line)
            y -= line_height
            if y < margin:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = page_height - margin

    c.save()
    print(f"✅ PDF created: {output_file}")

