import datetime
from loguru import logger

from sqlalchemy import select, insert, func, update, CursorResult
from General.database.models.user import User


class DB:
    """"Database requests"""

    def __init__(self, session):
        self.session = session

    async def get_user(self, user_id: int):
        sql = select(User).where(User.user_id == user_id)
        request = await self.session.execute(sql)
        return request.scalar()

    async def add_user(self, user_id: int, username: str) -> CursorResult:
        sql = insert(User).values(
            user_id=user_id,
            username=username
        ).returning('*')

        request = await self.session.execute(sql)
        await self.session.commit()
        logger.info(f"User {user_id} | {username} added")
        return request.first()

    async def count_users(self) -> int:
        sql = select(func.count("*")).select_from(User)
        request = await self.session.execute(sql)
        await self.session.commit()
        return request.scalar()

    async def update_user(self,
                          user_id: int,
                          balance: int = None,
                          latest_online: datetime.datetime = None,
                          username: str = None
                          ) -> CursorResult:
        values = {}
        if balance is not None:
            values.update(dict(balance=balance))
        if latest_online is not None:
            values.update(dict(latest_online=latest_online))
        if username is not None:
            values.update(dict(username=username))

        sql = update(User).where(User.user_id == user_id).values(**values).returning("*")
        request = await self.session.execute(sql)
        await self.session.commit()

        logger.info(f"User {user_id} updated. Values: {values}")
        return request

    async def count_id_users(self) -> int:
        sql = select(User.user_id).select_from(User)
        request = await self.session.execute(sql)
        return request.scalars().all()

