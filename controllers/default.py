# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
__author__=u"María Andrea Vignau <mavignau@gmail.com>"
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
    content=T(u'Sistema para abogados y estudios jurídicos')
    modules=None
    features=None
    if auth.user:
        message=T("Bienvenido a pyDoctor, %s %s")%(auth.user.first_name,auth.user.last_name)
        modules=[{'url':URL('default','admin_expedientes'),'img':'expedientes.png','alt':T('Administración de expedientes')},
                 {'url':URL('default','calendar'),'img':'calendario.png','alt':T('Calendario de vencimientos')},
                 {'url':URL('default','admin_personas'),'img':'personas.png','alt':T('Contactos')},
                 {'url':URL('default','admin_juzgados'),'img':'juzgados.png','alt':T('Oficinas judiciales')}
        ]
    else:
        message=T('¡Bienvenido! Pruébelo ya mismo.')
        features=[{'img':'feature-easy.png','alt':T('Intuitivo y muy fácil de usar, Ud. estára trabajando en sus expedientes inmediatamente. ')},
                 {'img':'feature-responsive.png','alt':T('Acceso total desde cualquier parte con conexión Internet. Podrá acceder desde todos sus dispositivos, computadoras o móviles')},
                 {'img':'feature-secure.png','alt':T('Tendrá sus datos en la seguridad absoluta de nuestros servidores. ¡Olvídese de las copias de seguridad!')},
                 {'img':'feature-fast.png','alt':T('Rápido de usar y veloz para empezar. Ahórrese el tiempo para instalar y configurar su software. Úselo ya mismo')}
        ]
    return dict(message=message,modules=modules,features=features)

@auth.requires_login()
def agenda():
    maxtextlengths={'db.agenda.vencimiento':15,
            'db.agenda.titulo':60,
            'db.agenda.texto':70}
    grid = SQLFORM.grid(db.agenda.created_by==auth.user.id,
                        fields=[db.agenda.vencimiento,db.agenda.titulo,db.agenda.texto,db.agenda.estado,db.agenda.prioridad],
                        headers={'db.agenda.vencimiento':'Vence el',
                            'db.agenda.titulo':'Titulo',
                            'db.agenda.texto':'Descripcion',
                            'db.agenda.estado':'E',
                            'db.agenda.prioridad':'P'},
                        maxtextlengths=maxtextlengths,maxtextlength=70,
                        user_signature=False,exportclasses=myexport)
    return locals()

@auth.requires_login()
def calendar():
    rows=db(db.agenda.created_by==auth.user.id).select()
    return dict(rows=rows)

@auth.requires_login()
def agenda_edit():
    record = db.agenda(request.args(0,cast=int)) or redirect(URL('calendario'))
    expte= crud.read(db.expediente,record.expediente_id)
    form = SQLFORM(db.agenda,record).process()
    return locals()


@auth.requires_login()
def admin_expedientes():
    maxtextlengths={'db.expediente.numero' : 15,
             'db.expediente.caratula':60,
             'db.expediente.juzgado_id':45,
            'db.movimiento.titulo':60,
            'db.movimiento.texto':70,
            'db.movimiento.estado':5,
            'db.agenda.vencimiento':15,
            'db.agenda.titulo':60,
            'db.parte.persona_id':50,
            'db.parte.caracter':30}
    ar = request.args # save typing
    vv = request.vars.lang
    expte=''
    linked_tables=['movimiento','agenda','parte']
    if ar and len(ar)>2:
        if 'expediente_id' in ar[1]:
            #expte= crud.read(db.expediente, ar[2])
            expte= SQLFORM(db.expediente, ar[2], readonly=True)
            links=[]
            for k in linked_tables:
                args=['expediente','%s.expediente_id'%k,ar[2]]
                url=URL('admin_expedientes',args=args, user_signature=True)
                text=SPAN(k.capitalize()+'s',_class='buttontext button')
                links.append(A(text,_href=url,_class='class="btn btn-default'))
        if len(ar)>4 and ar[4]=="parte":
            response.flash='Es una parte'
    grid = SQLFORM.smartgrid(db.expediente,
                             fields=[db.expediente.numero,
                                     db.expediente.caratula,
                                     db.expediente.juzgado_id,
                                    db.movimiento.estado,
                                    db.movimiento.titulo,
                                    db.movimiento.texto,
                                    db.agenda.estado,db.agenda.prioridad,
                                    db.agenda.vencimiento,
                                    db.agenda.titulo,
                                    db.parte.persona_id,
                                    db.parte.caracter],
                             constraints={'expediente':(db.expediente.created_by==auth.user.id)},
                             linked_tables=['movimiento','agenda','parte'],
                            buttons_placement = 'right',
                            exportclasses=myexport,
                             maxtextlength=100,
                            maxtextlengths=maxtextlengths)
    #dd=info(grid)
    return locals()


@auth.requires_login()
def admin_juzgados():
    db.juzgado.fuero_id.widget._class='form-control string'
    grid = SQLFORM.grid(db.juzgado,user_signature=False,maxtextlength=50,exportclasses=myexport)
    return locals()

@auth.requires_login()
def admin_personas():
    grid = SQLFORM.grid(db.persona.created_by==auth.user.id,
                        user_signature=False,
                        maxtextlength=50,
                        exportclasses=myexport)
    return locals()

@auth.requires_login()
def fueros():
    grid = SQLFORM.grid(db.fuero,maxtextlength=50,exportclasses=myexport)
    return locals()

@auth.requires_login()
def instancias():
    grid = SQLFORM.grid(db.instancia,maxtextlength=50,exportclasses=myexport)
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
