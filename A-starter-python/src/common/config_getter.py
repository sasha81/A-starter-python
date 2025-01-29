import configparser
import os
from typing import List, Dict, Any
import yaml
import re

def getConfig(path: str, args: Any, default_mode: str, trim: bool = True):
    if hasattr(args, "mode"):
        config = load_yml_config(path, args.mode, trim=trim)
    else:
        config = load_yml_config(path, default_mode, trim=trim)

    return config


def load_yml_config(path: str, mode: str, conf_inner_path: str= '/config', default_mode: str= 'prod', extension: str= 'yml', trim: bool = True):

    config = load_raw_config(path, conf_inner_path, mode, default_mode, extension)

    config = flatten_dict(config, separator='.')
    env_var_dict = dict(os.environ)
    config = update_config(config, env_var_dict)
    if trim is True:
        config = trim_config(config)
    return config

def load_raw_config(path: str,inner_path: str ,mode: str, default_mode: str='prod', extension: str='yml')-> Dict[str, Any]:
    file_names = os.listdir(path + inner_path)
    files = [i for i in file_names if i.endswith(extension)]
    files = [i.split('.')[0] for i in files]
    files = [i for i in files if i in mode]
    if len(files) > 0:
        config = load_yml(path + inner_path+'/'+files[0]+'.'+extension)
    else:
        config = load_yml(path + inner_path + '/' + f'{default_mode}.{extension}')
    return config


def trim_config(input_dict: Dict[str, Any])->Dict[str, Any]:
    output_dict ={}
    for key in input_dict.keys():
        output_dict[key.split('.')[1]] = input_dict[key]
    return output_dict


def get_config_path(path: str):
    path_current_directory = os.path.dirname(__file__)
    path_arr = path_current_directory.split("/")
    path_arr.pop()
    path_arr.append(path)
    config_path = "/".join(path_arr)
    return config_path


def update_config(config: Dict[str, Any], config_from_ext_vars: Dict[str,Any]):
    for key in config:
        if config_from_ext_vars.get(key) is not None:
            config[key] = config_from_ext_vars[key]
    return config


def load_yml(file_name: str):
    with open(file_name) as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        return dict

def flatten_dict(dd, separator='_', prefix=''):
    res = {}
    for key, value in dd.items():
        if isinstance(value, dict):
            res.update(flatten_dict(value, separator, prefix + key + separator))
        else:
            res[prefix + key] = value
    return res