from urllib.request import urlopen
import json
from connect_db import Connect_db
from path_url import Path_URL

connect_db = Connect_db
path_file = Path_URL

url = path_file.path_server+"api/Rest_api/get_filtration_data_time"

class Setting_filtration:

    def get_setting(machine_code):
        path_url = url+'?machine_code='+machine_code
        response = urlopen(path_url)
        data_json = json.loads(response.read())
        mydb = connect_db.update_setting_mode()

        mycursor = mydb.cursor()
        sql = "UPDATE filtration_time SET ft_status_1 = "+data_json[0]['ft_status_1']+", ft_status_2 = "+data_json[0]['ft_status_2']+", ft_status_3 = "+data_json[0]['ft_status_3']+", ft_status_4 = "+data_json[0]['ft_status_4']+", ft_status_5 = "+data_json[0]['ft_status_5']+", ft_status_6 = "+data_json[0]['ft_status_6']+", ft_status_7 = "+data_json[0]['ft_status_7']+", ft_status_8 = "+data_json[0]['ft_status_8']+", ft_status_9 = "+data_json[0]['ft_status_9']+", ft_status_10 = "+data_json[0]['ft_status_10']+", ft_status_11 = "+data_json[0]['ft_status_11']+", ft_status_12 = "+data_json[0]['ft_status_12']+", ft_status_13 = "+data_json[0]['ft_status_13']+", ft_status_14 = "+data_json[0]['ft_status_14']+", ft_status_15 = "+data_json[0]['ft_status_15']+", ft_status_16 = "+data_json[0]['ft_status_16']+", ft_status_17 = "+data_json[0]['ft_status_17']+", ft_status_18 = "+data_json[0]['ft_status_18']+", ft_status_19 = "+data_json[0]['ft_status_19']+", ft_status_20 = "+data_json[0]['ft_status_20']+", ft_status_21 = "+data_json[0]['ft_status_21']+", ft_status_22 = "+data_json[0]['ft_status_22']+", ft_status_23 = "+data_json[0]['ft_status_23']+", ft_status_24 = "+data_json[0]['ft_status_24']+" WHERE ft_id = 1"
        
        mycursor.execute(sql)
        mydb.commit()
        # data_json[0]['sm_filtration']
