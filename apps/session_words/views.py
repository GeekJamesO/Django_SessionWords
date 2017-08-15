# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    try:
        request.session['words']
    except Exception as e:
        request.session['words'] = [ ]

    return render(request, "session_words/index.html")

def add_words(request):
    thisWord = request.POST['txtInput']
    if (thisWord == ""):
        thisWord = "<-blank->"
    ClassBigFont = 'notSet'
    thisColor = request.POST['ChooseColor']
    if ('BigFont' in request.POST.keys()):
        ClassBigFont = " bigFont"
    else:
        ClassBigFont = " "
    compoundString = "<div class='" + thisColor + ClassBigFont + "'>" + thisWord + "</div>"
    try:
        # print "Appending..  '" + compoundString + "'"
        request.session['words'].append(compoundString)
        request.session.modified = True
    except Exception as e:
        print "exception in saving word.", e.message
        request.session['words'] = [ compoundString ]
    return index(request)

def clear(request):
    del request.session['words']
    return redirect("/")
