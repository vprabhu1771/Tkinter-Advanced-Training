from escpos.printer import Usb

p = Usb(0x0416, 0x5011)

p.text("hello, paper control!\n")
p.text("This is a text print using python-escpos.\n")

p.cut()

p.feed(3)

p.text("This is after paper feeding.\n")

p.cut()

p.close()


