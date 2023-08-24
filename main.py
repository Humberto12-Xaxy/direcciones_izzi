from Data import Data
from map_bot import MapBot
import os
from dotenv import load_dotenv
from time import sleep


if __name__ == '__main__':
    load_dotenv()
    
    with MapBot() as map_bot:
        
        map_bot.get_url(os.getenv('URL_MAP'))
        map_bot.click_to_login()
        
        # Se cambia a la ventana emergente
        map_bot.change_window(1)
        
        # map_bot.get_url(os.getenv('URL_LOGIN'))
        #map_bot.click_to_login()
        map_bot.click_to_izzi_button()
        map_bot.fill_email_input(os.getenv('EMAIL'))
        map_bot.fill_password_input(os.getenv('PASSWORD'))
        map_bot.click_to_maintain_session()
        map_bot.change_window(0)
        
        data = Data('./Chihuahua1.xlsx')
        list_address = data.get_address()
        # ARROYO EL ALAMO 16701,31000
        map_bot.search_one_address('ARROYO EL ALAMO 16701,31000')
        # all_address = map_bot.search_address(list_address)
        # print(all_address)
        # data.add_address_to_excel(all_address)