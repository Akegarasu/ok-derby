import time
import logging
import win32con
import win32gui
import webbrowser
from typing import Optional
from auto_derby import plugin

from . import clients, config, jobs, templates

LOGGER = logging.getLogger(__name__)


def start(job_name: str,
          plugins: str,
          adb_address: Optional[str] = None) -> None:
    if adb_address == None:
        adb_address = config.ADB_ADDRESS

    avaliable_jobs = {
        "team_race": jobs.team_race,
        "champions_meeting": jobs.champions_meeting,
        "legend_race": jobs.legend_race,
        "nurturing": jobs.nurturing,
        "daily_race_money": lambda: jobs.daily_race(templates.MOONLIGHT_PRIZE),
        "daily_race_sp": lambda: jobs.daily_race(templates.JUPITER_CUP),
        "roulette_derby": jobs.roulette_derby,
    }

    job = avaliable_jobs.get(job_name)

    plugin.reload()
    if plugins != "":
        for i in plugins.split(","):
            plugin.install(i)
    config.apply()

    if adb_address:
        c = clients.ADBClient(adb_address)
    else:
        c = clients.DMMClient.find()
        if not c:
            if (
                    win32gui.MessageBox(
                        0,
                        "是否启动DMM版游戏?",
                        "没有找到游戏窗口",
                        win32con.MB_YESNO,
                    )
                    == 6
            ):
                webbrowser.open("dmmgameplayer://umamusume/cl/general/umamusume")
                while not c:
                    time.sleep(1)
                    LOGGER.info("waiting game launch")
                    c = clients.DMMClient.find()
                LOGGER.info("game window: %s", c.h_wnd)
            else:
                exit(1)
    c.setup()
    clients.set_current(c)
    job()
