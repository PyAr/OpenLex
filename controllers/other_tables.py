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
    formcsv = import_table(db(db.fuero))
    return dict(grid=grid, formcsv=formcsv)


@auth.requires_membership('admin')
def instancias():
    grid = SQLFORM.grid(db.instancia,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.instancia.descripcion,
                        exportclasses=myexport)
    formcsv = import_table(db(db.instancia))
    return dict(grid=grid, formcsv=formcsv)


@auth.requires_membership('admin')
def jurisdicciones():
    grid = SQLFORM.grid(db.jurisdiccion,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.jurisdiccion.descripcion,
                        exportclasses=myexport)
    formcsv = import_table(db(db.jurisdiccion))
    return dict(grid=grid, formcsv=formcsv)


def tipoproceso():
    grid = SQLFORM.grid(db.tipoproceso,
                        maxtextlength=50,
                        advanced_search=False,
                        orderby=db.tipoproceso.descripcion,
                        exportclasses=myexport)
    formcsv = import_table(db(db.tipoproceso))
    return dict(grid=grid, formcsv=formcsv)


def import_csv(table, file):
    table.import_from_csv_file(file)


def import_table(table):
    csv_table = table or request.vars.table
    if csv_table:
        formcsv = FORM(str(T('or import from csv file')) + " ",
                       INPUT(_type='file', _name='csvfile'),
                       INPUT(_type='hidden', _value=csv_table, _name='table'),
                       INPUT(_type='submit', _value=T('import')))
    else:
        formcsv = None
    if formcsv and formcsv.process().accepted:
        try:
            import_csv(db[request.vars.table],
                       request.vars.csvfile.file)
            response.flash = T('data uploaded')
        except Exception as err:
            response.flash = DIV(T('unable to parse csv file'), PRE(str(err)))
    return formcsv
