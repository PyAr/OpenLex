def test_register(page):
    # ir a la página de inicio (ver pytest.ini para la url base)
    page.goto("")
    # ir a la página de registración (y confirmar url)
    page.click("text=Registrarse")
    assert page.url.endswith("openlex/default/user/register")

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
