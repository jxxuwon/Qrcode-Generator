from PIL import Image
import qrcode

def generate_qr_code(info, file_name):
    qr = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 10,
        border = 4
    )

    qr.add_data(info)
    qr.make(fit = True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

info = input("Write Your QR CODE Information : ")
file_name = input("Write QR CODE Image Name (ex : qr.png): ")

generate_qr_code(info, file_name)
print(f"QR code saved as <{file_name}>")

# jw