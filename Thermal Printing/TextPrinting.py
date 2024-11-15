from escpos.printer import Usb

p = Usb(0x0416, 0x5011)

p.set(align='center', text_type='B', width=2, height=2, density=8, invert=True)

p.text("Hello, Bold and Underlined!\n")

p.set(align='left', text_type='NORMAL', width=1, height=1, density=6, invert=False)

p.text("This is a regular text.\n")

p.set(align='right', text_type='U', width=1, height=1, density=8, invert=True)

p.text("This text is underlined and inverted.\n")

p.set(align='left', text_type='NORMAL', width=1, height=1, density=6, invert=False)


p.char_spacing(n=3)
p.line_spacing(n=30)

p.text("Custom spacing example.\n")

p.char_spacing(n=0)
p.line_spacing(n=0)

p.cut()
p.close()

