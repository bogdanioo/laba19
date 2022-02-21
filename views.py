from django.shortcuts import render
from django.http import HttpResponse

ttable = [['Інформатика', 'Фізкультура', 'Література', 'Українська мова'],
['Інформатика', 'Математика', 'Література', 'Географія'],
['Фізкультура', 'Математика', 'Математика', 'Українська мова'],
['Математика', 'Інформатика', 'Література', 'Біологія'],
['Література', 'Математика', 'Інформатика', 'Фізкультура']]
def index(request):
    return HttpResponse("Hello!")
def monday(request):
    v = ""
    i = 0
    while i < len(ttable[0]):
        v=v+str(i+1)+". "+ttable[0][i]+"<br>"
        i += 1

    return HttpResponse("Понедельник:<br><br>"+v)
def tuesday(request):
    v = ""
    i = 0
    while i < len(ttable[1]):
        v = v + str(i + 1) + ". " + ttable[1][i] + "<br>"
        i += 1

    return HttpResponse("Вторник:<br><br>"+v)
def wednesday(request):
    v = ""
    i = 0
    while i < len(ttable[2]):
        v = v + str(i + 1) + ". " + ttable[2][i] + "<br>"
        i += 1

    return HttpResponse("Среда:<br><br>"+v)
def thursday(request):
    v = ""
    i = 0
    while i < len(ttable[3]):
        v = v + str(i + 1) + ". " + ttable[3][i] + "<br>"
        i += 1

    return HttpResponse("Четверг:<br><br>"+v)
def friday(request):
    v = ""
    i = 0
    while i < len(ttable[4]):
        v = v + str(i + 1) + ". " + ttable[4][i] + "<br>"
        i += 1

    return HttpResponse("Пятница:<br><br>"+v)
def saturday(request):
    return HttpResponse("Суббота:<br><br>Выходной!")
def sunday(request):
    return HttpResponse("Воскресенье:<br><br>Выходной!")
