# -*- coding: utf-8 -*-
# este módulo define un panel de control o dashboard
# se incluyen: una agenda con un vista general de todo el mes
# un listado de las tareas que vencen esta semana o que están vencidas
# mostrando un resumen de la tarea junto con accesos al expediente
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."
import datetime

@auth.requires_login()
def view():
    expte_grid = SQLFORM.grid(
        db.expediente.created_by == auth.user.id,
        fields=[
            db.expediente.numero,
            db.expediente.caratula],
        orderby=~db.expediente.changed_at,
        paginate=20,
        maxtextlength=40,
        searchable=False,
        sortable=True,
        deletable=False,
        editable=False,
        details=False,
        create=False,
        exportclasses=myexport)
    query_agenda = (db.agenda.created_by == auth.user.id)
    query_agenda &= (db.agenda.estado == 'P')
    ahora = request.now
    query_semana = query_agenda & (db.agenda.vencimiento > ahora)
    query_vencidos = query_agenda & (
        db.agenda.vencimiento < ahora)
    ahora += datetime.timedelta(7)
    if not request.is_local:
        update_task_week(ahora)  # Para mantener visible la agenda en tareas urgentes en la version de testeo online
    query_semana &= (db.agenda.vencimiento < ahora)

    semanal_grid = SQLFORM.grid(
        query_semana,
        fields=[
            db.agenda.titulo,
            db.agenda.vencimiento,
            db.agenda.prioridad,
            db.agenda.estado,
            db.agenda.expediente_id],
        orderby=db.agenda.vencimiento,
        paginate=9,
        maxtextlength=40,
        searchable=False,
        sortable=True,
        deletable=False,
        editable=False,
        details=False,
        create=False,
        exportclasses=myexport)
    vencidos_grid = SQLFORM.grid(
        query_vencidos,
        fields=[
            db.agenda.titulo,
            db.agenda.vencimiento,
            db.agenda.prioridad,
            db.agenda.estado,
            db.agenda.expediente_id],
        orderby=db.agenda.vencimiento,
        paginate=9,
        maxtextlength=40,
        searchable=False,
        sortable=True,
        deletable=False,
        editable=False,
        details=False,
        create=False,
        exportclasses=myexport)

    message = T("Bienvenido, %s %s") % (
        auth.user.first_name, auth.user.last_name)
    modules = [
        {
            'url': URL(
                'expedientes', 'index'), 'img': 'expedientes.png', 'alt': T('Expedientes')}, {
            'url': URL(
                'agenda', 'calendar'), 'img': 'calendario.png', 'alt': T('Calendario')}, {
            'url': URL(
                'contactos', 'index'), 'img': 'personas.png', 'alt': T('Contactos')}, ]
    if auth.has_membership(user_id=auth.user.id, role='admin'):
        modules.append({'url': URL('other_tables', 'juzgados'),
                        'img': 'juzgados.png', 'alt': T('Oficinas judiciales')})
    admin = db.auth_group.role.validate('admin')
    if None in admin:
        auto_assign_role_admin()
    return locals()


def auto_assign_role_admin():
    id_grupo = auth.add_group('admin', 'administrador de la aplicacion')
    auth.add_membership(id_grupo)
    db.commit()
    
    
def update_task_week(ahora):
    db(db.agenda.id == myconf.take('test-version.update')).update(vencimiento=ahora)   
