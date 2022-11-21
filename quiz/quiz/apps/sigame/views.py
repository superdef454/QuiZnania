from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Section, Subject, Question
import urllib

def home(request):
    # Выбор раздела
    sections = Section.objects.filter(view=True).order_by('title')
    out = {
        'sections' : sections,
    }
    return render(request, 'sigame/home.html', out)

def type_selection(request, section):
    section_item = Section.objects.get(title=section)
    subjects = section_item.subject_set.filter(view=True).order_by('type')
    types = []
    for item in subjects:
        if item.type not in types:
            types.append(item.type)
    out = {
        'section' : section,
        'types' : types,
    }
    return render(request, 'sigame/type_selection.html', out)

def round_selection(request, section, type):
    section_item = Section.objects.get(title=section)
    subjects = section_item.subject_set.filter(view=True, type = type)
    if len(subjects) > 0:
        round = [subjects[0].round]
        for item in subjects:
            if item.round > round[-1]:
                round.append(item.round)
    else:
        round = []
    out = {
        'section' : section,
        'type' : type,
        'round' : round,
    }
    return render(request, 'sigame/round_selection.html', out)

def game(request, section, type, round = 1):
    if request.method == "POST":
        count_team = request.POST.get('count_team')
        if count_team != '6' and count_team != '5' and count_team != '4' and count_team != '3' and count_team != '2':
            pass
        else:
            request.session['teams'] = count_team
    section_item = Section.objects.get(title=section)
    subjects = section_item.subject_set.filter(view=True, type = type, round=round)
    if len(subjects) == 0:
        return HttpResponse(end(request))
    sq = []
    json = []
    for a in subjects:
        q = a.question_set.all()
        sq.append({
            "subject" : a,
            'questions' : q,
        })
        jsonadd = {
            "subject" : a.title,
            'questions' : []
        }
        qs = []
        for qq in q:
            qs.append({
                'question' : qq.description,
                'cost' : qq.cost,
                'answer' : qq.answer,
                'id' : qq.id,
            })
        jsonadd['questions'] = qs
        json.append(jsonadd)
    if "score" in request.COOKIES:
        score = urllib.parse.unquote(request.COOKIES.get("score")).split(' ')
        for i in range(1, len(score)):
            # print(str(i) + str(score[i-1]))
            request.session['team{0}'.format(i)] = score[i-1]
    # request.set_cookie('score', x, max_age = None)
    team = int(request.session.get('teams', 6)) # Переменная с количеством команд
    if team < 2:
        team = 2
    if team > 6:
        team = 6
    teams = []
    for i in range(1, team + 1):
        add = {
            'name' : i,
            'points' : request.session.get('team{0}'.format(i), 0),
        }
        teams.append(add)
    # plus = request.session.get('team{0}'.format(1), 0)
    # request.session['team1'] = plus + 100
    # teams[0]['points'] = request.session.get('team{0}'.format(1), 0)
    # request.session['team5'] = 45600
    # teams[4]['points'] = 45600
    out = {
        'sq' : sq,
        'type' : type,
        'round' : round,
        'section' : section,
        'next' : round + 1,
        'teams' : teams,
        'json' : json,
    }
    return render(request, 'sigame/game.html', out)

def end(request):
    team = int(request.session.get('teams', 6)) # Переменная с количеством команд
    if team < 2:
        team = 2
    teams = []
    win = -1
    winteam = 0
    if "score" in request.COOKIES:
        score = urllib.parse.unquote(request.COOKIES.get("score")).split(' ')
        for i in range(1, len(score)):
            # print(str(i) + str(score[i-1]))
            request.session['team{0}'.format(i)] = score[i-1]
    for i in range(1, team + 1):
        add = {
            'name' : i,
            'points' : request.session.get('team{0}'.format(i), 0),
        }
        if int(add['points']) > win:
            win = int(add['points'])
            winteam = i
        teams.append(add)
    out = {
        'teams' : teams,
        'winteam' : winteam,
    }
    return render(request, 'sigame/end.html', out)

# def data_question(request):
#     """Передаёт вопрос и ответ на страницу"""
#     question = 1
#     pass
