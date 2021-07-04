# Acá realizaremos un testing del recorrido del calendario.
# El testing está incompleto, ya que depende de la funcionalidad de carga de agenda, la cual requiere una revisión marcada como issue.

def test_calendario(page):
    # Go to main page
    page.goto("")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")

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

    # Click text=HoyMesSemanaDíaagosto 2028 >> button
    page.click("text=HoyMesSemanaDíaagosto 2028 >> button")

    # Double click text=HoyMesSemanaDíaagosto 2027 >> button
    page.dblclick("text=HoyMesSemanaDíaagosto 2027 >> button")

    # Triple click text=HoyMesSemanaDíaagosto 2026 >> button
    page.click("text=HoyMesSemanaDíaagosto 2026 >> button", click_count=3)

    # Double click text=HoyMesSemanaDíaagosto 2022 >> button
    page.dblclick("text=HoyMesSemanaDíaagosto 2022 >> button")

    # Triple click text=HoyMesSemanaDíaagosto 2021 >> button
    page.click("text=HoyMesSemanaDíaagosto 2021 >> button", click_count=3)

    # Double click text=HoyMesSemanaDíaagosto 2017 >> button
    page.dblclick("text=HoyMesSemanaDíaagosto 2017 >> button")

    # Triple click text=HoyMesSemanaDíaagosto 2016 >> button
    page.click("text=HoyMesSemanaDíaagosto 2016 >> button", click_count=3)

    # Click text=HoyMesSemanaDíaagosto 2013 >> button
    page.click("text=HoyMesSemanaDíaagosto 2013 >> button")

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

    # Click text=HoyMesSemanaDía4 — 10 de jun. de 2029 >> button
    page.click("text=HoyMesSemanaDía4 — 10 de jun. de 2029 >> button")

    # Double click text=HoyMesSemanaDía5 — 11 de jun. de 2028 >> button
    page.dblclick("text=HoyMesSemanaDía5 — 11 de jun. de 2028 >> button")

    # Triple click text=HoyMesSemanaDía7 — 13 de jun. de 2027 >> button
    page.click("text=HoyMesSemanaDía7 — 13 de jun. de 2027 >> button", click_count=3)

    # Double click text=HoyMesSemanaDía5 — 11 de jun. de 2023 >> button
    page.dblclick("text=HoyMesSemanaDía5 — 11 de jun. de 2023 >> button")

    # Triple click text=HoyMesSemanaDía6 — 12 de jun. de 2022 >> button
    page.click("text=HoyMesSemanaDía6 — 12 de jun. de 2022 >> button", click_count=3)

    # Double click text=HoyMesSemanaDía4 — 10 de jun. de 2018 >> button
    page.dblclick("text=HoyMesSemanaDía4 — 10 de jun. de 2018 >> button")

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

    # Click text=HoyMesSemanaDía15 de junio de 2032 >> button
    page.click("text=HoyMesSemanaDía15 de junio de 2032 >> button")

    # Double click text=HoyMesSemanaDía15 de junio de 2031 >> button
    page.dblclick("text=HoyMesSemanaDía15 de junio de 2031 >> button")

    # Triple click text=HoyMesSemanaDía15 de junio de 2030 >> button
    page.click("text=HoyMesSemanaDía15 de junio de 2030 >> button", click_count=3)

    # Double click text=HoyMesSemanaDía15 de junio de 2026 >> button
    page.dblclick("text=HoyMesSemanaDía15 de junio de 2026 >> button")

    # Triple click text=HoyMesSemanaDía15 de junio de 2025 >> button
    page.click("text=HoyMesSemanaDía15 de junio de 2025 >> button", click_count=3)

    # Double click text=HoyMesSemanaDía15 de junio de 2021 >> button
    page.dblclick("text=HoyMesSemanaDía15 de junio de 2021 >> button")

    # Triple click text=HoyMesSemanaDía15 de junio de 2020 >> button
    page.click("text=HoyMesSemanaDía15 de junio de 2020 >> button", click_count=3)

    # Double click text=HoyMesSemanaDía15 de junio de 2016 >> button
    page.dblclick("text=HoyMesSemanaDía15 de junio de 2016 >> button")

    # Click text=Hoy
    page.click("text=Hoy")

    # Close page
    page.close()
