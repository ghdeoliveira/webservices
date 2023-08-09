import pycurl
import certifi
from io import BytesIO
# Creating a buffer as the cURL is not allocating a buffer for the network response
buffer = BytesIO()
c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'https://www.scrapingbee.com/')
#setting options for cURL transfer  
c.setopt(c.WRITEDATA, buffer)
#setting the file name holding the certificates
c.setopt(c.CAINFO, certifi.where())
# perform file transfer
c.perform()
#Ending the session and freeing the resources
c.close()

#retrieve the content BytesIO
body = buffer.getvalue()
#decoding the buffer 
print(body.decode('iso-8859-1'))






#/html/body/div[1]/div/div/section[1]/div/div/div[1]/div/div/span