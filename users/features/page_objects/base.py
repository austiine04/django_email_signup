from lettuce.django import django_url


class PageObject(object):

    def __init__(self, browser):
        self.browser = browser

    def visit(self):
        self.browser.visit(django_url(self.url))

    def fill(self, name, text):
        self.browser.fill(name, text)

    def click(self, name):
        self.browser.find_by_name(name).click()
        self.url = self.browser.url

    def is_element_present(self, name):
        return self.browser.is_element_present_by_xpath(name)

    def is_current_url(self, url):
        return self.url == django_url(url)

    def is_text_present(self, text):
        return self.browser.is_text_present(text)

    def text_is_not_present(self, text):
        return self.browser.is_text_not_present(text)



