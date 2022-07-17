import inspect

from typing import Any, Dict, Any, Callable, Optional


class BaseEffective:
    fields: Dict[Any, Callable]

    def __getitem__(self, key):
        return self.fields[key]

    def __contains__(self, item):
        return item in self.fields


class Effective(BaseEffective):
    def __init__(self, fields: Optional[dict] = None, **kwagrs) -> None:
        self.fields: Dict[Any, Callable] = {**fields, **kwagrs} if fields else kwagrs

    @classmethod
    def perform(cls, effect, *args, **kwargs):
        frame = inspect.currentframe()
        for local in cls.frame_locals(frame):
            for v in reversed(local.values()):
                if isinstance(v, BaseEffective):
                    if effect in v:
                        return v[effect](*args, **kwargs)

    @classmethod
    async def async_perform(cls, effect, *args, **kwargs):
        frame = inspect.currentframe()
        for local in cls.frame_locals(frame):
            for v in reversed(local.values()):
                if isinstance(v, BaseEffective):
                    if effect in v:
                        return await v[effect](*args, **kwargs)

    @staticmethod
    def frame_locals(frame):
        frame = frame.f_back  # type: ignore
        while frame:
            yield frame.f_locals
            frame = frame.f_back
