from Data import Data
from map_bot import MapBot
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    
    with MapBot() as map_bot:
        map_bot.get_url(os.getenv('URL_LOGIN'))
        # map_bot.click_to_login()
        map_bot.click_to_izzi_button()
        map_bot.fill_email_input(os.getenv('EMAIL'))
        map_bot.fill_password_input(os.getenv('PASSWORD'))
        map_bot.click_to_maintain_session()

        map_bot.get_url(os.getenv('URL_MAP'))
        map_bot.click_to_login()

        data = Data('./Chihuahua1.xlsx')
        list_address = data.get_address()
        all_address = map_bot.seach_address(list_address)

        data.add_address_to_excel(all_address)