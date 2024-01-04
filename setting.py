from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_data_setting"

class Setting:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE setting SET setting_temperature = "+data_json[0]['setting_temperature']+", setting_aeau = "+data_json[0]['setting_aeau']+", setting_eau = "+data_json[0]['setting_eau']+", setting_systeme = "+data_json[0]['setting_systeme']+", setting_temp_deff = "+data_json[0]['setting_temp_deff']+", setting_basse = "+data_json[0]['setting_basse']+", setting_haute = "+data_json[0]['setting_haute']+", setting_tentative = "+data_json[0]['setting_tentative']+", setting_frequence = "+data_json[0]['setting_frequence']+" WHERE setting_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
