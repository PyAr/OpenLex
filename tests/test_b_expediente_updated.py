def test_upload_expedientes(page, login):
    pattern = "movimiento.expediente_id"
    page.click("css=[alt=Expedientes]")
    assert page.url.endswith("/expedientes/index")
    page.click("text=Agregar")
    page.fill("input[name=\"numero\"]", "1111")
    page.press("input[name=\"numero\"]", "Tab")
    page.fill("input[name=\"caratula\"]", "ssdd")
    page.click("input:has-text(\"Enviar\")")
