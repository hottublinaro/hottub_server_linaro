from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_substance"

class Setting_substance:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE substance SET ph_set = "+data_json[0]['ph_set']+", ph_lower = "+data_json[0]['ph_lower']+", ph_inj = "+data_json[0]['ph_inj']+", ph_freq = "+data_json[0]['ph_freq']+", orp_set = "+data_json[0]['orp_set']+", orp_lower = "+data_json[0]['orp_lower']+", orp_inj = "+data_json[0]['orp_inj']+", orp_freq = "+data_json[0]['orp_freq']+", apf_set = "+data_json[0]['apf_set']+", apf_lower = "+data_json[0]['apf_lower']+", apf_inj = "+data_json[0]['apf_inj']+", apf_freq = "+data_json[0]['apf_freq']+" WHERE substance_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
