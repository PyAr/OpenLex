def test_agenda_issue44_without_expediente_id(page, login):
    # Click text=Agenda
    page.click("text=Agenda")
    assert page.url.endswith("/agenda/agenda")
    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")
    assert page.url.endswith("/agenda/agenda/new/agenda")
    # Click input[name="titulo"]
    # Fill Without the field expediente_id
    page.click("input[name=\"titulo\"]")
    # Fill input[name="titulo"]
    page.fill("input[name=\"titulo\"]", "tarea erronea")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")
    # Error Message
    # Click text=Vincular con un expediente
    page.click("text=Vincular con un expediente")
    # Fill the field expediente_id
    # Click input[name="_autocomplete_expediente_numero_aux"]
    page.click("input[name=\"_autocomplete_expediente_numero_aux\"]")
    # Fill input[name="_autocomplete_expediente_numero_aux"]
    page.fill("input[name=\"_autocomplete_expediente_numero_aux\"]", "1111")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")

