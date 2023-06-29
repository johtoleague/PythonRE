import requests
from bs4 import BeautifulSoup

# Make an HTTP request
response = requests.get('https://www.example.com')

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the paragraph tags
paragraphs = soup.find_all('p')

# Print the text from each paragraph
for p in paragraphs:
    print(p.get_text())
