from setting_besgo import Setting_besgo
import time
setting_besgo = Setting_besgo

machine_code = "MA-202306-001"
while True:
    setting_besgo.get_setting(machine_code)
    time.sleep(2)
