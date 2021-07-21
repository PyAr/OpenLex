def test_agenda_issue56_without_reminder(page, login):
    # Click text=Agenda
    page.click("text=Agenda")
    assert page.url.endswith("/agenda/agenda")
    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")
    assert page.url.endswith("/agenda/agenda/new/agenda")
    # Click input[name="_autocomplete_expediente_numero_aux"]
    page.click("input[name=\"_autocomplete_expediente_numero_aux\"]")
    # Fill input[name="_autocomplete_expediente_numero_aux"]
    page.fill("input[name=\"_autocomplete_expediente_numero_aux\"]", "11")
    # Click input[name="titulo"]
    page.click("input[name=\"titulo\"]")
    # Fill input[name="titulo"]
    page.fill("input[name=\"titulo\"]", "tarea erronea sin recordatorio")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")
    # Error Message
    # Click text=Establezca la frecuencia correcta
    page.click("text=Establezca la frecuencia correcta")
    # Select S
    page.select_option("select[name=\"recordatorio\"]", "S")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/agenda/agenda/new/agenda#")
