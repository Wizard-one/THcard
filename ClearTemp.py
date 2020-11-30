import os
import csv
from shutil import copytree, rmtree
""" 
删除临时HTML文件夹
"""
# 需要生成的目录
game = ('TH7','TH8','TH9','TH10','TH11','TH10.5','TH')
for num in game:
	#设置目录
	gamedir = "./img/"+num+'/'
	htmlfolder = gamedir+'html/'  # 存放html目录
	rmtree(htmlfolder)
