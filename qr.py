import pyqrcode
s = "https://github.com/Akashsshinde07"
url = pyqrcode.create(s)
url.svg("mydr1.svg", scale = 8)
