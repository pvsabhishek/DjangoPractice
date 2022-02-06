# I have created This file - chiku
from django.http import HttpResponse
from django.shortcuts import render

# CODE FOR VIDEO 6
# def index(request):
#     return HttpResponse('''<h1>hello chiku bhai</h1>  <a href = "https://www.google.co.in/"> google Site</a>''')
#
# def about(request):
#     return HttpResponse("This Page is about page")


# CODE FOR VIDEO 7
# def index(req):
#     return render(req, 'index.html')
#
#
#     # return HttpResponse("Home")
#
# def removepunc(req):
#     #GET THE TEXT
#     djtext = req.GET.get('text', 'default')
#     print(djtext)
#     #ANALYZE THE TEXT
#     return HttpResponse("remove punc <a href = '/'>back</a>")
#
# def capfirst(req):
#     return HttpResponse("capitalizefirst <a href = '/'>back</a>")
#
# def newlineremove(req):
#     return HttpResponse("newlineremove <a href = '/'>back</a>")
#
# def spaceremove(req):
#     return HttpResponse("spaceremove <a href = '/'>back</a>")
#
# def charcount(req):
#     return HttpResponse("charcount <a href = '/'>back</a>")

# CODE FOR VIDEO 11
def index(req):
    return render(req, 'index.html')


    # return HttpResponse("Home")
#CODE FOR VIDEO 11
def ex1(req):
    s = '''<h2>Navigator Bar</h2>
    <a href = "https://www.google.co.in/"</a>Google<br>
    <a href = "https://www.youtube.com/"</a>YouTube<br>
    '''
    return HttpResponse(s)

def analyze(req):
    #GET THE TEXT
    djtext = req.GET.get('text', 'default')
    removepunc = req.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        #ANALYZE THE TEXT
        return render(req, 'analyze.html', params)
    else:
        return HttpResponse("ERROR")
