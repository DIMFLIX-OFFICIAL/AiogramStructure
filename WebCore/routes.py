from aiohttp import web


class WebRoutes:
    """
    Класс используется для размещения в нем функций, которые будут вызываться из веба.
    """

    def __init__(self, webapp: web.Application) -> None:
        """
        Здесь нужно добавлять роуты в webapp
        """
        ...
