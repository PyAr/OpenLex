# Este es el testing de lectura y carga de juzgados.
# No puede ser testeado apropiadamente hasta resolver el issue de las tablas.

def test_juzgados(page):
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

    # Click text=Juzgados
    page.click("text=Juzgados")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/other_tables/juzgados"

    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/other_tables/juzgados/new/juzgado"

    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")

    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "Juzgado Municipal")
    page.press("input[name=\"descripcion\"]", "Tab")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/other_tables/juzgados/new/juzgado#"

    # Click a:has-text("Atrás")
    page.click("a:has-text(\"Atrás\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/other_tables/juzgados"

    # Close page
    page.close()
