# Acá realizaremos un testing del recorrido del calendario.
# El testing está incompleto, ya que depende de la funcionalidad de carga de agenda, la cual requiere una revisión marcada como issue.

def test_calendario(page, login):
    # Click text=Calendario
    page.click("text=Calendario")
    assert page.url.endswith("/agenda/calendar")

    # Click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)")

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 3)
    page.dblclick("#calendar div div >> :nth-match(button, 3)")

    # Triple click #calendar div div >> :nth-match(button, 2)
    page.click("#calendar div div >> :nth-match(button, 2)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 2)
    page.dblclick("#calendar div div >> :nth-match(button, 2)")

    # Click text=Hoy
    page.click("text=Hoy")

    # Click text=Semana
    page.click("text=Semana")

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 4)
    page.dblclick("#calendar div div >> :nth-match(button, 4)")

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 4)
    page.dblclick("#calendar div div >> :nth-match(button, 4)")

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 3)
    page.dblclick("#calendar div div >> :nth-match(button, 3)")

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 2)
    page.click("#calendar div div >> :nth-match(button, 2)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 2)
    page.dblclick("#calendar div div >> :nth-match(button, 2)")

    # Click text=Hoy
    page.click("text=Hoy")

    # Click text=Día
    page.click("text=Día")

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 4)
    page.click("#calendar div div >> :nth-match(button, 4)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 4)
    page.dblclick("#calendar div div >> :nth-match(button, 4)")

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 3)
    page.dblclick("#calendar div div >> :nth-match(button, 3)")

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 3)
    page.click("#calendar div div >> :nth-match(button, 3)", click_count=3)

    # Double click #calendar div div >> :nth-match(button, 3)
    page.dblclick("#calendar div div >> :nth-match(button, 3)")

    # Triple click #calendar div div >> :nth-match(button, 2)
    page.click("#calendar div div >> :nth-match(button, 2)", click_count=3)

    # Triple click #calendar div div >> :nth-match(button, 2)
    page.click("#calendar div div >> :nth-match(button, 2)", click_count=3)

    # Click text=Hoy
    page.click("text=Hoy")
