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
    
    def change_window(self, index):
        self.switch_to.window(self.window_handles[index])

    def click_to_login(self):
        login_button = self.find_element(By.XPATH, '//html/body/div[5]/div[2]/div/div[5]/span[1]')
        login_button.click()
        sleep(10)

    def click_to_izzi_button(self):
        izzi_button = self.find_element(By.XPATH, '//html/body/div/div/div[2]/div/div[2]/section[1]/div/div/div')
        izzi_button.click()
        sleep(10)

    def fill_email_input(self, email:str):
        email_input = self.find_element(by= By.XPATH, value= '//*[@id="i0116"]')
        email_input.send_keys(email)
        sleep(1)

        next_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        next_button.click()
        sleep(3)

    def fill_password_input(self, password:str):
       
        password_input = self.find_element(By.XPATH, '//*[@id="i0118"]')
        password_input.send_keys(password)
        sleep(1)
       
        login_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        login_button.click()
        sleep(3)

    def click_to_maintain_session(self):
        
        check = self.find_element(By.XPATH,'//*[@id="KmsiCheckboxField"]')
        check.click()
        
        sleep(3)
       
        si_button = self.find_element(By.XPATH, '//*[@id="idSIButton9"]')
        si_button.click()
        sleep(12)
    
    def search_address(self, list_address:list):
        
        all_address:list = []
        self.close_searcher()
        for i, address in enumerate(list_address):
            
            print(i+1)
            all_address.append(self.search_one_address(address))

        
        return all_address

    def search_one_address(self, address:str):

        self.input_search(address)

        self.add_a_maker()
        self.click_maker()
        data = self.get_data()
        self.delete_marker()

        return data


    def add_a_maker(self):

        points = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[3]/div/div/span')
        points.click()
        sleep(6)

        add_maker = self.find_element(By.XPATH, '//html/body/div[4]/div/div[2]/div[2]')
        add_maker.click()
        sleep(1)

    def click_maker(self):
        active = ActionChains(self)
        maker = self.find_element(By.XPATH, '//div[@id="map_gc"]//*[@id="marker-feature-action-layer_layer"]')
        active.move_to_element(maker).click().perform()
        sleep(1)

      
    
    def get_data(self):
        flag = self.label_name()
        if flag != 'Name':
            self.next_button()
        
        sleep(10)
        try:
            head = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[2]')
            if (head.text == '(2 of 2)' or head.text == '(3 of 3)' or head.text == '(3 of 4)' or head.text == '(2 of 3)') or flag == 'Name':
                name = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[1]/td[2]')
                # sleep(.5)
                hub = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[2]/td[2]')
                # sleep(.5)
                rama = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[3]/td[2]')
                # sleep(.5)
                nodo = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[4]/td[2]')
                # sleep(.5)
                x_tt_hfc_flg = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[5]/td[2]')
                # sleep(.5)
                x_tt_rpt_codigo = self.find_element(By.XPATH, '//*/table[@class="attrTable"]//*/td/span')
                sleep(.5)
                
                final_value = f'Name: {name.text}, HUB: {hub.text}, Rama: {rama.text}, Nodo: {nodo.text}, X_TT_HFC_FLG: {x_tt_hfc_flg.text}, X_TT_RPT_CODIGO: {x_tt_rpt_codigo.text}'
                print(final_value)

                return final_value
            
            else:
                return None

        except Exception as e:
            print(f'Error: {e}')
            return None
    
    def close_searcher(self):
        action = ActionChains(self)
        close_button = self.find_element(By.XPATH, '//*[@id="_7_panel"]/div[1]/div/div[3]')
        action.move_to_element(close_button).click().perform()
        sleep(1)
        
    def delete_marker(self):
        head = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[2]')
        
        if (head.text == '(1 of 2)' or head.text == '(1 of 3)' or head.text == '(1 of 4)' ) and self.label_name() == 'Name':
            self.next_button()
        
        if (head.text == '(2 of 2)' or head.text == '(3 of 3)' or head.text == '(3 of 4)' or head.text == '(2 of 3)') and self.label_name() == 'Name':
            self.prev_button()
        


        points = self.find_element(By.XPATH, '//div[@class="sizer"]//*/span[@class="popup-menu-button"]')
        points.click()
        sleep(1)
        
        remove_button = self.find_element(By.XPATH, '//html/body/div[4]/div/div[2]/div[2]')
        remove_button.click()
        sleep(1)
    
    def prev_button(self):

        back_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[3]')
        back_button.click()
        sleep(1)
    
    def next_button(self):
        head_maker = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[2]')
        
        if (head_maker.text == '(1 of 4)' or head_maker.text == '(1 of 3)') and self.label_name() != 'Name':

            next_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')
            next_button.click()
            sleep(.5)
            if (head_maker.text == '(2 of 3)' or head_maker.text == '(2 of 4)') and self.label_name() != 'Name':
                next_button.click()
                sleep(.5)

        elif head_maker.text == '(1 of 2)' and self.label_name() != 'Name':

            next_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')
            next_button.click()
            sleep(.5)
        
        elif (head_maker.text == '(1 of 2)' or head_maker.text == '(1 of 4)' or head_maker.text == '(1 of 3)') and self.label_name() == 'Name':

            next_button = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[4]')
            next_button.click()
            sleep(.5)
        
    
    def input_search(self, address):
        search_input = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0_input"]')
        search_input.send_keys(address)
        sleep(1)

        search_button = self.find_element(By.XPATH, '//*[@id="esri_dijit_Search_0"]/div/div[2]')
        search_button.click()
        sleep(.5)

        search_input.clear()
        sleep(1.5)      
    
    def label_name(self):

        try:
            label_name = self.find_element(By.XPATH, '//*/div[@class= "esriPopupWrapper"]//*/div[@class="mainSection"]//*/table[@class="attrTable"]/tr[1]/td[1]')
            return label_name.text
        
        except Exception as e:
            return None
    def head_label(self):
        head_label = self.find_element(By.XPATH, '//*[@id="map_root"]/div[3]/div[1]/div[1]/div/div[2]')
        return head_label.text