from PIL import Image


def decode_image(file_location="images/encoded_sample.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[1]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
    decoded_image.save("decoded_image.png")

decode_image('download.png')