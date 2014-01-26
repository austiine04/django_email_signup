from users.features.page_objects.base import PageObject


class SignupPage(PageObject):

    def __init__(self, browser, url):
        PageObject.__init__(self, browser)
        self.url = url