# install PIL library : pip install PIL

from PIL import Image

def conv_img_to_pdf():
    image=Image.open('python.png')
    pdf=image.convert('RGB')
    pdf.save('converted.pdf')

conv_img_to_pdf()

