from PIL import Image
import io
def openim(image):
    im = Image.open(image)
    if im.format=="PNG":
        return im
    out=io.BytesIO()
    im.save(out,"PNG")
    return Image.open(out)
