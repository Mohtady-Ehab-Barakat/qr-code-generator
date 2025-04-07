import qrcode
from PIL import Image


def generate_transparent_qr(data, output_file="transparent_qr.png", size=10, border=2):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_image = qr.make_image(fill="black", back_color="white").convert("RGBA")
    
    # Make the white background transparent
    qr_pixels = qr_image.load()
    for y in range(qr_image.size[1]):
        for x in range(qr_image.size[0]):
            r, g, b, a = qr_pixels[x, y]
            if r == 255 and g == 255 and b == 255:  # White background
                qr_pixels[x, y] = (255, 255, 255, 0)  # Make transparent

    # Save the transparent QR code
    qr_image.save(output_file)
    print(f"Transparent QR code saved as {output_file}")


# Example usage
text = "https://drive.google.com/file/d/1AU68xzX206sv2VgzgByZPO9MZRPG6jzl/view?usp=drive_link"
generate_transparent_qr(text)
