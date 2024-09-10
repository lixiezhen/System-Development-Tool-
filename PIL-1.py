from PIL import Image
pil_im = Image.open('image-20221226145619790.jpg')
pil_im.show()
pil_im2 = Image.open('image-20221226145619790.jpg').convert('L')

out = pil_im.resize((128,128))
out = pil_im.rotate(45)
out.show()