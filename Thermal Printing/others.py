from escpos.printer import Usb

printer = Usb(0x1234, 0x5678)


def set_hardware_font(font_code):
    command = b'\x1b\x4d'+ font_code
    printer._raw(command)


def set_text_width(width_code):
    command = b'\x1b\x21'
    printer._raw(command)


try:
    set_hardware_font(b'\x00')

    set_text_width(b'\x01')

    printer.text("Hello, this is an example.\n")

except Exception as e:
    print("Error:", str(e))
    printer.close()



