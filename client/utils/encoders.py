import json


class ObjectJsonSerializable(object):
    def toJSON(self):
        # TODO: remove null field
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
