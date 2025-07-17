```
https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
```

# 1 - pyqrcode module

pyqrcode module is a QR code generator. The module automates most of the building process for creating QR codes. This module attempts to follow the QR code standard as closely as possible. The terminology and the encodings used in pyqrcode come directly from the standard.


pyqrcode.create(content, error='H', version=None, mode=None, encoding=None) : When creating a QR code only the content to be encoded is required, all the other properties of the code will be guessed based on the contents given. This function will return a QRCode object.

One can specify all the properties of required QR code through the optional parameters of the pyqrcode.create() function. Below are some properties:


error: This parameter sets the error correction level of the code.
version: This parameter specifies the size and data capacity of the code.
mode: This parameter sets how the contents will be encoded.

```
pip install pyqrcode
```

# 2 - pypng module

install an additional module pypng to save image in png format

```
pip install pypng
```

# 3 - `app.py`

```
# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "www.bughunt.in"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)

# Print QRCODE in Terminal
print(url.terminal(quiet_zone=1))
```