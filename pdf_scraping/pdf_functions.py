import requests
from bs4 import BeautifulSoup
from markitdown import MarkItDown
import os

def get_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    
def  extract_pdf_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_link = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            pdf_link.append(href)
    return pdf_link

def download_pdf(url, filename):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        with open(filename, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the PDF: {e}")

def get_pdfs(url = "https://fi-ing.unison.mx/acuerdos-de-sesiones-del-h-colegio-de-la-facultad-interdisciplinaria-de-ingenieria-2026/"):
    download_path = "downloaded_pdfs"
    if not os.path.exists(download_path):
        #create the directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)
    html = get_webpage(url)
    if not html:
        print("Failed to retrieve the webpage.")
        exit(1)
    pdf_links = extract_pdf_links(html)
    for link in pdf_links:
        print(link)
        filename = link.split('/')[-1]  # Get the filename from the URL
        downloaded_path = os.path.join(download_path, filename)  # Create the full path for the PDF
        download_pdf(link, f"{downloaded_path}")  # Save the PDF in the 'pdfs' directory
        print(f"Downloaded: {downloaded_path}")

def convert_pdf_to_markdown(pdf_path, markdown_path):
    # Placeholder for PDF to Markdown conversion logic
    try:
        convert = MarkItDown()
        result = convert.convert(pdf_path)
        markdown_content = result.markdown or result.text_content
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
    except Exception as e:
        print(f"Error converting PDF to Markdown: {e}")

def main():
    if not os.path.exists("markdown_files"):
        os.makedirs("markdown_files", exist_ok=True)  # Create the directory if it doesn't exist
    for filename in os.listdir("downloaded_pdfs"):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join("downloaded_pdfs", filename)
            markdown_path = os.path.join("markdown_files", f"{os.path.splitext(filename)[0]}.md")
            convert_pdf_to_markdown(pdf_path, markdown_path)
            print(f"Converted {filename} to Markdown.")

if __name__ == "__main__":
    main()