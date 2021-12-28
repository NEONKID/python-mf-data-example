from dependency_injector.containers import copy
from dependency_injector.providers import Factory, Singleton

from common.containers import BaseContainer
from common.modules.label.application.usecase import LabelUseCaseUnitOfWork, LabelUseCase
from common.modules.memo.application.usecase import MemoUseCaseUnitOfWork, MemoUseCase


@copy(BaseContainer)
class Container(BaseContainer):
    # Unit Of Work
    label_unit_of_work = Factory(LabelUseCaseUnitOfWork, engine=BaseContainer.db.provided.engine)
    memo_unit_of_work = Factory(MemoUseCaseUnitOfWork, engine=BaseContainer.db.provided.engine)

    # Use Case
    label_use_case = Factory(LabelUseCase, uow=label_unit_of_work)
    memo_use_case = Factory(MemoUseCase, uow=memo_unit_of_work)
