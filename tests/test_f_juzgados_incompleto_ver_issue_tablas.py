# Este es el testing de lectura y carga de juzgados.
# No puede ser testeado apropiadamente hasta resolver el issue de las tablas.

def test_juzgados(page, login):
    # Click text=Juzgados
    page.click("text=Juzgados")
    assert page.url.endswith("/other_tables/juzgados")

    # Click text=Agregar
    page.click("text=Agregar")
    assert page.url.endswith("/other_tables/juzgados/new/juzgado")

    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")

    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "Juzgado Municipal")
    page.press("input[name=\"descripcion\"]", "Tab")

    #Ampliar con datos una vez cargada las demas tablas
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/other_tables/juzgados/new/juzgado#")

    # Click a:has-text("Atrás")
    page.click("a:has-text(\"Atrás\")")
    assert page.url.endswith("/other_tables/juzgados")
