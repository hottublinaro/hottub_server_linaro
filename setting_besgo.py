from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_data_besgo"

class Setting_besgo:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE backwash SET backwash_state_1 = '"+data_json[0]['backwash_state_1']+"', backwash_start_1 = '"+data_json[0]['backwash_start_1']+"', backwash_end_1 = '"+data_json[0]['backwash_end_1']+"', backwash_status_1 = "+data_json[0]['backwash_status_1']+", backwash_state_2 = '"+data_json[0]['backwash_state_2']+"', backwash_start_2 = '"+data_json[0]['backwash_start_2']+"', backwash_end_2 = '"+data_json[0]['backwash_end_2']+"', backwash_status_2 = "+data_json[0]['backwash_status_2']+", backwash_state_3 = '"+data_json[0]['backwash_state_3']+"', backwash_start_3 = '"+data_json[0]['backwash_start_3']+"', backwash_end_3 = '"+data_json[0]['backwash_end_3']+"', backwash_status_3 = "+data_json[0]['backwash_status_3']+", backwash_state_4 = '"+data_json[0]['backwash_state_4']+"', backwash_start_4 = '"+data_json[0]['backwash_start_4']+"', backwash_end_4 = '"+data_json[0]['backwash_end_4']+"', backwash_status_4 = "+data_json[0]['backwash_status_4']+", backwash_mode = "+data_json[0]['backwash_mode']+", backwash_time = "+data_json[0]['backwash_time']+" WHERE backwash_id = 1"
       
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
