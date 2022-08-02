from pages.form_page import FormPage


class TestFormPage:

    def test_form(self,driver):
        form_page= FormPage(driver,'https://planetforme.ru/')
        form_page.open()
        form_page.fill_fields_and_submit()


