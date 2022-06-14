from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class PAttr:
    name: str
    type_: Any
    doc: str = field(default="", repr=False)
    link: bool = field(default=False, repr=False)
    many: bool = field(default=False, repr=False)

    def __repr__(self):
        return f"PAttr({self.name}:{self.type_})"
x

@dataclass
class PObject:
    """
    Represent Model object.

    Attrs:
        name: Formal name of the object.
        doc: Detailed description, if any.
        attrs: List (even empty) of attribiuts of itself.
    """
    name: str
    doc: str = field(default="", repr=False)
    attrs: List[PAttr] = field(default_factory=list, repr=False)

    def __post_init__(self):
        if not isinstance(self.attrs, list) and not self.attrs:
            self.attrs = []
