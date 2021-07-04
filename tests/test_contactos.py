# Acá realizaremos un testing de la funcionalidad de carga y eliminación de contactos.

def test_contactos(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click :nth-match(:text("Log In"), 2)
    page.click(":nth-match(:text(\"Log In\"), 2)")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/login?_next=/OpenLex/default/index"

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")

    # Click input:has-text("Log In")
    page.click("input:has-text(\"Log In\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Click text=Contactos
    page.click("text=Contactos")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index"

    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index/new/persona?_signature=08fbad2cf0e79833b0ba8d2ed92faeeee5c705dd"

    # Select F
    page.select_option("select[name=\"sexo\"]", "F")

    # Click input[name="apellido"]
    page.click("input[name=\"apellido\"]")

    # Fill input[name="apellido"]
    page.fill("input[name=\"apellido\"]", "Gonzalez")

    # Click input[name="nombre"]
    page.click("input[name=\"nombre\"]")

    # Fill input[name="nombre"]
    page.fill("input[name=\"nombre\"]", "María Juana")

    # Click input[name="cuitcuil"]
    page.click("input[name=\"cuitcuil\"]")

    # Fill input[name="cuitcuil"]
    page.fill("input[name=\"cuitcuil\"]", "20111111115")

    # Click input[name="domicilio"]
    page.click("input[name=\"domicilio\"]")

    # Fill input[name="domicilio"]
    page.fill("input[name=\"domicilio\"]", "Avenida del Software Libre 1984, Ciudad GNU")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "mariajuana@example.com")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Click html
    page.frame(url="about:blank").click("html")

    # Click input[name="telefono"]
    page.click("input[name=\"telefono\"]")

    # Fill input[name="telefono"]
    page.fill("input[name=\"telefono\"]", "1166666666")

    # Click input[name="celular"]
    page.click("input[name=\"celular\"]")

    # Fill input[name="celular"]
    page.fill("input[name=\"celular\"]", "1177777777")

    # Click input[name="matricula"]
    page.click("input[name=\"matricula\"]")

    # Fill input[name="matricula"]
    page.fill("input[name=\"matricula\"]", "666777")

    # Click input[name="domiciliolegal"]
    page.click("input[name=\"domiciliolegal\"]")

    # Fill input[name="domiciliolegal"]
    page.fill("input[name=\"domiciliolegal\"]", "Boulevard del Tux, Ciudad GNU")

    # Click input[name="domiciliolegal"]
    page.click("input[name=\"domiciliolegal\"]")

    # Click input[name="domiciliolegal"]
    page.click("input[name=\"domiciliolegal\"]")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("input[name=\"domiciliolegal\"]", "ArrowLeft")

    # Press ArrowRight
    page.press("input[name=\"domiciliolegal\"]", "ArrowRight")

    # Press ArrowRight
    page.press("input[name=\"domiciliolegal\"]", "ArrowRight")

    # Fill input[name="domiciliolegal"]
    page.fill("input[name=\"domiciliolegal\"]", "Boulevard del Tux 1992, Ciudad GNU")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?_signature=757a993c643dc478b57b21486e68f722168946fc#"

    # Click text=Apellido o Razón Social
    page.click("text=Apellido o Razón Social")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.apellido&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Nombre
    page.click("text=Nombre")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.nombre&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Nombre▲
    page.click("text=Nombre▲")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=~persona.nombre&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Domicilio
    page.click("text=Domicilio")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.domicilio&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=E-Mail
    page.click("text=E-Mail")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.email&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Teléfono
    page.click("text=Teléfono")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.telefono&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Vista
    page.click("text=Vista")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index/view/persona/1?order=persona.telefono&_signature=b9ce84649e3cdacb7bd38da86223c5840c41449d"

    # Click text=Atrás
    page.click("text=Atrás")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.telefono&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Editar
    page.click("text=Editar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index/edit/persona/1?order=persona.telefono&_signature=5ca1ac15e3f76cae30d075eda1dec5dd776dbc68"

    # Click text=Atrás
    page.click("text=Atrás")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?order=persona.telefono&_signature=757a993c643dc478b57b21486e68f722168946fc"

    # Click text=Eliminar
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.click("text=Eliminar")

    # Close page
    page.close()
