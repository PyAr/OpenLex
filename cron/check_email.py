#!/usr/bin/env python
# -*- coding: utf-8 -*-


def send_reminder(agenda):
    failed = 0
    user = agenda.created_by
    user_info = db(db.auth_user.id == user).select(db.auth_user.first_name, db.auth_user.email).first()
    context = dict(user_info=user_info, agenda=agenda)
    message = response.render('message.html', context)
    while failed < myconf.take('email_var.error'):
        if mail.send(to=user_info.email,
                        subject='Recordatorio de Openlex',
                        message=message):
            return db.commit()
        else:
            failed = failed + 1


def daily_check_email():
    today = request.now
    agenda = db(db.agenda.vencimiento != None).select(db.agenda.vencimiento, db.agenda.recordatorio, db.agenda.titulo, db.agenda.created_by)
    for agenda_single in agenda:
        if agenda_single.recordatorio != 0 :
            reminder_id = agenda_single.recordatorio
            vencimientos = (agenda_single.vencimiento - today).days
            if (vencimientos == int(reminder_id)):
                send_reminder(agenda_single)


if __name__ == "__main__":
    daily_check_email()
