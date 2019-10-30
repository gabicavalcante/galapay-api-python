import json
from datetime import datetime, date


class ObjectJsonSerializable(object):
    def toJSON(self):
        remove_null(self.__dict__)

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4,)


def remove_null(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d
