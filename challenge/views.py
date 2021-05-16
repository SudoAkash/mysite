from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

month_chall={
    "jan":"Django",
    "feb":"React",
    "mar":"Node js",
    "apr":"Angular",
    "may":"Typescript",
    "june":"Graph Ql",
    "july":"Mongo Db",
    "aug":" Express js",
    "sept":"Vue js",
    "oct":"Docker",
    "nov":"Kubruntus",
    "dec":"Flutter"
    
}
# Create your views here.
def monthly_challenge_num(request,month):
    months=list(month_chall.keys())
    if month > len(months):
        return HttpResponseNotFound("Invaild Month")
    redirect_month=months[month-1]
    return HttpResponseRedirect("/challenge/" +redirect_month)

def monthly_challenge(request,month):
   try:
       challenge_text=month_chall[month]
       return HttpResponse(challenge_text)
   except :
       return HttpResponseNotFound("Page Not found")

