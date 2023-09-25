from django.shortcuts import HttpResponse,render,redirect
import pandas as pd
import webbrowser

# Create your views here.


def login(request):
    return render(request,'index.html')
# def map_demo(request):
#     return render(request,'map_demo.html')

def UTC(requset):
    return redirect('https://www.matools.com/timestamp?embed')

def map(request):
    return render(request,"map.html")

def relay2(request):
    star = request.GET.get('StartTime')
    end = request.GET.get('EndTime')
    StartTime = int(star)
    EndTime = int(end)
    data = pd.read_csv(r'./static/data/0912_view.csv',encoding='utf-8')
    dta = data[(data['UTC'] >= StartTime) & (data['UTC'] <= EndTime)]
    car = []
    for i in range(0,len(dta)):
        car.append({'lat':dta.iloc[i,2],'lng':dta.iloc[i,3],'name':dta.iloc[i,0]})
    return render(request, 'View.html', {"aa": car})

def relay3(request):
    StartTime = int(request.GET.get('StartTime'))
    EndTime = int(request.GET.get('EndTime'))
    CarID = int(request.GET.get('CarId'))
    data = pd.read_csv(r'./static/data/0912_view.csv',encoding='utf-8')
    data = data[data['CarId'] == CarID]
    dta = data[(data['UTC'] >= StartTime) & (data['UTC'] <= EndTime)]
    car = []
    for i in range(0,len(dta)):
        car.append({'lat':dta.iloc[i,2],'lng':dta.iloc[i,3],'name':dta.iloc[i,0],'UTC':dta.iloc[i,1]})
    return render(request, 'Dynamic.html', {"aa": car})

def fx(request):
    webbrowser.open("http://localhost:8000/relay5")
    return render(request,'map.html')

def fx1(request):
    return render(request,'index_fx.html')