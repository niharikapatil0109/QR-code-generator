


print("Hello World")# Importing library
import qrcodegen

# Data to be encoded
data = ''

# Encoding data using make() function
img = qrcodegen.make(data)

# Saving as an image file
img.save('myqrcode.jpeg')
