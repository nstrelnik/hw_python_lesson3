from selene import browser, be, have


def test_search_from_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_from_google_not_find_text():
    browser.open("https://google.ru")
    browser.element('[name="q"]').should(be.blank).type('uryytyweuiyruuyt!!!fs,jhjhs').press_enter()
    browser.element('#botstuff').should(have.text('По запросу uryytyweuiyruuyt!!!fs,jhjhs ничего не найдено.'))




