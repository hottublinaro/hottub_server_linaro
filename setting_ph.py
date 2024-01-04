from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_ph"

class Setting_ph:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE ph SET ph_1 = "+data_json[0]['ph_1']+", ph_2 = "+data_json[0]['ph_2']+", ph_3 = "+data_json[0]['ph_3']+", ph_4 = "+data_json[0]['ph_4']+", ph_5 = "+data_json[0]['ph_5']+", ph_6 = "+data_json[0]['ph_6']+", ph_7 = "+data_json[0]['ph_7']+", ph_8 = "+data_json[0]['ph_8']+", ph_9 = "+data_json[0]['ph_9']+", ph_10 = "+data_json[0]['ph_10']+", ph_11 = "+data_json[0]['ph_11']+", ph_12 = "+data_json[0]['ph_12']+", ph_13 = "+data_json[0]['ph_13']+", ph_14 = "+data_json[0]['ph_14']+", ph_15 = "+data_json[0]['ph_15']+", ph_16 = "+data_json[0]['ph_16']+", ph_17 = "+data_json[0]['ph_17']+", ph_18 = "+data_json[0]['ph_18']+", ph_19 = "+data_json[0]['ph_19']+", ph_20 = "+data_json[0]['ph_20']+", ph_21 = "+data_json[0]['ph_21']+", ph_22 = "+data_json[0]['ph_22']+", ph_23 = "+data_json[0]['ph_23']+", ph_24 = "+data_json[0]['ph_24']+" WHERE ph_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
