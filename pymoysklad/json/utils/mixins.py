import dataclasses
from operator import attrgetter


# Нагло позаимствовано из vcs
# (https://github.com/vcs-python/libvcs/blob/v0.13.0a3/libvcs/utils/dataclasses.py#L5)
class SkipDefaultFieldsReprMixin:
    def __repr__(self):
        nodef_f_vals = (
            (f.name, attrgetter(f.name)(self))
            for f in dataclasses.fields(self)
            if attrgetter(f.name)(self) != f.default
        )

        nodef_f_repr = ", ".join(f"{name}={value}" for name, value in nodef_f_vals)
        return f"{self.__class__.__name__}({nodef_f_repr})"
