import random
with open("short_urls.txt", "r") as f:
	short_urls=[i.strip() for i in f.readlines()]
alpha="abcdefghijklmnopqrstuvwxyz"
my_url="www.pyvy/"
lists=list(alpha+alpha.upper()+str(1234567890))
random.shuffle(lists)
link=""
def shorten(x):
	global link
	for i in range(5):
		link+=random.choice(x)
	link=my_url+link
shorten(lists)
while link in short_urls:
	shorten(lists)
else:
	with open("short_urls.txt","a") as f2:
		f2.seek(0,2)
		f2.write(link+"\n")
		print(link)