import logging
import os

import api.base
from models.resp import response

logger = logging.getLogger(__name__)
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
PLUGINS_PATH = os.path.join(BASE_PATH, "..", "plugins")

PLUGIN_DESCRIPTION = {
    "avoid_high_failure_rate_trains": "训练中失败率高于30%则不选",
    "example_custom_context": "自定义单人模式上下文示例，通过覆盖 next_turn 每回合执行自定义逻辑。",
    "example_custom_race_score": "自定义单人模式比赛示例，通过覆盖 score 更改比赛评分。",
    "example_custom_training_score": "自定义单人模式训练示例，通过覆盖 score 更改训练评分。",
    "example_smart_falcon": "完成醒目飞鹰育成目标的插件示例。使用插件生成器生成",
    "hello_world": "最简单的打印 Hello world 插件实现。",
    "limited_sale_buy_everything": "限时商店购买所有可购买物品",
    "limited_sale_buy_first_3": "限时商店购买前三个可购买物品",
    "limited_sale_ignore": "遇到限时商店直接关闭",
    "more_g1": "更倾向于 G1 比赛，重复多次会增强效果。",
    "umapyoi": "URA 决胜结束后播放 live",
    "auto_crane": "自动抓娃娃，实战曾经 3 次均命中",
    "no_event_prompt": "未见过的事件不请求人工处理自动选择第一项",
    "no_ocr_prompt": "文本识别匹配度较低时不请求人工处理而是自动使用匹配度最高的字",
    "afk": "无人值守模式 比赛前不暂停 + auto_crane + no_event_prompt + no_ocr_prompt",
    "use_legacy_screenshot": "使用旧版截图，性能较低。截屏出错时可尝试使用。",
    "less_op": "更少参加 OP/Pre-OP 的比赛，重复多次会增强效果。",
    "pause_before_command": "在执行每个命令之前暂停，可用于调试评分。",
    "pause_before_race_continue": "在比赛失败消耗闹钟继续比赛前暂停",
    "SSR樫本理子": "将友人卡假设为 樫本理子 进行更精准的评分",
    "SSR駿川たづな": "将友人卡假设为 駿川たづな 进行更精准的评分"
}


# noinspection PyAbstractClass
class PluginHandler(api.base.ApiHandler):
    async def get(self):
        plugins = [
            {
                "name": i.strip(".py"),
                "checked": False,
                "description": PLUGIN_DESCRIPTION.get(i.strip(".py"), "这个插件还没有描述哟")
            }
            for i in os.listdir(PLUGINS_PATH)
            if i != "__pycache__"
        ]
        self.write(response.ok(plugins))
