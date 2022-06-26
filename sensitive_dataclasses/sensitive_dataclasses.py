from typing import Any, Callable, NewType, Optional

import dataclasses

SensitiveData = NewType('SensitiveData', Any)  # type: ignore[valid-newtype]


def sensitive_dataclass(
    class_: Optional[type] = None,
    /,
    *,
    init: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = False,
    unsafe_hash: bool = False,
    frozen: bool = False,
) -> Callable:
    def _process_sensitive_fields(class_: type) -> type:
        for field, annotation in class_.__annotations__.items():
            if annotation is not SensitiveData:
                continue

            explicit_defined_field = getattr(class_, field, None)

            if explicit_defined_field:
                explicit_defined_field.repr = False
            else:
                setattr(class_, field, dataclasses.field(repr=False))

        return class_

    def decorator(class_: type) -> Callable:
        dataclass_ = dataclasses.dataclass(  # type: ignore[call-overload]
            _process_sensitive_fields(class_),
            init=init,
            repr=repr,
            eq=eq,
            order=order,
            unsafe_hash=unsafe_hash,
            frozen=frozen,
        )

        return dataclass_

    if class_ is None:
        return decorator

    return decorator(class_)
