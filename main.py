import bs4
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Download page
getPage = requests.get('https://kolesa.kz/cars/region-almatinskaya-oblast' +
                       '/?auto-emergency=1&auto-car-transm=2345&auto-sweel=1' +
                       '&auto-car-volume[to]=2&price[to]=900%20000&year[from]=1993')

# if error it will stop the program
getPage.raise_for_status()

# Parse text for foods
searchResults = bs4.BeautifulSoup(getPage.text, 'html.parser')
lastUploadedCar = searchResults.select_one('#results .vw-item')

lastUploadedCarId = lastUploadedCar['id']

# open the file where previous last car id is:
fileHandle = open('text.txt', 'r')

# if the previous last car id and last car id don't match, write new last id to the file and send email:
if lastUploadedCarId not in fileHandle.readline():
    newFile = open("text.txt", "w")
    newFile.write(lastUploadedCarId)
    newFile.close()

    # car info
    carName = lastUploadedCar.select_one('.a-el-info-title > a').text.strip()
    carYear = lastUploadedCar.select_one('.year').text.strip()
    carPrice = lastUploadedCar.select_one('.price').text.strip()

    # send message
    message = carName + '\n' + ' ' + carYear + ' for ' + carPrice + '\n' + lastUploadedCarId
    msg = MIMEMultipart()
    password = "Usmc1775ex!"  # Type your password
    msg['From'] = "kolesanotify@yandex.kz"  # Type your own gmail address
    msg['To'] = "darmen89@yandex.ru"  # Type your friend's mail address
    msg['Subject'] = "New car: " + carName  # Type the subject of your message
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.yandex.com: 587')
    server.starttls()
    server.login('kolesanotify', password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

