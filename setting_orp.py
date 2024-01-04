from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_orp"

class Setting_orp:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE orp SET orp_1 = "+data_json[0]['orp_1']+", orp_2 = "+data_json[0]['orp_2']+", orp_3 = "+data_json[0]['orp_3']+", orp_4 = "+data_json[0]['orp_4']+", orp_5 = "+data_json[0]['orp_5']+", orp_6 = "+data_json[0]['orp_6']+", orp_7 = "+data_json[0]['orp_7']+", orp_8 = "+data_json[0]['orp_8']+", orp_9 = "+data_json[0]['orp_9']+", orp_10 = "+data_json[0]['orp_10']+", orp_11 = "+data_json[0]['orp_11']+", orp_12 = "+data_json[0]['orp_12']+", orp_13 = "+data_json[0]['orp_13']+", orp_14 = "+data_json[0]['orp_14']+", orp_15 = "+data_json[0]['orp_15']+", orp_16 = "+data_json[0]['orp_16']+", orp_17 = "+data_json[0]['orp_17']+", orp_18 = "+data_json[0]['orp_18']+", orp_19 = "+data_json[0]['orp_19']+", orp_20 = "+data_json[0]['orp_20']+", orp_21 = "+data_json[0]['orp_21']+", orp_22 = "+data_json[0]['orp_22']+", orp_23 = "+data_json[0]['orp_23']+", orp_24 = "+data_json[0]['orp_24']+" WHERE orp_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
