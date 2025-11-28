import qrcode

url_to_encode = input("Enter text or URL to encode: ")

qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr_code.add_data(url_to_encode)

qr_code.make(fit=True)

qr_image = qr_code.make_image(fill_color="black", back_color="white")

qr_image.save('qr_encoder/qr_code.png')