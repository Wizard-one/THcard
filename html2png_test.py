from html2png import html2png_display
from PIL import Image,ImageDraw


htfn="html/Sample.html"
html2png_display(htfn,"demo.png")
im=Image.open("demo.png")
im=im.convert(mode="CMYK")
im.save("target.jpg", dpi=(300.0, 300.0))  # 保存文件
