
def test_instancia(page, login):
    # Click text=Tablas
    page.click("text=Tablas")
    # Click text=Instancias
    page.click("text=Instancias")
    assert page.url.endswith("/other_tables/instancias")
    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/instancias/new/instancia?_signature=6bb7e73c9ce1c8a5173cc913bdaaf72f421d4992"
    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")
    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "Segunda instancia")
    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/instancias?_signature=442d4dabfb40d53d499162c3efb4d218a85daba9#"
    # Click text=Segunda instancia
    page.click("text=Segunda instancia")
