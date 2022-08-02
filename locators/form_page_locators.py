from selenium.webdriver.common.by import By


class FormPageLocators:

    CONTACT= (By.XPATH,'//*[@id="menu-osnovnoe-menyu-1"]/li/a')
    NAME= (By.XPATH,'//*[@id="wpcf7-f1729-p270-o2"]/form/p[1]/label/span/input')
    EMAIL = (By.XPATH, '//*[@id="wpcf7-f1729-p270-o2"]/form/p[2]/label/span/input')
    THEME = (By.XPATH, '//*[@id="wpcf7-f1729-p270-o2"]/form/p[3]/label/span/input')
    MESSAGE= (By.XPATH, '//*[@id="wpcf7-f1729-p270-o2"]/form/p[4]/label/span/textarea')
    BUTTOM= (By.XPATH, '//*[@id="wpcf7-f1729-p270-o2"]/form/p[5]/input')


