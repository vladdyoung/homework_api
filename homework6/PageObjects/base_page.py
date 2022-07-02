class BasePage:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open(self):
        self.browser.get(self.base_url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except Exception:
            return False
