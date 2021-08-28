from typing import Optional, Union, Any


class response:
    def __init__(self,
                 rep_type: int,
                 message: dict):
        pass

    @classmethod
    def ok(cls, data: Optional[Union[dict, str, Any]]) -> dict:
        return {
            "code": 0,
            "data": data
        }

    @classmethod
    def error(cls, data: Optional[Union[dict, str]]) -> dict:
        return {
            "code": -1,
            "data": data
        }
