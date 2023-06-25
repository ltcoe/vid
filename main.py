
# from crypt import methods
# from urllib import request
from flask import Flask,render_template,request
from bs4 import BeautifulSoup as bs
import requests

url_link = "https://indimonk.in/indimonk.in/kunal/"
result = requests.get(url_link)
soup = bs(result.content, "html.parser")

li=[]
td= soup.find_all('a', href=True)
for all in td:
    li.append(all.text)

li=li[4:]
print(li)


app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html',data=li)

@app.route('/video',methods =["GET", "POST"])
def video():
	if request.method=='POST':
		value=request.form.get('sel')
		url="https://indimonk.in/indimonk.in/kunal/"+value
		iframe=""" <div style="padding-top: 56.34%; position: relative; overflow: hidden;"><iframe frameborder="0" allowfullscreen="" scrolling="no" allow="autoplay;fullscreen" src="https://onelineplayer.com/player.html?autoplay=false&autopause=false&muted=false&loop=true&url=""" +url+ """&poster=&time=true&progressBar=true&overlay=true&muteButton=true&fullscreenButton=true&style=light&quality=auto&playButton=true" style="position: absolute; height: 100%; width: 100%; left: 0px; top: 0px;"></iframe></div> """
		print(iframe)
	return render_template("video.html",iframe=iframe)




if __name__ == '__main__':


	app.run()
