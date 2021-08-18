
def test_tipo_de_proceso(page, login):
    # Click text=Tablas
    page.click("text=Tablas")
    # Click text=Tipos de proceso
    page.click("text=Tipos de proceso")
    assert page.url.endswith("/other_tables/tipoproceso")
    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/tipoproceso/new/tipoproceso?_signature=3a63d84ac5c5925f156967bbf138e5f8fa026e80"
    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")
    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "penal")
    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/tipoproceso?_signature=0e3a79c8cb0dfe0968eaee471147a72cfd303d33#"
    # Click text=penal
    page.click("text=penal")

