# Testing obligatorio para tener un usuario y contraseña de prueba, para usar los demás scripts.

def test_register(page):
    # Go to main page
    page.goto("")

    # Click text=Log In
    page.click("text=Log In")

    # Click text=Registrarse
    page.click("text=Registrarse")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/register?_next=/OpenLex/default/index"


    # Click input[name="first_name"]
    page.click("input[name=\"first_name\"]")

    # Fill input[name="first_name"]
    page.fill("input[name=\"first_name\"]", "Juan")
    page.press("input[name=\"first_name\"]", "Tab")

    # Click input[name="last_name"]
    page.click("input[name=\"last_name\"]")

    # Fill input[name="last_name"]
    page.fill("input[name=\"last_name\"]", "Perez")
    page.press("input[name=\"last_name\"]", "Tab")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input[name="password_two"]
    page.click("input[name=\"password_two\"]")

    # Fill input[name="password_two"]
    page.fill("input[name=\"password_two\"]", "openlex1234")
    page.press("input[name=\"password_two\"]", "Tab")

    # Click input:has-text("Registrarse")
    page.click("input:has-text(\"Registrarse\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"
