# -*- coding: utf-8 -*-

import argparse
import logging
import logging.handlers
import os
import webbrowser
import tornado.ioloop
import tornado.web

import api.settings
import api.main
import api.mission
import api.plugins

import models.settings

from auto_derby import okderby
from auto_derby import config as auto_derby_config
from models.controller import missionController

logger = logging.getLogger(__name__)

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
WEB_ROOT = os.path.join(BASE_PATH, "frontend", "dist")
LOG_FILE_NAME = os.path.join(BASE_PATH, "log", "ok-derby.log")


def main():
    args = parse_args()
    init_logging(args.debug)
    missionController.init(okderby.start)
    models.settings.init(auto_derby_config)
    run_server(args.host, args.port, args.debug)


def parse_args():
    parser = argparse.ArgumentParser(description="全自动养马")
    parser.add_argument("--host", help="服务器host，默认为127.0.0.1", default="127.0.0.1")
    parser.add_argument("--port", help="服务器端口，默认为12780", type=int, default=12780)
    parser.add_argument("--debug", help="调试模式", action="store_true")
    return parser.parse_args()


def init_logging(debug):
    stream_handler = logging.StreamHandler()
    file_handler = logging.handlers.TimedRotatingFileHandler(
        LOG_FILE_NAME, encoding="utf-8", when="midnight", backupCount=7, delay=True
    )
    logging.basicConfig(
        format="{asctime} {levelname} [{name}]: {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{",
        level=logging.INFO if not debug else logging.DEBUG,
        handlers=[stream_handler, file_handler],
    )

    # 屏蔽访问日志
    logging.getLogger("tornado.access").setLevel(logging.WARNING)


def run_server(host, port, debug):
    routes = [
        # (r'/api/server_info', api.main.ServerInfoHandler),
        (r"/api/settings", api.settings.SettingsHandler),
        (r"/api/settings/reset", api.settings.ResetSettingsHandler),
        (r"/api/plugins", api.plugins.PluginHandler),
        (r"/api/start", api.mission.StartHandler),
        (r"/api/stop", api.mission.StopHandler),
        (r"/api/status", api.mission.StatusHandler),
        (
            r"/(.*)",
            api.main.MainHandler,
            {"path": WEB_ROOT, "default_filename": "index.html"},
        ),
    ]
    app = tornado.web.Application(
        routes, websocket_ping_interval=10, debug=debug, autoreload=False
    )

    try:
        app.listen(port, host, xheaders=False)
    except OSError:
        logger.warning("Address is used %s:%d", host, port)
        return
    finally:
        url = "http://localhost/" if port == 80 else f"http://localhost:{port}/"
        # 防止更新版本后浏览器加载缓存
        url += "?_v=" + '0.5'
        webbrowser.open(url)
    logger.info("Server started: %s:%d", host, port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
