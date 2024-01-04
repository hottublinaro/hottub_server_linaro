from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL
import requests


connect_db = Connect_db
path_file = Path_URL


url = path_file.path_local+"api/Rest_api/get_dashborad"
url_server = path_file.path_server+'api/Receive_api/get_dashboard' 

class Setting_dashboard:

    def get_setting(machine_code, dt_string):
        response = urlopen(url)
        data_json = json.loads(response.read())
        resp = requests.post(url_server, data={'datetime':dt_string,
                                            'pressure': data_json[0]['pressure'],
                                            'ph':data_json[0]['ph'],
                                            'orp':data_json[0]['orp'],
                                            'temperature':data_json[0]['temperature'],
                                            'filtration':data_json[0]['filtration'],
                                            'pompe_ozone':data_json[0]['pompe_ozone'],
                                            'chauffage':data_json[0]['chauffage'],
                                            'chauffage2':data_json[0]['chauffage2'],
                                            'lamp_zone1':data_json[0]['lamp_zone1'],
                                            'lamp_zone2':data_json[0]['lamp_zone2'],
                                            'lamp_uv':data_json[0]['lamp_uv'],
                                            'volt_1':data_json[0]['volt_1'],
                                            'volt_2':data_json[0]['volt_2'],
                                            'volt_3':data_json[0]['volt_3'],
                                            'machine_code':machine_code,
                                            'max_pressure':data_json[0]['max_pressure'],
                                            'min_pressure':data_json[0]['min_pressure'],
                                            "plc_in":data_json[0]['plc_in'],
                                            "plc_out":data_json[0]['plc_out'],
                                            "relay_ch":data_json[0]['relay_ch'],
                                            "count_down":data_json[0]['count_down']
                                               })

       
        # data_json[0]['sm_filtration']
