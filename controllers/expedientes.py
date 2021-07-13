# -*- coding: utf-8 -*-
__author__ = "María Andrea Vignau (mavignau@gmail.com)"
__copyright__ = "(C) 2016 María Andrea Vignau. GNU GPL 3."

import zipfile
import io
import tempfile
from collections import OrderedDict
from xhtml2pdf import pisa
LINKED_TABLES = ['movimiento', 'agenda', 'parte']
ZIP_FILENAME = 'Movimiento.zip'
CHUNK_SIZE = 4096


@auth.requires_login()
def index():
    'muestra la grilla y permite la edición de los datos de los expedientes'

    # para que no aparezca visible el expediente al editarse datos relacionados
    db.movimiento.expediente_id.readable = db.movimiento.expediente_id.writable = False
    db.parte.expediente_id.readable = db.parte.expediente_id.writable = False
    db.agenda.expediente_id.readable = db.agenda.expediente_id.writable = False

    maxtextlengths = {'db.expediente.numero': 15,
                      'db.expediente.caratula': 60,
                      'db.expediente.juzgado_id': 45,
                      'db.movimiento.titulo': 40,
                      'db.movimiento.texto': 40,
                      'db.movimiento.estado': 5,
                      'db.agenda.vencimiento': 15,
                      'db.agenda.titulo': 60,
                      'db.parte.persona_id': 40,
                      'db.parte.caracter': 30}
    grid = SQLFORM.smartgrid(
        db.expediente,
        fields=[
            db.expediente.numero,
            db.expediente.caratula,
            db.expediente.juzgado_id,
            db.movimiento.estado,
            db.movimiento.titulo,
            db.movimiento.texto,
            db.agenda.estado,
            db.agenda.prioridad,
            db.agenda.vencimiento,
            db.agenda.titulo,
            db.parte.persona_id,
            db.parte.caracter,
            db.movimiento.expediente_id,
            db.parte.expediente_id,
            db.agenda.expediente_id,
            db.movimiento.id,
            db.parte.id,
            db.agenda.id,
        ],
        constraints={
            'expediente': (
                db.expediente.created_by == auth.user.id)},
        linked_tables=LINKED_TABLES,
        buttons_placement='right',
        exportclasses=myexport,
        advanced_search=False,
        maxtextlength=100,
        orderby={
            'expediente': db.expediente.numero,
            'movimiento': db.movimiento.id,
            'parte': db.parte.persona_id,
            'agenda': ~db.agenda.vencimiento},
        maxtextlengths=maxtextlengths)
    return locals()


@auth.requires_login()
def download():
    tempfiles = io.BytesIO()
    temparchive = zipfile.ZipFile(tempfiles, 'w', zipfile.ZIP_DEFLATED)
    temp_dir = tempfile.TemporaryDirectory()
    # Obtener ID de expediente y guardarlo en una lista.
    movimiento_full_row = db(db.movimiento).select()
    expediente_list = [numero.expediente_id for numero in movimiento_full_row]
    expediente_lists = OrderedDict.fromkeys(expediente_list).keys()

    # Separar archivos por el numero de expediente.
    for expedient_single_id in expediente_lists:
        movimiento_filter_row = db(db.movimiento.expediente_id == expedient_single_id).select(
                                    db.movimiento.archivo,
                                    db.movimiento.texto,
                                    db.movimiento.titulo)
        expedient_number_row = db(db.expediente.id == expedient_single_id).select(db.expediente.numero)
        expedient_name = [numero.numero for numero in expedient_number_row]
        try:
            for file_id in movimiento_filter_row:
                file_single = file_id.archivo
                if file_single:
                    file_loc = db.movimiento.archivo.retrieve_file_properties(file_single)['path'] + '/' + file_single
                    file_name = db.movimiento.archivo.retrieve_file_properties(file_single)['filename']
                    temparchive.write(file_loc, "upload/" + str(expedient_name[0]) + "/" + file_name)
        except Exception as err:
            response.flash = DIV(T('Fallo en la descarga de archivos'), PRE(str(err)))
        finally:
            for text_id in movimiento_filter_row:
                text_single_text = text_id.texto
                text_single_title = text_id.titulo
                status, result_file = convert_html_to_pdf(text_single_text, temp_dir.name + "/" + text_single_title + ".pdf")
                temparchive.write(result_file.name, "upload/" + str(expedient_name[0]) + "/" + text_single_title + ".pdf")
    del temp_dir
    temparchive.close()
    tempfiles.seek(0)
    response.headers['Content-Type'] = 'application/zip'
    response.headers['Content-Disposition'] = 'attachment; filename = %s' % ZIP_FILENAME
    res = response.stream(tempfiles, CHUNK_SIZE)
    return res


def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    with open(output_filename, "w+b") as result_file:
        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
                source_html,  # the HTML to convert
                dest=result_file)  # file handle to recieve result
        # return False on success and True on errors
    return pisa_status, result_file


def vista_expediente():
    'muestra un panel a la izquierda que tiene los datos del expediente y permite navegar en él'
    expte = SQLFORM(db.expediente,
                    int(request.args[0]),
                    formstyle='bootstrap',
                    readonly=True)

    url = URL(
        'index',
        args=[
            'expediente',
            'edit',
            'expediente',
            request.args[0]],
        user_signature=True)
    links = [A('Expediente', _href=url, _type='button',
               _class='btn btn-default')]
    for k in LINKED_TABLES:
        args = ['expediente', '%s.expediente_id' % k, request.args[0]]
        url = URL('index', args=args, user_signature=True)
        text = SPAN(k.capitalize() + 's', _class='buttontext button')
        links.append(A(text, _href=url, _type='button',
                       _class='btn btn-default'))
    url = URL('download', args='movimiento.archivo')  # Boton de descarga
    text_download = "Descarga"
    links.append(A(text_download, _href=url, _type='button',
                 _class='btn btn-default'))

    return dict(links=links, expte=expte)
