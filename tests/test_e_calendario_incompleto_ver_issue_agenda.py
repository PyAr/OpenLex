# Acá realizaremos un testing del recorrido del calendario.
# El testing está incompleto, ya que depende de la funcionalidad de carga de agenda, la cual requiere una revisión marcada como issue.

def test_calendario(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Calendario
    page.click("text=Calendario")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/agenda/calendar"

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
