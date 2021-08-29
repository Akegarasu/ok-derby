import logging
import api.base

from utils.util import is_game_running

from models.resp import response
from models.controller import missionController

logger = logging.getLogger(__name__)


# noinspection PyAbstractClass
class StartHandler(api.base.ApiHandler):
    async def post(self):
        if missionController.get_mission_status() == "running":
            self.write(response.error("已经有任务正在进行了"))
            logger.info("Start Failed, There's already a job in progress")
            return
        job_name = self.json_args.get("job_name")
        plugins = self.json_args.get("plugins")
        adb_address = self.json_args.get("adb_address", None)
        if not is_game_running() and not adb_address:
            self.write(
                response.error('游戏未运行，请启动游戏再运行')
            )
            return
        logger.debug(f"job_name: {job_name}, plugins: {plugins}, adb_address: {adb_address}")
        missionController.start_mission(job_name, plugins, adb_address)
        self.write(
            response.ok('启动成功')
        )
        logger.info("Start Success")


# noinspection PyAbstractClass
class StopHandler(api.base.ApiHandler):
    async def post(self):
        if missionController.get_mission_status() == 'running':
            missionController.stop_mission()
            self.write({
                'code': 0,
            })
        else:
            self.write(
                response.error('没有任务正在进行')
            )


# noinspection PyAbstractClass
class StatusHandler(api.base.ApiHandler):
    async def get(self):
        self.write(response.ok(
            {
                "status": missionController.get_mission_status(),
                "job_name": missionController.job_name,
            }
        ))
