from PIL import Image, ImageDraw, ImageFont

img = Image.open(r'download.jpg') 
draw = ImageDraw.Draw(img) 
text = "Nowshad Ruhan"
font = ImageFont.truetype('arial.ttf', 20)
textwidth, textheight = draw.textsize(text, font)
width, height = img.size 
x=width/2-textwidth/2
y=height-textheight-50
draw.text((x, y), text, font=font) 
img.save(r'download1.jpg')
Image.open('download1.jpg')