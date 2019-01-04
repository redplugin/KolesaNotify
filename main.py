import bs4
import requests
import smtplib

# Download page
getPage = requests.get('https://kolesa.kz/cars/region-almatinskaya-oblast/?auto-emergency=1&auto-car-transm=2345&auto-sweel=1&auto-car-volume[to]=2&price[to]=900%20000&year[from]=1993')

# if error it will stop the program
getPage.raise_for_status()

# Parse text for foods
searchResults = bs4.BeautifulSoup(getPage.text, 'html.parser')
lastUploadedCar = searchResults.select_one('#results .vw-item')

print(lastUploadedCar['id'])
