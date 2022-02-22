from django.shortcuts import render
from django.http import HttpResponse

news_list = {"2022":
                {"10":
                        {"20":
["Кабмін призначив Капінуса на посаду голови Пенсійного фонду",
"Фонд держмайна виставив на продаж спиртзавод за 31 мільйон",
"На Гаванському мосту у Києві загорівся автомобіль"],

"21":["Сьогодні увесь світ відзначає Міжнародний день рідної мови",
"У Київській ОДА хочуть зупинити ремонт онкодиспансеру."]
},
"11":
{"30":
["Створено першу в історії молекулу-транзистор",
"Компанія Renault у 2022 році готує новинки"]
}
},
"2021":
{"5":
{"17":
["Як знизити цукор у крові: найкращі ягоди при діабеті 2-го типу",
"Україна звернулась до Радбезу ООН щодо гарантування безпеки"]
}
}
}


def news(request,rik=0,mis=0,den=0):
    a=""
    b=""
    c=0
    g=0
    if (rik==0):
        for x in news_list:
            for x2 in news_list[x]:
                for x3 in news_list[x][x2]:
                    b=b+x3+"."+x2+"."+x+":<br>"
                    while c<len(news_list[x][x2][x3]):
                        b=b+"<li>"+news_list[x][x2][x3][c]+"</li>"
                        c=c+1
                    c=0
        return HttpResponse(b)
    if (mis == 0):
        for x in news_list:
            if (x==str(rik)):
                for x2 in news_list[x]:
                    for x3 in news_list[x][x2]:
                        b=b+x3+"."+x2+"."+x+":<br>"
                        while c<len(news_list[x][x2][x3]):
                            b=b+"<li>"+news_list[x][x2][x3][c]+"</li>"
                            c=c+1
                        c=0
        return HttpResponse(b)
    if (den == 0):
        for x in news_list:
            if (x==str(rik)):
                for x2 in news_list[x]:
                    if (x2 == str(mis)):
                        for x3 in news_list[x][x2]:
                            b=b+x3+"."+x2+"."+x+":<br>"
                            while c<len(news_list[x][x2][x3]):
                                b=b+"<li>"+news_list[x][x2][x3][c]+"</li>"
                                c=c+1
                            c=0
        return HttpResponse(b)
    if (den != 0):
        for x in news_list:
            if (x==str(rik)):
                for x2 in news_list[x]:
                    if (x2 == str(mis)):
                        for x3 in news_list[x][x2]:
                            if (x3 == str(den)):
                                b = b + x3 + "." + x2 + "." + x + ":<br>"
                                for x4 in news_list[x][x2][x3]:
                                    id = request.GET.get("id","-1")
                                    if (id!="-1" and int(id)<=len(news_list[x][x2][x3])):
                                        b = b + "<li>" + news_list[x][x2][x3][int(id)-1] + "</li>"
                                        return HttpResponse(b)
                                    else:
                                        while c < len(news_list[x][x2][x3]):
                                            b = b + "<li>" + news_list[x][x2][x3][c] + "</li>"
                                            c = c + 1
                                        return HttpResponse(b)


