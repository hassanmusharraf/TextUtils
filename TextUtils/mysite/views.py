# Created by Hassan :)
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {"purpose": "Enter text below"}
    return render(request, "index.html", params)

def analyze(request):
    # get text
    djtext = request.POST.get("text", "default")

    removepunc = request.POST.get("removepunc", "off")
    uppercase = request.POST.get("uppercase", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charcount = request.POST.get("charcount", "off")
    c = 0 #for counting character

    if removepunc == "on":
        analyzed = ''
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
        djtext=analyzed

    if uppercase == "on":
        analyzed = ""
        analyzed = djtext.upper()
        params = {"purpose": "UPPERCASE", "analyzed_text": analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "New line remover", "analyzed_text": analyzed}
        djtext=analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra Space remover", "analyzed_text": analyzed}
        djtext=analyzed

    if charcount == "on":
        for char in djtext:
            if char.isalpha():
                c += 1
        params = {"purpose": "Character Counter", "analyzed_text": c}         

    if (removepunc!='on'and extraspaceremover!='on'and charcount!='on'and newlineremover!='on'and uppercase!='on'):
        params = {"analyzed_text": "Error"}

    return render(request, "analyze.html", params)
