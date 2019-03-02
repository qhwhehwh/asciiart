from django.shortcuts import render
from art import *

def home(request):
    text1=art("random")
    return render(request,'home.html',{'text1':text1})
def good(request):
    text2=request.GET['something']
    text3=text2art(text2)
    text4=text2art(text2,font='rnd-small')
    text5=text2art(text2,font='rnd-medium')
    text6=text2art(text2,font='rnd-large')
    text7=text2art(text2,font='rnd-xlarge')
    return render(request,'good.html',{'text3':text3,'text4':text4,'text5':text5,'text6':text6,'text7':text7})