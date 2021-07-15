from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# usei o firefox, mas pode usar chrome, opera

# Obs o diretorio do webdriver


class FirefoxWhats():
    def FirefoxWhatsapp(self):
        self.drive_whatsapp = webdriver.Firefox(
            executable_path=r'D:\\Projetos\\Python\\BotWhatsapp\\virtual\\Include\\geckodriver.exe')
        self.drive_whatsapp.get('https://web.whatsapp.com/')

        while True:  # Verificar se foi realizado o "Login"
            try:
                self.drive_whatsapp.find_element_by_xpath(
                    '//div[contains(@class, "YtmXM")]')
                break
            except:
                pass
        return self.drive_whatsapp

    def contatos(self, contato):
        pesquisa = self.drive_whatsapp.find_element_by_xpath(
            '//div[contains(@class, "copyable-text selectable-text")]')
        time.sleep(3)
        pesquisa.click()
        pesquisa.send_keys(contato)
        time.sleep(5)
        pesquisa.send_keys(Keys.ENTER)

    def send_Mensagem(self, msg):
        mensagem = self.drive_whatsapp.find_elements_by_xpath(
            '//div[contains(@class, "copyable-text selectable-text")]')
        mensagem[1].click()
        mensagem[1].send_keys(msg)
        time.sleep(5)
        mensagem[1].send_keys(Keys.ENTER)
