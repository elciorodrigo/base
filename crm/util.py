
import io
from PIL import Image
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None