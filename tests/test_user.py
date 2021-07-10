def login(page):
    page.click("text=Log In")
    page.click(":nth-match(:text(\"Log In\"), 2)")
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")
    page.fill("input[name=\"password\"]", "openlex1234")
    page.click("input:has-text(\"Log In\")")

def test_register(page):
    # ir a la página de inicio (ver pytest.ini para la url base)
    page.goto("")
    # desplegar el menu, ir a la página de registración (y confirmar url)
    page.click("text=Log In")
    page.click("text=Registrarse")
    assert page.url.endswith("OpenLex/default/user/register?_next=/OpenLex/default/index")

    # completar el formulario de registro:
    page.click("input[name=\"first_name\"]")
    page.fill("input[name=\"first_name\"]", "Juan")
    page.press("input[name=\"first_name\"]", "Tab")
    page.fill("input[name=\"last_name\"]", "Perez")
    page.press("input[name=\"last_name\"]", "Tab")
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")
    page.fill("input[name=\"password\"]", "openlex1234")
    page.press("input[name=\"password\"]", "Tab")
    page.fill("input[name=\"password_two\"]", "openlex1234")
    page.click("input:has-text(\"Registrarse\")")

    # confirmar que se tomó el formulario y pasó a la página principal:
    assert page.url.endswith("/dashboard/view#")
    # confirmar que se creó el usuario:
    assert page.inner_text("text=Bienvenido, Juan Perez")


def test_login(page):
    # ADVERTENCIA: este test depende del anterior (sería bueno que sea independiente)
    # ir a la página de inicio (ver pytest.ini para la url base)
    page.goto("")
    # desplegar el menu, ir a la página de registración (y confirmar url)
    login(page)
    # confirmar
    assert page.url.endswith("/dashboard/view#")


def test_upload_expedientes(page):
    page.goto("")
    login(page)
    page.click("css=[alt=Expedientes]")
    assert page.url.endswith("/expedientes/index")
    page.click("text=Agregar")
    page.fill("input[name=\"numero\"]", "1111")
    page.press("input[name=\"numero\"]", "Tab")
    page.fill("input[name=\"caratula\"]", "ssdd")
    page.click("input:has-text(\"Enviar\")")


def test_download(page):
    page.goto("")
    page.setDefaultTimeout(10000)
    login(page)
    page.goto("expedientes/index")
    page.click("text=Movimientos")
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.click("text=Descarga")
    download = download_info.value
    # Wait for the download process to complete
    name = download.suggested_filename
    #cut_link = link[22:]
    assert "Movimiento.zip" == name
