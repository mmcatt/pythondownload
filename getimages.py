# -*- coding:utf8 -*-
#用于批量获取文件名比较规范的内容，此处为批量获取素材图片时写的，代码不难，主要是需求分析，获得解决方案
#分析该图片网站，发现所有图片的url格式规范，故写脚本获取之

import urllib2


def download(url,filename):
	try:
		f = urllib2.urlopen(url)
		with open(filename+".jpg","wb") as file:
			file.write(f.read())
	except Exception, e:
		print ("ERROR:"+e)
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	url1 = "http://finda.photo/image/"
	#17038
	url2 = "/thumbnail/original"
	a = 16000
	b = 17082
	for n in range (a,b):
		download(url1+str(n)+url2,str(n))
