def test_groups(page, login):
    page.click("text=Bienvenido")
    page.click("text=Inicio")
    page.click("text=Bienvenido")
    # Click text=Grupos
    page.click("text=Grupos")
    assert page.url.endswith("/groups/groups")
    # Click text=Crear grupos
    page.click("text=Crear grupos")
    assert page.url.endswith("/groups/create_groups")
    # Click a:has-text("Agregar")
    page.click("a:has-text(\"Agregar\")")
    assert page.url.endswith("/groups/create_groups/new/auth_group")
    # Click input[name="role"]
    page.click("input[name=\"role\"]")
    page.fill("input[name=\"role\"]", "Nuevo")
    # Click textarea[name="description"]
    page.click("textarea[name=\"description\"]")
    # Fill textarea[name="description"]
    page.fill("textarea[name=\"description\"]", "Grupo de prueba")
    # Click text=Enviar
    page.click("text=Enviar")
    assert page.url.endswith("/groups/create_groups#")
    # Click text=Grupos
    page.click("text=Grupos")
    assert page.url.endswith("/groups/groups")
    # Click text=Agregar
    page.click("text=Agregar")
    assert page.url.endswith("/groups/groups/new/auth_membership")

