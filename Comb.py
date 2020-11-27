from html2png import html2png_display
import re
import os
import csv
from shutil import copytree, rmtree
from PIL import Image
""" 
TouHou 卡牌生成器，利用HTML模板截图生成
"""
# 生成器html模板所在位置
temple = "html/Sample.html"
if not os.path.exists('./card/'):
	os.mkdir("./card")
# 需要生成的目录
game=('TH10','TH11')
with open(temple,encoding='utf-8') as f:
	html=f.read()
for num in game:
	#设置目录
	gamedir="./img/"+num+'/'
	titledir=gamedir+'title.csv'#称号和名字
	shadir='../../2/'#立绘填充
	maindir='../../1/'#立绘
	htmlfolder = gamedir+'html/'#存放html目录
	carddir = "./card/"+num+"/"#存放卡的目录
	#创建工作html文件夹
	if os.path.exists(htmlfolder):
		#如果存在就刷新所有目录
		rmtree(htmlfolder)
		os.mkdir(htmlfolder)
	if not os.path.exists(carddir):
		os.mkdir(carddir)  # 卡片保存目录
	with open(titledir,encoding='utf-8') as f:
		title=csv.reader(f)
		for i,row in enumerate(title):
			#批量替换素材
			htmldir = htmlfolder+str(i+1)+'/Sample.html'
			copytree('./html/', htmlfolder+str(i+1))
			shadirc=shadir+str(i+1)+'.png'#当前卡图
			maindirc=maindir+str(i+1)+'.png'#当前卡图
			curcard = re.sub("mytitle",row[0],html)
			curcard = re.sub("myname",row[1],curcard)
			curcard = re.sub("TH6",num,curcard)
			curcard = re.sub("Sample_sha.png", shadirc, curcard)
			curcard = re.sub("Sample_main.png", maindirc, curcard)
			with open(htmldir,'w',encoding='utf-8') as f:
				f.write(curcard)
			html2png_display(htmldir, htmlfolder+'temp.png')
			#设置色彩模式和dpi
			im = Image.open(htmlfolder+'temp.png')
			im = im.convert(mode="CMYK")
			im.save(carddir+str(i+1)+'.jpg', dpi=(300.0, 300.0))  # 保存文件
			os.remove(htmlfolder+'temp.png')
			print(row[1], 'OK')
	# rmtree(htmlfolder)#删除html工作目录

		 
			
