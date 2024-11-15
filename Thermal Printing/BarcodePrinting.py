from escpos.printer import Usb

p = Usb(0x0416, 0x5011)

p.barcode('123456789', 'CODE39', width=2, height=100, pos='BELOW', font='B')
p.barcode('987654321', 'CODE128', width=2, height=100, pos='BELOW', font='B')

p.barcode('http:// www.example.com', 'QR', width=6, version=20)

p.cut()
p.close()