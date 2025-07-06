# tests/test_logout.py

def test_logout_flow(browser):
    browser.goto("https://the-internet.herokuapp.com/login")
    browser.fill("#username", "tomsmith")
    browser.fill("#password", "SuperSecretPassword!")
    browser.click("button[type='submit']")

    assert "Secure Area" in browser.content()

    # Simulamos que hay un botón de logout y lo clicamos
    # (este sitio demo no tiene logout funcional real, pero en uno real sería algo así)
    browser.click('a[href="/logout"]')
    assert "You logged out" in browser.content()

    print("✅ Simulación de logout exitosa")
