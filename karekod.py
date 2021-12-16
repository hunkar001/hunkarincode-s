import qrcode 

code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100,    #boyut
    border = 5         #kenarkalınlığı 

)

code.add_data("https://wwww.instagram.com/gencyazilimci0")
code.make(fit=True)

image = code.make_image(fill_color=(8,153,286),back_color="white")
image.save("qrcode.png")