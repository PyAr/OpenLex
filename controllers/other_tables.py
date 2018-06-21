# -*- coding: utf-8 -*-
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."



def juzgados():
    grid = SQLFORM.grid(db.juzgado,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
                        exportclasses=myexport)
    return locals()


@auth.requires_membership('admin')
def fueros():
    grid = SQLFORM.grid(db.fuero,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.fuero.descripcion,
                        exportclasses=myexport)
    return locals()


@auth.requires_membership('admin')
def instancias():
    grid = SQLFORM.grid(db.instancia,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.instancia.descripcion,
                        exportclasses=myexport)
    return locals()

@auth.requires_membership('admin')
def jurisdicciones():
    grid = SQLFORM.grid(db.jurisdiccion,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.jurisdiccion.descripcion,
                        exportclasses=myexport)
    return locals()



def tipoproceso():
    grid = SQLFORM.grid(db.tipoproceso,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.tipoproceso.descripcion,
                        exportclasses=myexport)
    return locals()
