from selenium import webdriver
from selenium.webdriver.common.by import By
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
        sleep(1)

    def fill_password_input(self, password:str):
       
        password_input = self.find_element(By.XPATH, '//*[@id="i0118"]')
        password_input.send_keys(password)
        sleep(1)
       
        login_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        login_button.click()
        sleep(1)

    def click_to_maintain_session(self):
       
        no_button = self.find_element(By.XPATH, '//*[@id="idBtn_Back"]')
        no_button.click()
        sleep(20)
    
    # un resultado: ARROYO EL POZO 2248,31125
    # mas de un resultado: ARROYO MARGARITAS 2208,31126
    def seach_address(self, list_address:list):
        
        all_address = []
        for address in list_address:
            search_input = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_input"]')
            search_input.send_keys(address)
            sleep(1)

            search_button = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0"]/div/div[2]')
            search_button.click()
            sleep(1)

            search_input.clear()
            sleep(7)

            address = self.get_address_complete()
            all_address.append(address)
        
        return all_address


    
    def get_address_complete(self):
        
        list_address = []
        full_address = ''
        address = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_more_results"]/div[1]')
        full_address = address.text
        # En este caso voy a verificar si esta etiqueta contiene mas elementos
        more_items = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_more_results"]/div[2]')

        if more_items.text:
            a_more_items = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_more_results_show"]')
            a_more_items.click()
            sleep(3)

            items = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_more_results_list"]/ul')  
            full_address = f'{full_address}, {items.text}'
            print(full_address) 
            list_address.append(full_address)
        
        else:
            print(full_address) 
            list_address.append(full_address)

        return list_address
