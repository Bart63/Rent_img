from JSONObj import JSONObj
from DictObj import DictObj
from json import dumps, load
from io import StringIO

class DictJSONAdapt(JSONObj, DictObj):
    def __init__(self, dict) -> None:
        self.dict = dict
        self.dictToJSON()

    def dictToJSON(self):
        self.json = load(StringIO(dumps(self.dict)))