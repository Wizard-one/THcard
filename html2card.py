from html2png import html2png_display
import re
import os
import csv
from shutil import copytree, rmtree
from PIL import Image
""" 
TouHou 卡牌生成器，利用HTML模板截图生成
"""
game = ('TH',)

def ChangeDpi(path, out_path):
	"""
	设置色彩模式，修改生成PNG DPI 并转换成jpg
	"""
	im = Image.open(path)
	im = im.convert(mode="CMYK")
	im.save(out_path, dpi=(300.0, 300.0))  # 保存文件
	os.remove(path)

with open('modify.csv',encoding='utf-8') as f:
	mo=csv.reader(f)
	for row in mo:
		#读取需要转换的HTML目录
		htmlfolder='./img/'+row[0]+'/html/'+row[1]+'/'
		htmldir = htmlfolder+'Sample.html'
		carddir = "./card/"+row[0]+"/"  # 存放卡的目录
		html2png_display(htmldir,htmlfolder+'tmp.png')
		ChangeDpi(htmlfolder+'tmp.png', carddir+row[1]+'.jpg')
		print(row,'OK')
