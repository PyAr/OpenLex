# Acá realizaremos un testing de la funcionalidad de carga de eventos en la agenda.
# El script está incompleto, ya que tuve que declarar un issue sobre un error especificado al testear.

def test_agenda(page):
    # Go to main page
    page.goto("")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")

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

    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente/new/expediente?_signature=abf1a846979d0a52c2cfd51266fa926ebc716634"

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

    # Fill input[name="_autocomplete_tipoproceso_descripcion_aux"]
    page.fill("input[name=\"_autocomplete_tipoproceso_descripcion_aux\"]", "")

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
    # assert page.url == "http://127.0.0.1:8020/OpenLex/expedientes/index/expediente?_signature=b4302dbdc27c76feb46824924c5cafd5f92c836c#"

    # Click text=Agenda
    page.click("text=Agenda")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/agenda/agenda"

    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/agenda/agenda/new/agenda"

    # Click input[name="_autocomplete_expediente_numero_aux"]
    page.click("input[name=\"_autocomplete_expediente_numero_aux\"]")

    # Fill input[name="_autocomplete_expediente_numero_aux"]
    page.fill("input[name=\"_autocomplete_expediente_numero_aux\"]", "1")

    # Click input[name="vencimiento"]
    page.click("input[name=\"vencimiento\"]")

    # Click text=30
    page.click("text=30")

    # Click input[name="cumplido"]
    page.click("input[name=\"cumplido\"]")

    # Click :nth-match(:text("27"), 2)
    page.click(":nth-match(:text(\"27\"), 2)")

    # Select 2
    page.select_option("select[name=\"prioridad\"]", "2")

    # Select R
    page.select_option("select[name=\"estado\"]", "R")

    # Click input[name="titulo"]
    page.click("input[name=\"titulo\"]")

    # Fill input[name="titulo"]
    page.fill("input[name=\"titulo\"]", "Agenda1")

    # Click html
    page.frame(url="about:blank").click("html")

    # Click text=Agenda
    page.frame(url="about:blank").click("text=Agenda")

    # Click text=Agenda de ejemplo
    page.frame(url="about:blank").click("text=Agenda de ejemplo")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/agenda/agenda/new/agenda#"

    # Close page
    page1.close()

    # Close page
    page.close()
