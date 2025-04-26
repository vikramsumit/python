import requests

def download_pdf(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status codes

        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ PDF downloaded successfully as '{filename}'")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading PDF: {e}")

# Example usage
pdf_url = "https://books.google.co.in/books?id=2GxHVjz9n0gC&pg=PA1&source=kp_read_button&hl=en&newbks=1&newbks_redir=0&gboemv=1&ovdme=1&redir_esc=y#v=onepage&q&f=false"
save_as = "downloaded_file.pdf"

download_pdf(pdf_url, save_as)
