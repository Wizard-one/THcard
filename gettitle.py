from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
#open site
urls = ["https://thwiki.cc/%E4%B8%9C%E6%96%B9%E8%8A%B1%E6%98%A0%E5%A1%9A_%EF%BD%9E_Phantasmagoria_of_Flower_View.",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E9%A3%8E%E7%A5%9E%E5%BD%95_%EF%BD%9E_Mountain_of_Faith.",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E5%9C%B0%E7%81%B5%E6%AE%BF_%EF%BD%9E_Subterranean_Animism.",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E6%98%9F%E8%8E%B2%E8%88%B9_%EF%BD%9E_Undefined_Fantastic_Object.",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%A5%9E%E7%81%B5%E5%BA%99_%EF%BD%9E_Ten_Desires.",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E8%BE%89%E9%92%88%E5%9F%8E",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BB%80%E7%8F%A0%E4%BC%A0",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E5%A4%A9%E7%A9%BA%E7%92%8B",
       "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E9%AC%BC%E5%BD%A2%E5%85%BD"]
for url in urls:
	html=urlopen(url)
	#get site object
	bsObj=BeautifulSoup(html, "html.parser")
	#get red text
	titleList=bsObj.findAll("td",{"style":"width:150px;padding:3px 9px 3px 7px;"})
	with open("title.csv", 'a', encoding="utf-8") as f:
		for name in titleList:
			print(name.get_text())
			f.writelines(name.get_text()+',\n')
