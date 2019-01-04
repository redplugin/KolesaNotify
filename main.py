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

lastUploadedCarId = lastUploadedCar['id']

conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
conn.ehlo()  # call this to start the connection
conn.starttls()  # starts tls encryption. When we send our password it will be encrypted.
conn.login('darmen1@gmail.com', 'Usmc1775le!')
conn.sendmail('darmen1@gmail.com', 'darmen89@yandex.ru',
              'Subject: Kolesa notify: ' + lastUploadedCarId)
conn.quit()