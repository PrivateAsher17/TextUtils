# Made by - Ashwani
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contacts.html')

def analyze(request):
    djtext = request.POST.get('data','default')
    removepunc = request.POST.get('removepunc','default')
    fullcaps = request.POST.get('fullcaps','default')
    new_line_char_remover = request.POST.get('new_line_char_remover','default')
    space_remover = request.POST.get('space_remover','default')
    char_counter = request.POST.get('char_counter','default')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for text in djtext:
            if text not in punctuations:
                analyzed = analyzed + text
        params = {
            'purpose':'remove_punctuations',
            'analyzed_text':analyzed
        }
        djtext = analyzed

    if (fullcaps=='on'):
        capital = djtext.upper()
        params = {
            'purpose':'capitalize',
            'analyzed_text':capital
        }
        djtext = capital

    if (new_line_char_remover=='on'):
        analyzed = ''
        for text in djtext:
            if text != '\n' and text != '\r':
                analyzed = analyzed + text
        params = {
            'purpose':'new_line_char_remover',
            'analyzed_text':analyzed
        }
        djtext = analyzed

    if (space_remover=='on'):
        analyzed = ''
        for index,text in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + text
        params = {
            'purpose':'space_remover',
            'analyzed_text':analyzed
        }
        djtext = analyzed

    if (char_counter=='on'):
        analyzed = 0
        for text in djtext:
            if text!=' ':
                analyzed = analyzed + 1
        params = {
            'purpose':'space_remover',
            'analyzed_text':analyzed
        }
        djtext = analyzed

    if(removepunc != 'on' and fullcaps!='on' and new_line_char_remover!='on' and space_remover!='on' and char_counter!='on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)