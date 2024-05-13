from selene import browser, be, have

def test_search_from_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_from_google_not_find():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qweqweqwe').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))