from glob import glob
from fpdf import FPDF
from pathlib import Path

files = glob("./input/*txt")
pdf = FPDF()
for f in files:
    with open(f, "r") as file:
        content = file.read()

    title = Path(f).stem.title()
    pdf.add_page()
    pdf.set_font("Times", "B", 20)
    pdf.cell(0, 10, title, 0, 1)
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(0, 5, content, 0)

pdf.output("./output/animals.pdf")
