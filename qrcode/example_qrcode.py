import qrcode

data = "https://www.graalvm.org/python/"

image = qrcode.make(data=data)
print(type(image))
image.save("graalpy_qr.png")

print("QR code saved to graalpy_qr.png")
