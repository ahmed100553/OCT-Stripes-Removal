from PIL import Image, ImageEnhance, ImageFilter

img = Image.open("m63219_res_SIP_420-444_res_output.tif")  # input image
img = img.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)
img = img.convert('1')
img.show()