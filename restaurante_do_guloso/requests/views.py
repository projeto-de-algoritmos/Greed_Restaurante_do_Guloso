from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from random import randint
import heapq as hp

class motoboy:
    def __init__(self):
        self.qtd = 0
        # ex.: [(10:30, [a, c, e]), (7:00, [b])]
        self.compatibility = []

heapTask = []

def addTask(tasks, inicio = 600, final = 900, tamanhoMin = 10, tamanhoMax = 60):
    inicioTask = randint(inicio, final)
    tamanhoTask = randint(tamanhoMin, tamanhoMax)
    hp.heappush(tasks, (inicioTask, inicioTask + tamanhoTask))
    return tasks

def randomizeTasks(tasks, qtd = 5):
    for _ in range(qtd):
            tasks = addTask(tasks)
    return tasks

def intervalPartitioning (motoboys, tasks):
    for task in tasks:
        if motoboys.compatibility and motoboys.compatibility[0][0] <= task[0]:
            motoboys.compatibility[0][1].append(task)
            motoboys.compatibility[0] = (task[1], motoboys.compatibility[0][1])
            hp.heapify(motoboys.compatibility)
        else:
            motoboys.qtd += 1
            hp.heappush(motoboys.compatibility, (task[1], [task]))

def menu(request):
    global heapTask 
    motoboys = motoboy()

    if request.GET.__contains__('qtd'):
        try:
            qtd = int(request.GET['qtd'])
            #  inicio = int(request.GET['inicio'])
            #  final = int(request.GET['final'])
            #  tamanhoMin = int(request.GET['tamanhoMin'])
            #  tamanhoMax = int(request.GET['tamanhoMax'])
            heapTask = randomizeTasks([], qtd)
            intervalPartitioning(motoboys, heapTask)
        except:
            ...
    elif request.GET.__contains__('plus'):
        heapTask = addTask(heapTask);
        intervalPartitioning(motoboys, heapTask)
    
    return render(request, 'menu.html', {'motoboys': motoboys.compatibility, 'qtd_motoboys': motoboys.qtd, 'qtd_tasks': len(heapTask)})
