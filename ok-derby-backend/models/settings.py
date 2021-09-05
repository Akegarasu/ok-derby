import logging
import os
import json
from utils.util import app_path
from typing import Dict, Text, List, Optional, Tuple

AUTO_DERBY_CONFIG_CLASS = None
logger = logging.getLogger(__name__)
BASE_PATH = app_path()
CONFIG_PATH = os.path.join(BASE_PATH, "ok_derby_config.json")
SETTINGS = {}


def _parse_training_levels(spec: Text) -> Dict[int, int]:
    ret: Dict[int, int] = {}
    for k, v in zip(
            (1, 2, 3, 4, 5),
            spec.split(","),
    ):
        if not v:
            continue
        ret[k] = int(v)
    return ret


def _unparse_training_levels(spec: Dict[int, int]) -> Text:
    ret: str = ","
    return ret.join([str(v) for k, v in spec.items()])


# def _parse_plugins(spec: Text) -> Tuple:
#     return tuple(i for i in spec.split(",") if i)

# def _unparse_plugins(spec: Tuple) -> Text:
#     ret = ",".join(list(spec))
#     return ret

DEFAULT_SETTINGS = {
    "ADB_ADDRESS": "",
    # "PLUGINS": tuple(),
    "use_legacy_screenshot": False,
    "ocr_data_path": "ocr_labels.json",
    "ocr_image_path": "",
    "ocr_prompt_disabled": False,
    "single_mode_target_training_levels": "5,3,3,0,1",
    "pause_if_race_order_gt": 5,
    "single_mode_race_data_path": "single_mode_races.jsonl",
    "single_mode_choice_path": "single_mode_choices.json"
}


def get_settings() -> Dict:
    return SETTINGS


def get_str_value_settings() -> Dict[Text, Text]:
    c = {
        k: str(v)
        for k, v in SETTINGS.items()
    }
    return c


def save_json_config() -> None:
    cache = SETTINGS
    if isinstance(SETTINGS["single_mode_target_training_levels"], dict):
        cache["single_mode_target_training_levels"] = _unparse_training_levels(
            SETTINGS["single_mode_target_training_levels"])
    # if isinstance(SETTINGS["PLUGINS"], tuple):
    #     cache["PLUGINS"] = _unparse_plugins(SETTINGS["PLUGINS"])
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(cache))


def set_config(cfg_name: str, cfg_content: str) -> Dict[Text, bool]:
    if cfg_name == "single_mode_target_training_levels":
        cfg_content = _parse_training_levels(cfg_content)
    # elif cfg_name == "PLUGINS":
    #     cfg_content = _parse_plugins(cfg_content)

    if SETTINGS[cfg_name] != cfg_content:
        SETTINGS[cfg_name] = cfg_content
        if getattr(AUTO_DERBY_CONFIG_CLASS, cfg_name) != cfg_content:
            logger.info(f"设置CONFIG: {cfg_name}: {getattr(AUTO_DERBY_CONFIG_CLASS, cfg_name)} -> {cfg_content}")
            setattr(AUTO_DERBY_CONFIG_CLASS, cfg_name, cfg_content)
            AUTO_DERBY_CONFIG_CLASS.apply()
            save_json_config()
        return {cfg_name: True}
    else:
        return {cfg_name: False}


def batch_set_config(cfgs: list) -> List[Dict[Text, bool]]:
    result = []
    for i in cfgs:
        result.append(set_config(i["name"], i["content"]))
    return result


def reset_config() -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(DEFAULT_SETTINGS))
    for k, v in DEFAULT_SETTINGS.items():
        set_config(k, v)


def init(cfg_class):
    global SETTINGS
    global AUTO_DERBY_CONFIG_CLASS
    AUTO_DERBY_CONFIG_CLASS = cfg_class
    if not os.path.exists(CONFIG_PATH):
        SETTINGS = DEFAULT_SETTINGS
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps(DEFAULT_SETTINGS))
    else:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            SETTINGS = json.loads(f.read())

    for k, v in SETTINGS.items():
        set_config(k, v)
