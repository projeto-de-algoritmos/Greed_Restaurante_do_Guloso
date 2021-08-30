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

"""Randomiza tarefas
Args:
    qtd (int)        : Quantidade de tarefas
    inicio (int)     : Inicio do período de entregas
    final (int)      : Final do período de entregas
    tamanhoMin (int) : Tamanho min da entrega
    tamanhoMax (int) : Tamanhp max da entrega

Returns:
    list: lista de task organizadas
"""
def randomizeTasks(qtd: 5, inicio = 600, final = 900, tamanhoMin = 10, tamanhoMax = 60):
    tasks = []
    for _ in range(qtd):
        inicioTask = randint(inicio, final)
        tamanhoTask = randint(tamanhoMin, tamanhoMax)
        hp.heappush(tasks, (inicioTask, inicioTask + tamanhoTask))
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
    motoboys = motoboy()
    intervalPartitioning(motoboys, randomizeTasks(5))
    return HttpResponse(f"{motoboys.qtd} motoboys: {motoboys.compatibility}")
