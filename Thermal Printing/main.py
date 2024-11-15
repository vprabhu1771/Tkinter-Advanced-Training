from escpos.printer import Usb


p = Usb(0x0416, 0x5011)

p.text("Hello, Windows!\n")
p.text("This is a test print using python-escpos.\n")

p.cut()
p.close()
