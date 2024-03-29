import time
from datetime import datetime
from setting_mode import Setting_mode
from setting_ph import Setting_ph
from setting_orp import Setting_orp
from setting_apf import Setting_apf
from setting_chlorine import Setting_chlorine
from setting_filtration import Setting_filtration
from setting import Setting
from setting_besgo import Setting_besgo
from setting_substance import Setting_substance
from urllib.request import urlopen
import json
from path_url import Path_URL
from setting_dashboard import Setting_dashboard
import SDL_DS3231


setting_mode = Setting_mode
setting_ph = Setting_ph
setting_orp = Setting_orp
setting_apf= Setting_apf
setting_chlorine = Setting_chlorine
setting_filtration = Setting_filtration
setting = Setting
setting_besgo = Setting_besgo
setting_substance = Setting_substance
path_file = Path_URL
setting_dashboard = Setting_dashboard

ds3231 = SDL_DS3231.SDL_DS3231(6, 0x68)

machine_code = ""
path_url = path_file.path_local+"api/Rest_api/get_data_setting"
while True:
    try:
        read_machine_code = open("/home/linaro/machine_code/machine_code.txt", "r")
        machine_code = read_machine_code.read().rstrip('\n')
        if machine_code != '':
            modult_rtc = str(ds3231.read_datetime())

            # print(get_i2c)
            split_date_time_rtc = modult_rtc.split(" ") 
            split_date_rtc = split_date_time_rtc[0].split("-")
            split_time_rtc = split_date_time_rtc[1].split(":")
            # print(split_date)
            # print(split_time)
            system_time = datetime(int(split_date_rtc[0]), int(split_date_rtc[1]), int(split_date_rtc[2]), int(split_time_rtc[0]), int(split_time_rtc[1]), int(split_time_rtc[2]))

            # now = datetime.now()
            dt_string = system_time.strftime("%Y-%m-%d %H:%M:%S")
            response = urlopen(path_url)
            data_json = json.loads(response.read())
            if int(data_json[0]['online_status']) == 1:
                print("working online")
                setting_mode.get_setting(machine_code)
                setting_ph.get_setting(machine_code)
                setting_orp.get_setting(machine_code)
                setting_apf.get_setting(machine_code)
                setting_chlorine.get_setting(machine_code)
                setting_filtration.get_setting(machine_code)
                setting.get_setting(machine_code)
                setting_besgo.get_setting(machine_code)
                setting_substance.get_setting(machine_code)
                setting_dashboard.get_setting(machine_code, dt_string)
                time.sleep(1)
            else:
                print("working offline")
                time.sleep(3)

    except:
        pass
   

   
