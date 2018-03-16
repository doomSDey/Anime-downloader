link="http://m1.chia-anime.tv/view/b-the-beginning-episode-12/?c=1520094489"
n=15
def FirstEpi(link):
	pos=link.find("episode")
	res=link[pos:]
	pos1=res.find("-")
	print res[pos1+3]
	if(res[pos1+2]=="/"):
		res1=res[pos1+1:pos1+2]
	elif(res[pos1+3]=="/"):
		res1=res[pos1+1:pos1+3]
	elif(res[pos1+4]=="/"):
		res1=res[pos1+1:pos1+4]
	a=int(res1)					#converting string to int
	return a

i=FirstEpi(link)
i=i+1

while (i<=n):
	x=i-1
	x=str(x)
	prev="episode-"+x
	y=i
	y=str(y)
	next="episode-"+y
	link=link.replace(prev,next)
	print link
	i=i+1