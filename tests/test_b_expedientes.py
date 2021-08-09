# Este es un testing de la funcionalidad de carga y eliminación de expedientes.

def test_expedientes(page, login):
    # Click text=Expedientes
    page.click("text=Expedientes")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index"

    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/new/expediente?_signature=810bffae43892495ced516903d05ceefa2274953"

    # Click input[name="numero"]
    page.click("input[name=\"numero\"]")

    # Fill input[name="numero"]
    page.fill("input[name=\"numero\"]", "1")
    page.press("input[name=\"numero\"]", "Tab")

    # Click input[name="caratula"]
    page.click("input[name=\"caratula\"]")

    # Fill input[name="caratula"]
    page.fill("input[name=\"caratula\"]", "Ejemplo1")
    page.press("input[name=\"caratula\"]", "Tab")

    # Click input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.click("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]")

    # Click input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.click("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]")

    # Fill input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.fill("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]", "Judicial")
    page.press("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]", "Tab")

    # Click input[name="_autocomplete_juzgado_descripcion_aux"]
    page.click("input[name=\"_autocomplete_juzgado_descripcion_aux\"]", modifiers=["Shift"])

    # Click input[name="_autocomplete_juzgado_descripcion_aux"]
    page.click("input[name=\"_autocomplete_juzgado_descripcion_aux\"]")

    # Fill input[name="_autocomplete_juzgado_descripcion_aux"]
    page.fill("input[name=\"_autocomplete_juzgado_descripcion_aux\"]", "Córdoba")
    page.press("input[name=\"_autocomplete_juzgado_descripcion_aux\"]", "Tab")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente?_signature=9738bd7a4677227cf1a6e2b1ae9a8747b990925a#"

    # Click text=Movimientos
    page.click("text=Movimientos")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/movimiento.expediente_id/1?_signature=77bd67d3790979a409cde74c6a77cf8b2fc17ef7"

    # Click text=Agendas
    page.click("text=Agendas")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/agenda.expediente_id/1?_signature=000118e6f124de00f945880d238c160fcee32582"

    # Click text=Partes
    page.click("text=Partes")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/parte.expediente_id/1?_signature=ab994621f5dadf11fe43424968092cb8f7cb7240"

    # Click text=Expedientes
    page.click("text=Expedientes")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index"

    # Click a:has-text("Editar")
    page.click("a:has-text(\"Editar\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/edit/expediente/1?_signature=91f6e51c077f52497a3812868aaebf58ff7b18d4"

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente?_signature=9738bd7a4677227cf1a6e2b1ae9a8747b990925a#"
