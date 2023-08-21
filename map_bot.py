from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


class MapBot(webdriver.Chrome):
    def __init__(self, teardown = False) -> None:
        
        self.teardown = teardown
        super().__init__()
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def get_url(self, url:str):
        self.get(url)
        sleep(20)

    def click_to_login(self):
        login_button = self.find_element(By.XPATH, '//html/body/div[5]/div[2]/div/div[5]/span[1]')
        login_button.click()
        sleep(10)

    def click_to_izzi_button(self):
        izzi_button = self.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/section[1]/div/div/div')
        izzi_button.click()
        sleep(10)

    def fill_email_input(self, email:str):
        email_input = self.find_element(by= By.XPATH, value= '//*[@id="i0116"]')
        email_input.send_keys(email)
        sleep(1)

        next_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        next_button.click()
        sleep(5)

    def fill_password_input(self, password:str):
       
        password_input = self.find_element(By.XPATH, '//*[@id="i0118"]')
        password_input.send_keys(password)
        sleep(1)
       
        login_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        login_button.click()
        sleep(5)

    def click_to_maintain_session(self):
       
        no_button = self.find_element(By.XPATH, '//*[@id="idBtn_Back"]')
        no_button.click()
        sleep(20)
    
    # un resultado: ARROYO EL POZO 2248,31125
    # mas de un resultado: ARROYO MARGARITAS 2208,31126
    def seach_address(self, list_address:list):
        
        all_address = []
        self.close_searcher()
        for address in list_address:
            
            search_input = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_input"]')
            search_input.send_keys(address)
            sleep(1)

            search_button = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0"]/div/div[2]')
            search_button.click()
            sleep(1)

            self.add_a_maker()
            self.click_maker()
            all_address.append(self.get_data())

            search_input.clear()
            sleep(1)

        
        return all_address

    def search_one_address(self, address:str):
        search_input = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_input"]')
        search_input.send_keys(address)
        sleep(1)

        search_button = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0"]/div/div[2]')
        search_button.click()
        sleep(3)

        self.add_a_maker()
        self.click_maker()
        self.get_data()

        search_input.clear()
        sleep(1)

    def add_a_maker(self):

        points = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[3]/div/div/span')
        points.click()
        sleep(15)

        add_maker = self.find_element(By.XPATH, '//html/body/div[4]/div/div[2]/div[2]')
        add_maker.click()
        sleep(10)

    def click_maker(self):

        action = ActionChains(self)
        maker = self.find_element(By.XPATH, '//div[@id="map_gc"]//*[@id="marker-feature-action-layer_layer"]')
        action.move_to_element(maker).click().perform()
        # maker.click()
        sleep(2)

        head_maker = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[2]')
        print(head_maker.text)
        if head_maker.text == '(1 of 4)' or head_maker.text == '(1 of 3)':

            next_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')
            next_button.click()
            sleep(2)
            next_button.click()
            sleep(2)

        elif head_maker.text == '(1 of 2)':

            next_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')
            next_button.click()
            sleep(2)
    
    def get_data(self):
        
        name = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[1]/td[2]')
        sleep(1)
        hub = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[2]/td[2]')
        sleep(1)
        rama = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[3]/td[2]')
        sleep(1)
        nodo = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[4]/td[2]')
        sleep(1)
        x_tt_hfc_flg = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[5]/td[2]')
        sleep(1)
        x_tt_rpt_codigo = self.find_element(By.XPATH, '//*/table[@class="attrTable"]//*/td/span')
        sleep(1)

        return [name.text, hub.text, rama.text, nodo.text, x_tt_hfc_flg.text, x_tt_rpt_codigo.text]
    
    def close_searcher(self):
        action = ActionChains(self)
        close_button = self.find_element(By.XPATH, '//*[@id="_7_panel"]/div[1]/div/div[3]')
        action.move_to_element(close_button).click().perform()
        sleep(3)