from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def notice(req):
    notice1 = "Your practical exams will be begin soon stay tuned for updates."
    notice2 = "Kindly clear your fees in order to give your exams."
    context = {
        "n1": notice1,
        "n2": notice2,
    }
    template = loader.get_template('notice.html')
    res = template.render(context, req)
    return HttpResponse(res)

def admitcard(req):
    template = loader.get_template('admitcard.html')
    res = template.render()
    return HttpResponse(res)

def result(req):
    template = loader.get_template('result.html')
    res = template.render()
    return HttpResponse(res)
