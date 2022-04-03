import json
import os
from typing import List

from utils import fail, debug

class Config:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.password_vpn = ''
        self.email = ''
        self.district = ''
        self.inschool = ''
        self.campus = ''
        self.building = ''
        self.room = ''


def make_configs(json_str: str) -> List[Config]:
    try:
        dicts = json.loads(json_str)["config"]
        cfgs = []
        for d in dicts:
            c = Config()
            for key in c.__dict__.keys():
                setattr(c, key, d[key])
            cfgs.append(c)
        return cfgs
    except Exception as e:
        fail("配置读取失败，请检查配置", "配置错误", e=e, shutdown=True)

def get_configs() -> List[Config]:
    if debug:
        with open("config.json", encoding="utf8") as f:
            return make_configs(f.read())
    else:
        return make_configs(os.getenv("CONFIG"))