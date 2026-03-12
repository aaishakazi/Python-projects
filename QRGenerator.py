import qrcode

def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

url = input("Enter the URL or text to generate QR code for: ")
filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")
generate_qr_code(url, filename)