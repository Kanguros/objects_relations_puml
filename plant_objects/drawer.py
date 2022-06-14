from typing import Type, Any
from models import PAttr, PObject

def define_object(cls: Type):
    pass


def define_attr(data: Any):
    pass


def create_diagram(classes: list):
    objects = []
    for cls in classes:
        objects.append(define_object(cls))

