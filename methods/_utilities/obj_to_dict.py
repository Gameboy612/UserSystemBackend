# I have no clue wtf is this btw, ty ChatGPT

from sqlalchemy.orm import class_mapper

def obj_to_dict(obj):
    """Converts a SQLAlchemy object to a dictionary."""
    mapper = class_mapper(obj.__class__)
    attributes = [attr.key for attr in mapper.iterate_properties if hasattr(obj, attr.key)]
    return {a: getattr(obj, a) for a in attributes}
    