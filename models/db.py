# -*- coding: utf-8 -*-
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."


def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    methodList = [
        method for method in dir(object) if callable(
            getattr(
                object,
                method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    return "\n<br>".join(["<strong>%s</strong> %s" %
                          (method.ljust(spacing),
                           processFunc(str(getattr(object, method).__doc__)))
                          for method in methodList])

#########################################################################
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
#########################################################################

# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# request.requires_https()

# app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
# once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    # if NOT running on Google App Engine use SQLite or other DB
    db = DAL(
        myconf.take('db.uri'),
        pool_size=myconf.take(
            'db.pool_size',
            cast=int),
        check_reserved=['all'])
else:
    # connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    # store sessions and tickets there
    session.connect(request, response, db=db)
    # or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
# choose a style for forms
# or 'bootstrap3_stacked' or 'bootstrap2' or other
response.formstyle = myconf.take('forms.formstyle')
response.form_label_separator = myconf.take('forms.separator')


# (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
# (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

# configure email
mail = auth.settings.mailer
mail.settings.server = myconf.take(
    'smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

# configure auth policy
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
#auth.settings.allow_basic_login = True

#########################################################################
# Define your tables below (or better in another model file) for example
##
# >>> db.define_table('mytable',Field('myfield','string'))
##
# Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
##
# More API examples for controllers:
##
# >>> db.mytable.insert(myfield='value')
# >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
#########################################################################

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
