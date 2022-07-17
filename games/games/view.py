from django.shortcuts import render
import requests


#import json
def index(request):
   # return HttpResponse("<h1>Home</h1>")
   #myfile = open('games/games/aim.json', 'r')
   #jdata = myfile.read()
   # parse
   #obj = json.loads(jdata)
   # extract value obj['key]
   #title=obj['title']
   #platform=obj['platform']
   #score=obj['score']
   #gener=obj['genre']
   respond=request.POST.get('https://s3-ap-southeast-1.amazonaws.com/he-public-data/gamesarena274f2bf.json')
   return render(request,'index.html',{'respond':respond})









