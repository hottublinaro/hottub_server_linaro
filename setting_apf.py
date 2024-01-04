from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_apf"

class Setting_apf:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE apf SET apf_1 = "+data_json[0]['apf_1']+", apf_2 = "+data_json[0]['apf_2']+", apf_3 = "+data_json[0]['apf_3']+", apf_4 = "+data_json[0]['apf_4']+", apf_5 = "+data_json[0]['apf_5']+", apf_6 = "+data_json[0]['apf_6']+", apf_7 = "+data_json[0]['apf_7']+", apf_8 = "+data_json[0]['apf_8']+", apf_9 = "+data_json[0]['apf_9']+", apf_10 = "+data_json[0]['apf_10']+", apf_11 = "+data_json[0]['apf_11']+", apf_12 = "+data_json[0]['apf_12']+", apf_13 = "+data_json[0]['apf_13']+", apf_14 = "+data_json[0]['apf_14']+", apf_15 = "+data_json[0]['apf_15']+", apf_16 = "+data_json[0]['apf_16']+", apf_17 = "+data_json[0]['apf_17']+", apf_18 = "+data_json[0]['apf_18']+", apf_19 = "+data_json[0]['apf_19']+", apf_20 = "+data_json[0]['apf_20']+", apf_21 = "+data_json[0]['apf_21']+", apf_22 = "+data_json[0]['apf_22']+", apf_23 = "+data_json[0]['apf_23']+", apf_24 = "+data_json[0]['apf_24']+" WHERE apf_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
