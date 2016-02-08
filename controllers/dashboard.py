# -*- coding: utf-8 -*-
# este módulo intenta definir un panel de control
# o dashboard
# se incluyen: una agenda con un vista general de todo el mes
# un listado de las tareas que vencen esta semana o que están vencidas
# mostrando un resumen de la tarea junto con accesos al expediente

def index(): 
    rows=db(db.expediente).select(db.expediente.ALL, limitby=[0,10], orderby=~db.expediente.changed_at)
    return locals()
