# tests/test_login.py
def test_login_success(browser):
    browser.goto("https://the-internet.herokuapp.com/login")
    browser.fill("#username", "tomsmith")
    browser.fill("#password", "SuperSecretPassword!")
    browser.click("button[type='submit']")

    assert "Secure Area" in browser.content()
