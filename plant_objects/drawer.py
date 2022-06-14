from typing import Type, Any
from models import PAttr, PObject


def define_object(cls: Type) -> PObject:
    name = cls.__getattribute__('name') or \
           cls.__getattribute__('__name__') or \
           cls.__class__.__name__
    logger.debug(f"[{cls}] Name defined as {name}")
    doc = cls.__doc__ or \
          ""
    logger.debug(f"[{cls}] Name defined as {doc}")
    attrs = find_attrs(cls)

    return PObject(name, doc, attrs)


def define_attr():
    pass


def find_attrs(cls: Any):
    pass



def create_diagram(classes: list):
    objects = []
    for cls in classes:
        objects.append(define_object(cls))

    links = []
    for obj in objects:
        for attr in obj.attrs:
            if attr.link:
                links.append((obj, attr), (attr.type_))
