import  pyqrcode
url = input("Enter url to Generate Your QR code:")
out = pyqrcode.create(url)
out.svg('Qr.svg,scale=10')