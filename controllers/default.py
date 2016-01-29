# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

'''export=dict(csv_with_hidden_cols=(ExporterCSV, 'CSV (columnas ocultas)'),
csv=(ExporterCSV, 'CSV'),
xml=(ExporterXML, 'XML'),
html=(ExporterHTML, 'HTML'),
tsv_with_hidden_cols=(ExporterTSV, 'TSV (Compatible con Excel, columnas ocultas)'),
tsv=(ExporterTSV, 'TSV (Compatible con excel)'))'''

myexport=dict(csv_with_hidden_cols=False,
            csv=False,
            xml=False,
            html=False,
            tsv_with_hidden_cols=False,
            tsv=False,
            json=False)

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Bienvenido a pyDoctor")
    response.title = T("pyDoctor")
    content=T(u'Sistema para abogados y estudios jurídicos realizado por María Andrea Vignau')
    modules=[{'url':URL('default','admin_expedientes'),'img':'expedientes.png','alt':T('Administración de expedientes')},
             {'url':URL('default','agenda'),'img':'calendario.png','alt':T('Agenda de vencimientos')},
             {'url':URL('default','admin_personas'),'img':'personas.png','alt':T('Contactos')},
             {'url':URL('default','admin_juzgados'),'img':'juzgados.png','alt':T('Oficinas judiciales')}
    ]
    return dict(message=T('Bienvenido!'),modules=modules)

@auth.requires_login()
def agenda():
    grid = SQLFORM.grid(db.agenda.created_by==auth.user.id,user_signature=False,exportclasses=myexport)
    return locals()

@auth.requires_login()
def calendar():
    '''
    rows
    row.f_title
    row.f_start_time
    row.f_end_time
    row.id'''
    rows=db(db.agenda.created_by==auth.user.id).select()
    return dict(rows=rows)


@auth.requires_login()
def admin_expedientes():

    ar = request.args # save typing


    grid = SQLFORM.smartgrid(db.expediente,
                             fields=[db.expediente.numero,
                                     db.expediente.caratula,
                                     db.expediente.juzgado_id.
                                    db.movimiento.titulo,
                                    db.movimiento.estado,
                                    db.agenda.vencimiento,
                                    db.agenda.titulo,
                                    db.parte.persona_id,
                                    db.parte.caracter],
                             constraints={'created_by':auth.user.id},
                             linked_tables=['movimiento','agenda','parte'],
                            buttons_placement = 'right',
                            #oncreate=dict(movimiento=[create_movimiento]),
                            #onupdate=dict(movimiento=[update_movimiento,]),
                             #oncreate=oncreate,onupdate=onupdate,
                            exportclasses=myexport)
    return locals()

@auth.requires_login()
def create_movimiento(form):
    response.flash = T("create_movimiento")
    print 'create!'
    print form.vars

@auth.requires_login()
def update_movimiento(form):
    response.flash = T("update_movimiento")
    print 'update!'
    print form.vars

@auth.requires_login()
def admin_juzgados():
    db.juzgado.fuero_id.widget._class='form-control string'
    grid = SQLFORM.grid(db.juzgado,user_signature=False,exportclasses=myexport)
    return locals()

@auth.requires_login()
def admin_personas():
    grid = SQLFORM.grid(db.persona.created_by==auth.user.id,user_signature=False,exportclasses=myexport)
    return locals()

@auth.requires_login()
def fueros():
    grid = SQLFORM.grid(db.fuero,exportclasses=myexport)
    return locals()

@auth.requires_login()
def instancias():
    grid = SQLFORM.grid(db.instancia,exportclasses=myexport)
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())
