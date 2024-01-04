from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_setting_mode"

class Setting_mode:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE setting_mode SET sm_filtration = "+data_json[0]['sm_filtration']+", sm_bypass = "+data_json[0]['sm_bypass']+", sm_ozone_choc = "+data_json[0]['sm_ozone_choc']+", sm_chauffage = "+data_json[0]['sm_chauffage']+", sm_pomp_ozone = "+data_json[0]['sm_pomp_ozone']+", sm_lamp_ozone = "+data_json[0]['sm_lamp_ozone']+", sm_lamp_uv = "+data_json[0]['sm_lamp_uv']+", sm_pump_air = "+data_json[0]['sm_pump_air']+" WHERE sm_id = 1 "
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
