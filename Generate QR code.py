import qrcode
SSID = input("What is the SSID? ")
PASSWORD = input("What is the Password? ")
codetext = 'WIFI:T:{type};S:{ssid};P:{password};H:{hidden};;'.format(type="WPA", ssid=SSID, password=PASSWORD, hidden="false")
print(codetext)
qrcodeObject = qrcode.make(codetext).get_image()
qrcodeObject.save(SSID+".png")
