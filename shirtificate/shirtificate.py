from fpdf import FPDF
from PIL import Image


# Function to get image dimensions
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        # It returns width and height
        return img.size

def main():
    name_of_student = input("Enter name of student: ").strip()

    # Create a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Image path
    image_path = "shirtificate.png"

    page_width = pdf.w
    page_height = pdf.h

    image_width, image_height = get_image_dimensions(image_path)

    # Calculate x and y to center the image
    x = (page_width - image_width * 0.25) / 2
    y = (page_height - image_height * 0.25) / 2

    # Add image to PDF
    pdf.image(image_path, x=x, y=y, w=image_width * 0.25, h=image_height * 0.25)

    title_text = "CS50 Shirtificate"
    title_width = len(title_text)

    x_title = (page_width - title_width) / 2
    pdf.ln(20)
    pdf.set_x(x_title)
    pdf.set_font("Arial", "B", 40)
    pdf.cell(title_width, 10, title_text, ln=True, align='C')

    name_of_student = name_of_student + " took CS50"

    student_text_width = len(name_of_student)

    x_student = (page_width - student_text_width) / 2
    pdf.ln(85)
    pdf.set_x(x_student)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(student_text_width, 10, name_of_student, ln=True, align='C')

    # Save the PDF
    pdf.output("shirtificate.pdf")

main()
