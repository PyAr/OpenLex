from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:8020/OpenLex/default/index
    page.goto("http://127.0.0.1:8020/OpenLex/default/index")

    # Click text=Log In
    page.click("text=Log In")

    # Click text=¿Olvidó la contraseña?
    page.click("text=¿Olvidó la contraseña?")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index"

    # Click text=Solicitar reinicio de contraseña
    page.click("text=Solicitar reinicio de contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index#"

    # Triple click input[name="email"]
    page.click("input[name=\"email\"]", click_count=3)

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")

    # Click text=Solicitar reinicio de contraseña
    page.click("text=Solicitar reinicio de contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index#"

    # Click text=OpenLex/127.0.0.1.2021-06-27.21-46-16.f49647e5-6f93-4b47-a330-f3bfb4f6ba1a
    with page.expect_popup() as popup_info:
        page.click("text=OpenLex/127.0.0.1.2021-06-27.21-46-16.f49647e5-6f93-4b47-a330-f3bfb4f6ba1a")
    page1 = popup_info.value

    # Fill input[name="password"]
    page1.fill("input[name=\"password\"]", "openlex1234")

    # Press Enter
    page1.press("input[name=\"password\"]", "Enter")
    # assert page1.url == "http://127.0.0.1:8020/admin/default/ticket/OpenLex/127.0.0.1.2021-06-27.21-46-16.f49647e5-6f93-4b47-a330-f3bfb4f6ba1a"

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)