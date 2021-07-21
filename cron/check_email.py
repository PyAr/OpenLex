#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


def send_reminder(agenda):
    failed = 0
    user = agenda.created_by
    user_info = db(db.auth_user.id == user).select(db.auth_user.first_name, db.auth_user.email).first()
    context = dict(user_info=user_info, agenda=agenda)
    message = response.render('message.html', context)
    while failed < 4:
        if mail.send(to=user_info.email,
                        subject='None',
                        message=message):
            return db.commit()
        else:
            failed = failed + 1


def daily_check_email():
    reminder_lst = ["O", "TW", "TH"]
    today = datetime.datetime.now()
    agenda = db(db.agenda.vencimiento != None).select(db.agenda.vencimiento, db.agenda.recordatorio, db.agenda.titulo)
    for agenda_single in agenda:
        if agenda_single.recordatorio != "S" :
            reminder_id = [(n+1) for n, i in enumerate(reminder_lst) if agenda_single.recordatorio == i]
            vencimientos = (agenda_single.vencimiento - today).days
            if (vencimientos == reminder_id[0]):
                send_reminder(agenda_single)


daily_check_email()
