# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

# test pandas table
data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
##############################################################

# Create your views here.
def index(request):
    if request.method == "POST":
        print("post")
        message = request.POST["message"]
        print(message)# html에서 입력한 text
        
        #모델에서 받아온 내용을 여기다가 담아서 보내면 될듯?
        context ={ 'df' : df.to_html(),
                    'image_url' : 'https://previews.123rf.com/images/marucyan/marucyan1211/marucyan121100106/16114832-%EC%83%88%EC%8B%B9.jpg?fj=1',
                    'text' : message}
        print(context)
        return render(request,'main/second.html',context)
    else:
        return render(request,'main/first.html') # first.html을 랜더링 해줘라





