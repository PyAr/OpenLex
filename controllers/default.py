# -*- coding: utf-8 -*-
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."

#########################################################################
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user:
        redirect(URL('dashboard', 'view'))
    else:
        response.flash = T("Bienvenido a OpenLex")
        response.title = T("OpenLex")
        content = T(u'Sistema para abogados y estudios jurídicos')
        message = T('¡Bienvenido! Pruébelo ya mismo.')
        features = [{'img': 'feature-easy.png',
                     'alt': T('Intuitivo y muy fácil de usar, Ud. estára trabajando en sus expedientes inmediatamente. ')},
                    {'img': 'feature-responsive.png',
                     'alt': T('Acceso total desde cualquier parte con conexión Internet. Podrá acceder desde todos sus dispositivos, computadoras o móviles')},
                    {'img': 'feature-secure.png',
                     'alt': T('Tendrá sus datos en la seguridad absoluta de nuestros servidores. ¡Olvídese de las copias de seguridad!')},
                    {'img': 'feature-fast.png',
                     'alt': T('Rápido de usar y veloz para empezar. Ahórrese el tiempo para instalar y configurar su software. Úselo ya mismo')}]
        if not request.is_local:
            features.append(
                   {'img': ' ',
                    'alt': T('Para acceder al usuario demo ingrese con el correo: "prueba@prueba.com" y su contraseña: "password"')})
        return dict(message=message, features=features)


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
