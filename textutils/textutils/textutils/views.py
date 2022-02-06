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
# def ex1(req):
#     s = '''<h2>Navigator Bar</h2>
#     <a href = "https://www.google.co.in/"</a>Google<br>
#     <a href = "https://www.youtube.com/"</a>YouTube<br>
#     '''
#     return HttpResponse(s)

def analyze(req):
    #GET THE TEXT
    djtext = req.GET.get('text', 'default')

    #CHECK CHECKBOX VALUES
    removepunc = req.GET.get('removepunc', 'off')
    fullcaps = req.GET.get('fullcaps','off')
    newlineremover = req.GET.get('newlineremover','off')
    extraspaceremover = req.GET.get('extraspaceremover','off')
    charcount = req.GET.get('charcount','off')

    #CHECK WHICH CHECKBOX IS ON
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
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(req, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        return render(req, 'analyze.html', params)
    elif (charcount == 'on'):
        count = 0
        djtext1 = djtext.replace(" ", "")
        for x in djtext1:
            if x != "/n":
                count = count + 1
        params = {'work': 'TextAnalyzer', 'analyzed_text': count}
        return render(req, 'analyze.html.', params)
    else:
        return HttpResponse('Error')
