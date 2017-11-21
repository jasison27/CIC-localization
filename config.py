from configparser import ConfigParser
import json

class Config():

    serial_name = ""
    zones = None
    dynamic_tags = None
    anchors = None
    background = ''

    @staticmethod
    def load_config():
        conf = ConfigParser()
        conf.read("settings.conf")
        Config.serial_name = conf.get("serial","serial_name")
        json_raw = conf.get("anchor","anchor_setting")
        Config.anchors = json.loads(json_raw)
        json_raw = conf.get("tag","dynamic_tag")
        Config.dynamic_tags = json.loads(json_raw)
        json_raw = conf.get("zone","dangerous_zone")
        Config.zones = json.loads(json_raw)



    @staticmethod
    def save_config():
        conf =ConfigParser()
        conf.add_section('serial')
        conf.set('serial','serial_name',Config.serial_name)
        conf.add_section('anchor')
        conf.set('anchor','anchor_setting',json.dumps(Config.anchors))
        conf.add_section('tag')
        conf.set('tag','dynamic_tag',json.dumps(Config.dynamic_tags))
        conf.add_section('zone')
        conf.set('zone','dangerous_zone',json.dumps(Config.zones))
        conf.add_section('plot')
        with open('settings.conf','w') as f:
            conf.write(f)

