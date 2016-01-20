# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

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
    return dict(message=T('Bienvenido!'),content=content)

@auth.requires_login()
def admin_expedientes():
    grid = SQLFORM.smartgrid(db.expediente,
                             fields=[db.expediente.numero,
                                     db.expediente.caratula,
                                     db.expediente.juzgado_id.
                                    db.movimiento.titulo,
                                    db.movimiento.procesal,
                                    db.agenda.vencimiento,
                                    db.agenda.titulo],
                             constraints={'created_by':auth.user.id},
                             linked_tables=['movimiento','agenda'])
    return locals()

@auth.requires_login()
def admin_juzgados():
    grid = SQLFORM.grid(db.juzgado,user_signature=False)
    return locals()

@auth.requires_login()
def admin_personas():
    grid = SQLFORM.grid(db.persona.created_by==auth.user.id,user_signature=False)
    return locals()

@auth.requires_login()
def fueros():
    grid = SQLFORM.grid(db.fuero)
    return locals()

@auth.requires_login()
def instancias():
    grid = SQLFORM.grid(db.instancia)
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
