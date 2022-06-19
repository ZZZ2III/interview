import requests
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def download_html_from_dude(url: str):
    with open('test.xml', 'wb+') as f:
        req = requests.get(url)
        f.write(req.content)

def parseXML(path:str):
        data = []
        price_data = []
        sklad_data = []
        data_id = []
        base_price = []
        base_disc_price = []
        sklad_id = []
        sklad_amount = []
        file_name = path
        xml_file = ET.parse(file_name)
        root = xml_file.getroot()

        for product_id in root.iter('product'):# Here we parsing Xml doc
            data.append(product_id.attrib)
        for price in root.iter("price"):
            price_data.append(price.attrib)
        for sklad in root.iter("assort"):
            sklad_data.append(sklad.attrib)

        for i in range(0, len(data)): #Here we choose what data we need for json
            z = data[i]['prodID']
            data_id.append(z)
        for i in range(0, len(price_data)):
            z = price_data[i]['RetailPrice']
            z1 = price_data[i]['WholePrice']
            base_price.append(z1)
            base_disc_price.append(z)
        for i in range(0,len(sklad_data)):
            z = sklad_data[i]["aID"]
            z1 = sklad_data[i]["sklad"]
            sklad_id.append(z)
            sklad_amount.append(z1)

        for i in range(0, 51): # Now we are trying to make requests
            updating_prices = {"product_id": f'{data_id[i]}',"multiple_sku_update_list": [{"price": f"{base_price[i]}","discount_price": f"{base_disc_price[i]}","sku_code": f"{sklad_id[i]}"}]}
            updating_prices_req = requests.post('https://aliexpress.ru/', params="aliexpress.solution.batch.product.price.update", json=json.dumps(updating_prices))
            print(updating_prices_req)
            updating_products = {"product_id": f'{data_id[i]}',"multiple_sku_update_list": [{"inventory": f"{sklad_amount[i]}","sku_code": f"{sklad_id[i]}"}]}
            updating_products_req = requests.post('https://aliexpress.ru/', params="aliexpress.solution.batch.product.inventory.update", json=json.dumps(updating_products))
            print(updating_products)

my_url = 'http://stripmag.ru/datafeed/p5s_full_stock.xml'

download_html_from_dude(my_url)

parseXML('test.xml')


