# -*- coding: utf-8 -*-
# intente algo como
def groups():
    grid = SQLFORM.grid(db.auth_membership,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
                        exportclasses=myexport)
    url = URL('create_groups')
    text_assign = "Crear grupos"
    link = (A(text_assign, _href=url, _type='button',
                 _class='btn btn-default'))
    url = URL('control')
    text_assign = "Control de cambios"
    link.append(A(text_assign, _href=url, _type='button',
                 _class='btn btn-default'))
    return dict(grid=grid, link=link)

def create_groups():
    grid = SQLFORM.grid(db.auth_group,
                        user_signature=False,
                        maxtextlength=50,
                        advanced_search=False,
                        exportclasses=myexport)
    return locals()


def control():
    db.expediente.modified_by.readable = True
    db.expediente.modified_on.readable = True 
    db.expediente.writable = False
    grid = SQLFORM.smartgrid(
        db.expediente,
        fields=[
            db.expediente.numero,
            db.expediente.modified_on,
            db.expediente.modified_by
        ],
        linked_tables=False,
        buttons_placement='right',
        exportclasses=myexport,
        advanced_search=False,
        maxtextlength=100,
        editable = False,
        deletable= False,
        create=False,
        orderby=db.expediente.modified_on,
        paginate=25,)
            
    return dict(grid=grid)



def control_groups():
    pass
