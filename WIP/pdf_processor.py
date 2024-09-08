from pypdf import PdfReader 
import requests

url = 'https://img.amizone.net/AzureFileHandler.ashx?FileName=amizonefiles/PlacementPdf/Placement_295eeb.pdf'
response = requests.get(url)
with open('temporary_placement.pdf', 'wb') as file:
    file.write(response.content)

pdf = PdfReader('temporary_placement.pdf')

# Left for Later