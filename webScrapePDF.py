import requests
from bs4 import BeautifulSoup as bs

def getPDFs(url, folder):
    
    # gather html and make pretty
    data = requests.get(url)
    soup = bs(data.text, 'html.parser')
    links = soup.find_all('a')
    
    #loop through html and grab pdf links
    i = 0
    for link in links:
        if ('.pdf' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)
    
            # Get response object for link
            response = requests.get(link.get('href'))
    
            # Write content to file
            pdf = open(folder+str(i)+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", i, " downloaded")
    
    print("All PDF files downloaded")