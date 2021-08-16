
def test_jurisdiccion(page, login):
   # Click text=Tablas
    page.click("text=Tablas")
    # Click text=Jurisdicciones
    page.click("text=Jurisdicciones")
    assert page.url.endswith("/other_tables/jurisdicciones")
    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/jurisdicciones/new/jurisdiccion?_signature=4d34dadde81096e807c60d8d1edc37d86b2a6e5d"
    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")
    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "Cordoba")
    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/jurisdicciones?_signature=90dba84860e5636d3dd047863481054363baf0a7#"

