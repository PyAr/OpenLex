# Este es el testing de la página principal.
# Para ser completado, debería revisarse el issue de la agenda.

def test_mainpage(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click img[alt="expedientes"]
    page.click("img[alt=\"expedientes\"]")

    # Click text=Open
    page.click("text=Open")

    # Click text=Inicio
    page.click("text=Inicio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view"

    # Click img[alt="Expedientes"]
    page.click("img[alt=\"Expedientes\"]")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index"

    # Click text=Inicio
    page.click("text=Inicio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view"

    # Click img[alt="Calendario"]
    page.click("img[alt=\"Calendario\"]")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/agenda/calendar"

    # Click text=Inicio
    page.click("text=Inicio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view"

    # Click img[alt="Contactos"]
    page.click("img[alt=\"Contactos\"]")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index"

    # Click text=Inicio
    page.click("text=Inicio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view"

    # Click a:has-text("1")
    page.click("a:has-text(\"1\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/edit/expediente/2?_signature=c4e967fad98132e50cf5f01dc49d20e477e34d04"

    # Click text=Inicio
    page.click("text=Inicio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view"

    # Click text=Nº
    page.click("text=Nº")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view?order=expediente.numero&_signature=549494d9439687f9306299879fc0996f2da81a7e"

    # Click text=Carátula
    page.click("text=Carátula")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view?order=expediente.caratula&_signature=549494d9439687f9306299879fc0996f2da81a7e"
