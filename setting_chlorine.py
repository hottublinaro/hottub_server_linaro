from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_chlorine"

class Setting_chlorine:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE chlorine SET chlorine_1 = "+data_json[0]['chlorine_1']+", chlorine_2 = "+data_json[0]['chlorine_2']+", chlorine_3 = "+data_json[0]['chlorine_3']+", chlorine_4 = "+data_json[0]['chlorine_4']+", chlorine_5 = "+data_json[0]['chlorine_5']+", chlorine_6 = "+data_json[0]['chlorine_6']+", chlorine_7 = "+data_json[0]['chlorine_7']+", chlorine_8 = "+data_json[0]['chlorine_8']+", chlorine_9 = "+data_json[0]['chlorine_9']+", chlorine_10 = "+data_json[0]['chlorine_10']+", chlorine_11 = "+data_json[0]['chlorine_11']+", chlorine_12 = "+data_json[0]['chlorine_12']+", chlorine_13 = "+data_json[0]['chlorine_13']+", chlorine_14 = "+data_json[0]['chlorine_14']+", chlorine_15 = "+data_json[0]['chlorine_15']+", chlorine_16 = "+data_json[0]['chlorine_16']+", chlorine_17 = "+data_json[0]['chlorine_17']+", chlorine_18 = "+data_json[0]['chlorine_18']+", chlorine_19 = "+data_json[0]['chlorine_19']+", chlorine_20 = "+data_json[0]['chlorine_20']+", chlorine_21 = "+data_json[0]['chlorine_21']+", chlorine_22 = "+data_json[0]['chlorine_22']+", chlorine_23 = "+data_json[0]['chlorine_23']+", chlorine_24 = "+data_json[0]['chlorine_24']+" WHERE chlorine_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
