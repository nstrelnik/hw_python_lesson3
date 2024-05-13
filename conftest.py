import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_window_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print("Размер окна установлен")
    yield
    browser.quit()
