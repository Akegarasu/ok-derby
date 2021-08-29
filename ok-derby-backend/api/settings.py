import json
import logging
import api.base

from models.resp import response
from models.settings import get_settings
from models.settings import batch_set_config, reset_config

logger = logging.getLogger(__name__)


# noinspection PyAbstractClass
class SettingsHandler(api.base.ApiHandler):
    async def get(self):
        self.write(
            response.ok(
                json.dumps(get_settings())
            )
        )

    async def post(self):
        try:
            batch_set_config(self.json_args.get("cfgs"))
            self.write(
                response.ok(self.json_args.get("cfgs"))
            )
        except Exception as e:
            self.write(
                response.error(repr(e))
            )


# noinspection PyAbstractClass
class ResetSettingsHandler(api.base.ApiHandler):
    async def get(self):
        try:
            reset_config()
            self.write(
                response.ok("重置成功")
            )
        except Exception as e:
            self.write(
                response.error(repr(e))
            )
