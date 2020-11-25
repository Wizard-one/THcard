from html2png import html2png_display
import re
import os
import csv
from shutil import copytree, rmtree
from PIL import Image
# 生成器html模板所在位置
temple = "html/Sample.html"
# 需要生成的目录
game=('TH6',)
with open(temple,encoding='utf-8') as f:
	html=f.read()
for num in game:
	#设置目录
	gamedir="./img/"+num+'/'
	titledir=gamedir+'title.csv'#称号和名字
	shadir='../2/'#立绘填充
	maindir='../1/'#立绘
	htmldir = gamedir+'html/Sample.html'
	carddir = gamedir+"card/"
	#创建工作html文件夹
	if os.path.exists(gamedir+'html/'):
		rmtree(gamedir+'html/')
	copytree('./html/',gamedir+'html/')
	os.mkdir(gamedir+"card/")#卡片保存目录
	with open(titledir,encoding='utf-8') as f:
		title=csv.reader(f)
		for i,row in enumerate(title):
			#批量替换素材
			shadirc=shadir+str(i+1)+'.png'
			maindirc=maindir+str(i+1)+'.png'
			curcard = re.sub("mytitle",row[0],html)
			curcard = re.sub("myname",row[1],curcard)
			curcard = re.sub("TH6",num,curcard)
			curcard = re.sub("Sample_sha.png", shadirc, curcard)
			curcard = re.sub("Sample_main.png", maindirc, curcard)
			with open(htmldir,'w',encoding='utf-8') as f:
				f.write(curcard)
			html2png_display(htmldir, carddir+'temp.png')
			#设置色彩模式和dpi
			im = Image.open(carddir+'temp.png')
			im = im.convert(mode="CMYK")
			im.save(carddir+row[1]+'.jpg', dpi=(300.0, 300.0))  # 保存文件
			print(row[1],'OK')
		os.remove(carddir+'temp.png')
	rmtree(gamedir+'html/')#删除html工作目录

		 
			
