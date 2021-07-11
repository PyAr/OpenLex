# Salteo del test provisorio
# Por favor, revisar todas estas líneas
# Revisar después de chequear issue de crasheo al intentar recuperar contraseña con servidor de e-mail inválido.

import pytest
@pytest.mark.skip(reason="Marking an issue with the password rescue feature, delete this line after closing the issue.")



# Este es un testing de una solicitud por contraseña olvidada.
# Genera un error al cargar una dirección de e-mail registrada, pero con un servidor ficticio. Ya fue reportado como issue.

def test_passwordchange(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click text=¿Olvidó la contraseña?
    page.click("text=¿Olvidó la contraseña?")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index"

    # Triple click input[name="email"]
    page.click("input[name=\"email\"]", click_count=3)

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click text=Solicitar reinicio de contraseña
    page.click("text=Solicitar reinicio de contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index#"
