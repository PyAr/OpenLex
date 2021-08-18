# Este es un testing de la funcionalidad de carga y eliminación de expedientes.

def test_fuero(page, login):
    # Click text=Tablas >> span
    page.click("text=Tablas >> span")
    # Click text=Fueros
    page.click("text=Fueros")
    assert page.url.endswith("/other_tables/fueros")
    # Click text=Agregar
    page.click("text=Agregar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/fueros/new/fuero?_signature=9c5e26524c1ba22e5950e19298faf96aa47e9900"
    # Click input[name="descripcion"]
    page.click("input[name=\"descripcion\"]")
    # Fill input[name="descripcion"]
    page.fill("input[name=\"descripcion\"]", "prueba")
    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8000/OpenLex_pruebs/other_tables/fueros?_signature=04feae14d228f1e0374a0e18482c4150b1d834b8#"
    # Click text=prueba
    page.click("text=prueba")
