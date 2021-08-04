def test_agenda_issue47_calendar_with_expiration(page, login):
    # Click text=Agenda
    page.click("text=Agenda")
    assert page.url.endswith("/agenda/agenda")
    # Click text=Agregar
    page.click("text=Agregar")
    assert page.url.endswith("/agenda/agenda/new/agenda")
    # Click input[name="_autocomplete_expediente_numero_aux"]
    page.click("input[name=\"_autocomplete_expediente_numero_aux\"]")
    # Fill input[name="_autocomplete_expediente_numero_aux"]
    page.fill("input[name=\"_autocomplete_expediente_numero_aux\"]", "1111")
    # Click input[name="vencimiento"]
    page.click("input[name=\"vencimiento\"]")
    # Click :nth-match(:text("29"), 2)
    page.click(":nth-match(:text(\"30\"), 2)")
    # Click input[name="titulo"]
    page.click("input[name=\"titulo\"]")
    # Fill input[name="titulo"]
    page.fill("input[name=\"titulo\"]", "tarea")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")

def test_agenda_issue47_calendar_without_expiration(page, login):
    # Click text=Agenda
    page.click("text=Agenda")
    # Click text=Agregar
    page.click("text=Agregar")
    page.click("input[name=\"_autocomplete_expediente_numero_aux\"]")
    # Fill input[name="_autocomplete_expediente_numero_aux"]
    page.fill("input[name=\"_autocomplete_expediente_numero_aux\"]", "1111")
    # Click input[name="titulo"]
    page.click("input[name=\"titulo\"]")
    # Fill input[name="titulo"]
    page.fill("input[name=\"titulo\"]", "tarea sin vencimiento")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")

