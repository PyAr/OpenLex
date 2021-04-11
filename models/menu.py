# -*- coding: utf-8 -*-
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."


#########################################################################
# Customize your APP title, subtitle and menus here
#########################################################################

DEVELOPMENT_MENU = False

response.logo = A(B(SPAN('Open'), 'Lex'), XML('&trade;&nbsp;'),
                  _class="navbar-brand",  # _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = 'Sistema de gestión para estudios jurídicos'

# read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

# your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
# this is the main application menu add/remove items as required
#########################################################################

'''response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Expedientes'),False,URL('expedientes','index')),
    (T('Contactos'),False,URL('contactos','index')),
    (T('Calendario'),False,URL('agenda','calendar')),
    (T('Agenda'),False,URL('agenda','agenda')),
    (T('Juzgados'),False,URL('other_tables','juzgados')),
    (T('Tablas'),False, '#', [
            (T('Tipos de proceso'),False,URL('other_tables','tipoproceso')),
            (T('Instancias'),False,URL('other_tables','instancias')),
            (T('Fueros'),False,URL('other_tables','fueros'))]),
]
'''

if not auth.user:
    response.menu = [
        (T('Home'), False, URL('default', 'index'), [])]
else:
    response.menu = [
        (T('Home'), False, URL('dashboard', 'view'), []),
        (T('Expedientes'), False, URL('expedientes', 'index')),
        (T('Contactos'), False, URL('contactos', 'index')),
        (T('Calendario'), False, URL('agenda', 'calendar')),
        (T('Agenda'), False, URL('agenda', 'agenda')),
        (T('Juzgados'), False, URL('other_tables', 'juzgados')),
    ]
    if auth.has_membership(user_id=auth.user.id, role='admin'):
        response.menu.append((T('Tablas'), False, '#', [
            (T('Tipos de proceso'), False, URL('other_tables', 'tipoproceso')),
            (T('Instancias'), False, URL('other_tables', 'instancias')),
            (T('Fueros'), False, URL('other_tables', 'fueros'))
            (T('Jurisdicciones'), False, URL('other_tables', 'jurisdicciones'))
        ]))


# fuerzo a la aplicación a usar el unico lenguage disponible por ahora
T.force('es')

#########################################################################
# provide shortcuts for development. remove in production
#########################################################################


def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [(T('My Sites'),
                       False,
                       URL('admin',
                           'default',
                           'site')),
                      (T('This App'),
                       False,
                       '#',
                       [(T('Design'),
                         False,
                         URL('admin',
                             'default',
                             'design/%s' % app)),
                          LI(_class="divider"),
                          (T('Controller'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/controllers/%s.py' % (app,
                                                              ctr))),
                          (T('View'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/views/%s' % (app,
                                                     response.view))),
                          (T('DB Model'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/models/db.py' % app)),
                          (T('Menu Model'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/models/menu.py' % app)),
                          (T('Config.ini'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/private/appconfig.ini' % app)),
                          (T('Layout'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/views/layout.html' % app)),
                          (T('Stylesheet'),
                           False,
                           URL('admin',
                               'default',
                               'edit/%s/static/css/web2py-bootstrap3.css' % app)),
                          (T('Database'),
                           False,
                           URL(app,
                               'appadmin',
                               'index')),
                          (T('Errors'),
                           False,
                           URL('admin',
                               'default',
                               'errors/' + app)),
                          (T('About'),
                           False,
                           URL('admin',
                               'default',
                               'about/' + app)),
                        ]),
                      ('web2py.com',
                       False,
                       '#',
                       [(T('Download'),
                         False,
                         'http://www.web2py.com/examples/default/download'),
                        (T('Support'),
                           False,
                           'http://www.web2py.com/examples/default/support'),
                           (T('Demo'),
                            False,
                            'http://web2py.com/demo_admin'),
                           (T('Quick Examples'),
                            False,
                            'http://web2py.com/examples/default/examples'),
                           (T('FAQ'),
                            False,
                            'http://web2py.com/AlterEgo'),
                           (T('Videos'),
                            False,
                            'http://www.web2py.com/examples/default/videos/'),
                           (T('Free Applications'),
                            False,
                            'http://web2py.com/appliances'),
                           (T('Plugins'),
                            False,
                            'http://web2py.com/plugins'),
                           (T('Recipes'),
                            False,
                            'http://web2pyslices.com/'),
                        ]),
                      (T('Documentation'),
                       False,
                       '#',
                       [(T('Online book'),
                         False,
                         'http://www.web2py.com/book'),
                          LI(_class="divider"),
                          (T('Preface'),
                           False,
                           'http://www.web2py.com/book/default/chapter/00'),
                          (T('Introduction'),
                           False,
                           'http://www.web2py.com/book/default/chapter/01'),
                          (T('Python'),
                           False,
                           'http://www.web2py.com/book/default/chapter/02'),
                          (T('Overview'),
                           False,
                           'http://www.web2py.com/book/default/chapter/03'),
                          (T('The Core'),
                           False,
                           'http://www.web2py.com/book/default/chapter/04'),
                          (T('The Views'),
                           False,
                           'http://www.web2py.com/book/default/chapter/05'),
                          (T('Database'),
                           False,
                           'http://www.web2py.com/book/default/chapter/06'),
                          (T('Forms and Validators'),
                           False,
                           'http://www.web2py.com/book/default/chapter/07'),
                          (T('Email and SMS'),
                           False,
                           'http://www.web2py.com/book/default/chapter/08'),
                          (T('Access Control'),
                           False,
                           'http://www.web2py.com/book/default/chapter/09'),
                          (T('Services'),
                           False,
                           'http://www.web2py.com/book/default/chapter/10'),
                          (T('Ajax Recipes'),
                           False,
                           'http://www.web2py.com/book/default/chapter/11'),
                          (T('Components and Plugins'),
                           False,
                           'http://www.web2py.com/book/default/chapter/12'),
                          (T('Deployment Recipes'),
                           False,
                           'http://www.web2py.com/book/default/chapter/13'),
                          (T('Other Recipes'),
                           False,
                           'http://www.web2py.com/book/default/chapter/14'),
                          (T('Helping web2py'),
                           False,
                           'http://www.web2py.com/book/default/chapter/15'),
                          (T("Buy web2py's book"),
                           False,
                           'http://stores.lulu.com/web2py'),
                        ]),
                      (T('Community'),
                       False,
                       None,
                       [(T('Groups'),
                         False,
                         'http://www.web2py.com/examples/default/usergroups'),
                          (T('Twitter'),
                           False,
                           'http://twitter.com/web2py'),
                          (T('Live Chat'),
                           False,
                           'http://webchat.freenode.net/?channels=web2py'),
                        ]),
                
# sistema de consulta web 
from tkinter import *
import webbrowser

root = Tk()

new = 1
url = "https://www.google.com"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(root, text = "This opens Google",command=openweb)
Btn.pack()

root.mainloop()
# end
if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
