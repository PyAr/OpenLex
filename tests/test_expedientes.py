# Este es un testing de la funcionalidad de carga y eliminación de expedientes.

def test_expedientes(page):
    # Go to main page
    page.goto("")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(i, 3)
    page.click(":nth-match(i, 3)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

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

    # Click input[name="caratula"]
    page.click("input[name=\"caratula\"]")

    # Fill input[name="caratula"]
    page.fill("input[name=\"caratula\"]", "Ejemplo1")

    # Click input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.click("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]")

    # Click input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.click("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]")

    # Fill input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.fill("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]", "Judicial")

    # Click input[name="_autocomplete_juzgado_descripcion_aux"]
    page.click("input[name=\"_autocomplete_juzgado_descripcion_aux\"]", modifiers=["Shift"])

    # Click input[name="_autocomplete_juzgado_descripcion_aux"]
    page.click("input[name=\"_autocomplete_juzgado_descripcion_aux\"]")

    # Fill input[name="_autocomplete_juzgado_descripcion_aux"]
    page.fill("input[name=\"_autocomplete_juzgado_descripcion_aux\"]", "Córdoba")

    # Click input[name="inicio"]
    page.click("input[name=\"inicio\"]")

    # Click text=27
    page.click("text=27")

    # Click input[name="final"]
    page.click("input[name=\"final\"]")

    # Click :nth-match(:text("30"), 2)
    page.click(":nth-match(:text(\"30\"), 2)")

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

    # Click #c13727166550682224 >> text=Expediente
    page.click("#c13727166550682224 >> text=Expediente")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/edit/expediente/1?_signature=91f6e51c077f52497a3812868aaebf58ff7b18d4"

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/parte.expediente_id/1?_signature=ab994621f5dadf11fe43424968092cb8f7cb7240#"

    # Click #c546270956379269 >> text=Expediente
    page.click("#c546270956379269 >> text=Expediente")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/edit/expediente/1?_signature=91f6e51c077f52497a3812868aaebf58ff7b18d4"

    # Click .icon.magnifier
    page.click(".icon.magnifier")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/view/expediente/1?_signature=26b7034014f4510f896b4c802b3a1aa9e333f93f"

    # Click text=Atrás
    page.click("text=Atrás")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/parte.expediente_id/1?_signature=ab994621f5dadf11fe43424968092cb8f7cb7240"

    # Click text=Expedientes
    page.click("text=Expedientes")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index"

    # Click a:has-text("Editar")
    page.click("a:has-text(\"Editar\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/edit/expediente/1?_signature=91f6e51c077f52497a3812868aaebf58ff7b18d4"

    # Check input[name="delete_this_record"]
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.check("input[name=\"delete_this_record\"]")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente?_signature=9738bd7a4677227cf1a6e2b1ae9a8747b990925a#"

    # Close page
    page.close()


test_expedientes(page)
