from fastapi import FastAPI
from pydantic import BaseModel, Field
from pymfdata.rdb.connection import AsyncSQLAlchemy
from starlette import status
from sqlalchemy import select
from typing import Optional

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.memo.infrastructure.entity import MemoEntity

app = FastAPI()
db = AsyncSQLAlchemy(db_uri='postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/pymfdata_sample_app')


class MemoRequest(BaseModel):
    title: str = Field(title="Memo Title")
    content: Optional[str] = Field(title="Memo content")


@app.on_event("startup")
async def on_startup():
    await db.connect()
    db.init_session_factory(autocommit=False, autoflush=False)


@app.on_event("shutdown")
async def on_shutdown():
    await db.disconnect()


@app.get("/memos")
async def get_memo():
    async with db.session() as session:
        stmt = select(MemoEntity)
        result = await session.execute(stmt)
        res = result.unique().scalars().fetchall()

    return res


@app.post("/memos", status_code=status.HTTP_201_CREATED)
async def add_memo(req: MemoRequest):
    entity = MemoEntity(**req.dict())
    async with db.session() as session:
        session.add(entity)
        await session.commit()
        await session.refresh(entity)

    return entity
