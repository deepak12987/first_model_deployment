from django.http import HttpResponse
from django.shortcuts import render
import pickle
loaded_model = pickle.load(open("model1.sav","rb"))
def home(request):
    return render(request,"main.html")

def pred(request):
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    bmi = request.POST.get("bmi")
    smoker = request.POST.get("smoke")
    no_child = request.POST.get("no_childrens")
    region = request.POST.get("region")
    if sex == "" or age == "" or bmi == "" or smoker == "" or no_child == "" or region == "":
        return render(request,"main.html")
    else:
        if sex == "male":
            sex = 1
        else:
            sex = 0
        if smoker == "yes":
            smoker = 1
        else:
            smoker = 0
        if region == "northwest":
            a,b,c = 1,0,0
        elif region == "southeast":
            a,b,c = 0,1,0
        elif region == "southwest":
            a,b,c = 0,0,1
        else:
            a,b,c = 0,0,0
        s = loaded_model.predict([[int(age),float(bmi),int(no_child),sex,smoker,a,b,c]])
        params = {"predicted":s[0]}
        return render(request,"output.html",params)
