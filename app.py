from aiogram.webhook.aiohttp_server import TokenBasedRequestHandler
from aiohttp import web
from loguru import logger

from BotCore import handlers
from BotCore.middlewares.add_users import AddUserMiddleware
from General import config as cfg
from General.loader import bot, dp
from WebCore.routes import WebRoutes


async def on_startup(app):
    dp.update.middleware(AddUserMiddleware())
    TokenBasedRequestHandler(dp).register(webapp, cfg.WEBHOOK_PATH)
    await bot.set_webhook(url=cfg.WEB_URL + cfg.WEBHOOK_PATH.format(bot_token=cfg.BOT_TOKEN))
    logger.success("Bot started succesfully")


async def on_shutdown(_):
    await bot.delete_webhook()
    await dp.storage.close()
    logger.warning("Bot turned off")


if __name__ == '__main__':
    webapp = web.Application()
    webapp.on_startup.append(on_startup)
    webapp.on_shutdown.append(on_shutdown)
    WebRoutes(webapp)
    web.run_app(webapp, host=cfg.WEBHOOK_HOST, port=cfg.WEBHOOK_PORT, print=logger.success("Server started"))
