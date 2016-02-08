# -*- coding: utf-8 -*-
# try something like

@auth.requires_login()
def agenda():
    expte_id=False
    if len(request.args)>1 and request.args[0]!='new':
        record = db.agenda(request.args(2,cast=int))
        if record:
            expte_id=record.expediente_id
    maxtextlengths={'db.agenda.vencimiento':15,
            'db.agenda.titulo':60,
            'db.agenda.texto':50}
    grid = SQLFORM.grid(db.agenda.created_by==auth.user.id,
                        fields=[db.agenda.vencimiento,db.agenda.titulo,db.agenda.texto,db.agenda.estado,db.agenda.prioridad],
                        maxtextlengths=maxtextlengths,
                        maxtextlength=70,
                        advanced_search=False,
                        user_signature=False,
                        exportclasses=myexport)
    return locals()

@auth.requires_login()
def calendar():
    rows=db(db.agenda.created_by==auth.user.id).select()
    return dict(rows=rows)

@auth.requires_login()
def agenda_edit():
    record = db.agenda(request.args(0,cast=int)) or redirect(URL('calendar'))
    expte_id=record.expediente_id
    form = SQLFORM(db.agenda,record).process()
    return locals()
