from escpos.printer import File

printer = File('')

printer.text("Hello, this will be written to the file.\n")
printer.cut()

