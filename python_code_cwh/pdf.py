import PyPDF2

def extract_pages(input_pdf, output_pdf, page_ranges):
    try:
        # Open the PDF file
        with open(input_pdf, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            # Parse page ranges (e.g., "1,3-5,7")
            pages_to_extract = set()
            for part in page_ranges.split(","):
                if "-" in part:
                    start, end = map(int, part.split("-"))
                    pages_to_extract.update(range(start, end + 1))
                else:
                    pages_to_extract.add(int(part))

            # Extract selected pages
            for page_num in sorted(pages_to_extract):
                if 1 <= page_num <= len(reader.pages):
                    writer.add_page(reader.pages[page_num - 1])  # Pages are zero-indexed
                else:
                    print(f"Warning: Page {page_num} is out of range and will be ignored.")

            # Save the new PDF
            with open(output_pdf, "wb") as output_pdf_file:
                writer.write(output_pdf_file)

            print(f"Pages extracted successfully to '{output_pdf}'")

    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    input_pdf = r"/home/raju/PDF/BTECH_IT.pdf"


    output_pdf = r"/home/raju/PDF/output.pdf"  # Change to desired output path
    page_input = input("Enter pages to extract (e.g., 1,3-5,7): ")
    
    extract_pages(input_pdf, output_pdf, page_input)
