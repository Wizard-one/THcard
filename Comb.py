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
def ChangeDpi(path,out_path):
	"""
	设置色彩模式，修改生成PNG DPI 并转换成jpg
	"""
	im = Image.open(path)
	im = im.convert(mode="CMYK")
	im.save(out_path, dpi=(300.0, 300.0))  # 保存文件
	os.remove(path)

def SubHTML(html,row,num,main,sha,**kw):
	"""
	替换HTML文件
	"""
	curcard = re.sub("mytitle", row[0], html)
	curcard = re.sub("myname",row[1],curcard)
	curcard = re.sub("TH6",num,curcard)
	curcard = re.sub("Sample_sha.png", sha, curcard)
	curcard = re.sub("Sample_main.png", main, curcard)
	return curcard

class Path_check(object):
	"""
	检查目录是否存在
	"""
	def __init__(self):
		pass

	def card(self):
		"""
		card path
		"""
		if not os.path.exists('./card/'):
			os.mkdir("./card")
	def html(self,path):
		"""
		gamedir 下 html工作目录
		"""
		if os.path.exists(path):
			#如果存在就刷新所有目录
			rmtree(path)
			os.mkdir(path)
	def cardsub(self,path):
		"""
		card 下 gamedir
		"""
		if not os.path.exists(path):
			os.mkdir(path)  # 卡片保存目录
	
# 生成器html模板所在位置

Pk=Path_check()
Pk.card()#生成卡牌的目录
# 需要生成的目录
temple = "html/Sample.html"
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
	Pk.html(htmlfolder)
	Pk.cardsub(carddir)
	with open(titledir,encoding='utf-8') as f:
		title=csv.reader(f)
		for i,row in enumerate(title):
			#批量替换素材
			htmldir = htmlfolder+str(i+1)+'/Sample.html'
			copytree('./html/', htmlfolder+str(i+1))
			shadirc=shadir+str(i+1)+'.png'#当前卡图
			maindirc=maindir+str(i+1)+'.png'#当前卡图
			curcard=SubHTML(html,row=row,num=num,sha=shadirc,main=maindirc)
			with open(htmldir,'w',encoding='utf-8') as f:
				f.write(curcard)
			html2png_display(htmldir, htmlfolder+'temp.png')
			ChangeDpi(htmlfolder+'temp.png', carddir+str(i+1)+'.jpg')
			print(row[1], 'OK')

		 
			
