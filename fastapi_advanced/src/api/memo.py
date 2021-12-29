from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path
from starlette import status
from typing import List

from common.modules.memo.application.usecase import MemoUseCase
from common.modules.memo.domain.dto import MemoRegister, MemoUpdate, MemoResponse, MemoSingleResponse

from fastapi_advanced.src.containers import Container

router = APIRouter(prefix='/memos')
metadata = {
    "name": "Memo API",
    "description": "Memo CRUD API"
}


@router.get(
    name="Get Memo List API",
    path='', tags=['Memo API'], response_model=List[MemoSingleResponse],
    description="Get Memo List"
)
@inject
async def get_memos(uc: MemoUseCase = Depends(Provide[Container.memo_use_case])):
    return await uc.fetch_all()


@router.get(
    name="Get Memo by ID",
    path='/{item_id}', tags=['Memo API'], response_model=MemoResponse,
    description="Get Memo by ID"
)
@inject
async def get_memo_by_id(item_id: int = Path(..., title="Memo ID"),
                         uc: MemoUseCase = Depends(Provide[Container.memo_use_case])):
    return await uc.fetch_by_id(item_id)


@router.post(
    name="Add Memo",
    path="", tags=['Memo API'], status_code=status.HTTP_201_CREATED,
    description="Add memo"
)
@inject
async def add_memo(req: MemoRegister,
                   uc: MemoUseCase = Depends(Provide[Container.memo_use_case])):
    await uc.create_memo(req)


@router.patch(
    name="Update Memo",
    path="/{item_id}", tags=['Memo API'],
    description="Update Memo"
)
@inject
async def update_memo(req: MemoUpdate, item_id: int = Path(..., title="Memo ID"),
                      uc: MemoUseCase = Depends(Provide[Container.memo_use_case])):
    await uc.update_memo(item_id, req)


@router.delete(
    name="Delete Memo",
    path="/{item_id}", tags=['Memo API'], status_code=status.HTTP_204_NO_CONTENT,
    description="Delete Memo"
)
@inject
async def delete_memo(item_id: int = Path(..., title="Memo ID"),
                      uc: MemoUseCase = Depends(Provide[Container.memo_use_case])):
    await uc.delete_memo(item_id)
