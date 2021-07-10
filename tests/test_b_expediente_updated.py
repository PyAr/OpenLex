def test_upload_expedientes(page):
    pattern = "movimiento.expediente_id"
    page.goto("http://127.0.0.1:8020/OpenLex/")
    login(page)
    page.click("css=[alt=Expedientes]")
    assert page.url.endswith("/expedientes/index")
    page.click("text=Agregar")
    page.fill("input[name=\"numero\"]", "1111")
    page.press("input[name=\"numero\"]", "Tab")
    page.fill("input[name=\"caratula\"]", "ssdd")
    page.click("input:has-text(\"Enviar\")")
    
def login(page):
    page.click("text=Log In")
    page.click(":nth-match(:text(\"Log In\"), 2)")
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")
    page.fill("input[name=\"password\"]", "openlex1234")
    page.click("input:has-text(\"Log In\")")
