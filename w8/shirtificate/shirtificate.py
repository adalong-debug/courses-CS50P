from fpdf import FPDF

def create(img_path, out_path, text):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    #shirt img start position
    pdf.image(img_path, x=10, y=70, w=190)  #est margin. 70 cuz A4 291mm's 1/4 around

    #title
    # style="B", size
    pdf.set_font("helvetica", "", 48)
    # Syntax: cell(w, h, text) or text(x, y, text)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C")
    # 0:"take up all the remaining space on this line."

    #name
    pdf.set_font("helvetica", "B", 36)
    pdf.set_text_color(255,255,255)
    # Move cursor to X=mm and Y=mm from the top-left
    pdf.set_xy(10, 100)
    pdf.cell(0, 70, text, align="C")

    pdf.output(out_path)

def main():
    create("shirtificate.png", "shirtificate2.pdf", input("name:")+" took CS50")

if __name__ == "__main__":
    main()
