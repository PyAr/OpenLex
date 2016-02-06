# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def juzgados():
    grid = SQLFORM.grid(db.juzgado,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
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
