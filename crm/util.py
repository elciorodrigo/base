import io
from PIL import Image


def remage(image_to_remage, width):
    new_width = int(width)
    image = Image.open(image_to_remage)
    width_image = image.size[0]
    height_image = image.size[1]
    percentage_width = float(new_width) / float(width_image)
    new_height = int((height_image * percentage_width))
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    #imagem.save('imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1]))
    output = io.BytesIO()
    image.save(output, format='png')
    return output.getvalue()

