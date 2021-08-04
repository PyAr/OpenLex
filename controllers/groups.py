# -*- coding: utf-8 -*-
# intente algo como
def groups():
    grid = SQLFORM.grid(db.auth_membership,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
                        exportclasses=myexport)
    url = URL('create_groups')  # Boton de descarga
    text_assign = "Crear grupos"
    link = (A(text_assign, _href=url, _type='button',
                 _class='btn btn-default'))
    return dict(grid=grid, link=link)

def create_groups():
    grid = SQLFORM.grid(db.auth_group,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
                        exportclasses=myexport)
    return locals()
