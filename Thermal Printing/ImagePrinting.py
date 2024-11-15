from escpos.printer import Usb

p = Usb(0x0416, 0x5011)

image_path = ''

p.image(image_path)

p.cut()
p.close()

