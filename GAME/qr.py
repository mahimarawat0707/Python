import qrcode 
qr = qrcode.make("My Name is Mahima")
qr.save("my_qrcode.png")
print("QR code generated and saved as 'my_qrcode.png'!")
qr.show()