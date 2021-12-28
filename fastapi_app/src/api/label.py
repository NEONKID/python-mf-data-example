from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path
from typing import List

from common.modules.label.application.usecase import LabelUseCase
from common.modules.label.domain.dto import LabelResponse, LabelSingleResponse

from fastapi_app.src.containers import Container

router = APIRouter(prefix='/labels')
metadata = {
    "name": "Label API",
    "description": "Label GET API"
}


@router.get(
    name="Get Label List API",
    path='', tags=['Label API'], response_model=List[LabelSingleResponse],
    description="Get Label List API"
)
@inject
async def get_labels(uc: LabelUseCase = Depends(Provide[Container.label_use_case])):
    return await uc.fetch_all()


@router.get(
    name="Get Label by name",
    path='/{item_name}', tags=['Label API'], response_model=LabelResponse,
    description="Get Label by name"
)
@inject
async def get_label_by_name(item_name: str = Path(..., title="Label name"),
                            uc: LabelUseCase = Depends(Provide[Container.label_use_case])):
    return await uc.fetch_by_name(item_name)
