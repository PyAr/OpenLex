# Testing script para editar el nombre de usuario, su contraseña, y una sucesión de log-out y log-in.

def test_edituser(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

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

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Perfil
    page.click("text=Perfil")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/profile?_next=/OpenLex/dashboard/view"

    # Double click input[name="first_name"]
    page.dblclick("input[name=\"first_name\"]")

    # Fill input[name="first_name"]
    page.fill("input[name=\"first_name\"]", "Jorge")
    page.press("input[name=\"first_name\"]", "Tab")

    # Double click input[name="last_name"]
    page.dblclick("input[name=\"last_name\"]")

    # Fill input[name="last_name"]
    page.fill("input[name=\"last_name\"]", "Lopez")
    page.press("input[name=\"last_name\"]", "Tab")

    # Click text=Aplicar cambios
    page.click("text=Aplicar cambios")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Jorge
    page.click("text=Bienvenido Jorge")

    # Click a:has-text("Perfil")
    page.click("a:has-text(\"Perfil\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/profile?_next=/OpenLex/dashboard/view"

    # Double click input[name="first_name"]
    page.dblclick("input[name=\"first_name\"]")

    # Fill input[name="first_name"]
    page.fill("input[name=\"first_name\"]", "Juan")
    page.press("input[name=\"first_name\"]", "Tab")

    # Click input[name="last_name"]
    page.click("input[name=\"last_name\"]")

    # Fill input[name="last_name"]
    page.fill("input[name=\"last_name\"]", "Perez")
    page.press("input[name=\"last_name\"]", "Tab")

    # Click text=Aplicar cambios
    page.click("text=Aplicar cambios")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Contraseña
    page.click("text=Contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/change_password?_next=/OpenLex/dashboard/view"

    # Fill input[name="old_password"]
    page.fill("input[name=\"old_password\"]", "openlex1234")
    page.press("input[name=\"old_password\"]", "Tab")

    # Click input[name="new_password"]
    page.click("input[name=\"new_password\"]")

    # Fill input[name="new_password"]
    page.fill("input[name=\"new_password\"]", "closedlex1234")
    page.press("input[name=\"new_password\"]", "Tab")

    # Click input[name="new_password2"]
    page.click("input[name=\"new_password2\"]")

    # Fill input[name="new_password2"]
    page.fill("input[name=\"new_password2\"]", "closedlex1234")
    page.press("input[name=\"new_password2\"]", "Tab")

    # Click input:has-text("Cambie la contraseña")
    page.click("input:has-text(\"Cambie la contraseña\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Log Out
    page.click("text=Log Out")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/index"

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=%2FOpenLex%2Fdefault%2Findex#"

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "closedlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Contraseña
    page.click("text=Contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/change_password?_next=/OpenLex/dashboard/view"

    # Fill input[name="old_password"]
    page.fill("input[name=\"old_password\"]", "closedlex1234")
    page.press("input[name=\"old_password\"]", "Tab")

    # Click input[name="new_password"]
    page.click("input[name=\"new_password\"]")

    # Fill input[name="new_password"]
    page.fill("input[name=\"new_password\"]", "openlex1234")
    page.press("input[name=\"new_password\"]", "Tab")

    # Click input[name="new_password2"]
    page.click("input[name=\"new_password2\"]")

    # Fill input[name="new_password2"]
    page.fill("input[name=\"new_password2\"]", "openlex1234")
    page.press("input[name=\"new_password2\"]", "Tab")

    # Click input:has-text("Cambie la contraseña")
    page.click("input:has-text(\"Cambie la contraseña\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Log Out
    page.click("text=Log Out")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/index"

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "closedlex1234")
    page.press("input[name=\"password\"]", "Tab")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=%2FOpenLex%2Fdefault%2Findex#"

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

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Bienvenido Juan
    page.click("text=Bienvenido Juan")

    # Click text=Log Out
    page.click("text=Log Out")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/index"
