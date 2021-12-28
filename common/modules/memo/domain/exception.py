from common.errors import NotFoundException


class MemoNotFoundException(NotFoundException):
    def __init__(self, item_id: int):
        self._message = "ID: {} Memo Not Found".format(item_id)

        super().__init__(self._message)

    def __str__(self) -> str:
        return self._message
