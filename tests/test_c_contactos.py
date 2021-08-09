# Acá realizaremos un testing de la funcionalidad de carga y eliminación de contactos.

def test_contactos(page, login):
    # Click text=Contactos
    page.click("text=Contactos")
    assert page.url.endswith("/contactos/index")

    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")

    # Select F
    page.select_option("select[name=\"sexo\"]", "F")

    # Click input[name="apellido"]
    page.click("input[name=\"apellido\"]")

    # Fill input[name="apellido"]
    page.fill("input[name=\"apellido\"]", "Gonzalez")
    page.press("input[name=\"apellido\"]", "Tab")

    # Click input[name="nombre"]
    page.click("input[name=\"nombre\"]")

    # Fill input[name="nombre"]
    page.fill("input[name=\"nombre\"]", "María Juana")
    page.press("input[name=\"nombre\"]", "Tab")

    # Click input[name="cuitcuil"]
    page.click("input[name=\"cuitcuil\"]")

    # Fill input[name="cuitcuil"]
    page.fill("input[name=\"cuitcuil\"]", "20111111115")
    page.press("input[name=\"cuitcuil\"]", "Tab")

    # Click input[name="domicilio"]
    page.click("input[name=\"domicilio\"]")

    # Fill input[name="domicilio"]
    page.fill("input[name=\"domicilio\"]", "Avenida del Software Libre 1984, Ciudad GNU")
    page.press("input[name=\"domicilio\"]", "Tab")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "mariajuana@example.com")
    page.press("input[name=\"email\"]", "Tab")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Click input[name="telefono"]
    page.click("input[name=\"telefono\"]")

    # Fill input[name="telefono"]
    page.fill("input[name=\"telefono\"]", "1166666666")
    page.press("input[name=\"telefono\"]", "Tab")

    # Click input[name="celular"]
    page.click("input[name=\"celular\"]")

    # Fill input[name="celular"]
    page.fill("input[name=\"celular\"]", "1177777777")
    page.press("input[name=\"celular\"]", "Tab")

    # Click input[name="matricula"]
    page.click("input[name=\"matricula\"]")

    # Fill input[name="matricula"]
    page.fill("input[name=\"matricula\"]", "666777")
    page.press("input[name=\"matricula\"]", "Tab")

    # Click text=Enviar
    page.click("text=Enviar")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/contactos/index?_signature=757a993c643dc478b57b21486e68f722168946fc#"
    
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
