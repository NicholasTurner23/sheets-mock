from index import Index
from helpers import check_spec, formatted_value
from typing import Any


class Spreadsheet():
    def __init__(self):
        self.sheet:dict = {}

    def set(self, index:Index, raw:str) -> None:
        row = index.row_label
        col = index.column_label
        if self.sheet.get(int(row), -1) == -1:
            self.sheet[int(row)] = {col:{"types":[type(raw)], "spec":"None", "original_value":raw, "formatted_value":None}}
        else:
            self.sheet.get(int(row), "Nan").update({col:{"types":[type(raw)], "spec":"None", "original_value":raw, "formatted_value":None}})
        return

    def set_format(self, index:Index, type_:str, spec:str) -> None:
        row = index.row_label
        col = index.column_label
        if self.sheet.get(int(row), -1) == -1:
            raise KeyError 
        else:
            entry:dict[str, dict] = self.sheet.get(int(row), {})
            value:str = entry[col]["original_value"]
            types:list = entry[col]["types"]
            if len(types) < 2:
                types.append(type_)
            if check_spec(type_, spec):
                formatted = formatted_value(type_, value, spec)
            self.sheet.get(int(row), "None").update({col:{"types":types, "spec":spec, "original_value":value, "formatted_value":formatted}})
        return
    

    def get_formatted(self, index:Index) -> str:
        row = index.row_label
        col = index.column_label

        if self.sheet.get(int(row), -1) == -1:
            raise KeyError
        else:
            entry:dict[str, dict] = self.sheet.get(int(row), {})
            original_value:str = entry[col]["original_value"]
            formatted_value:str = entry[col]["formatted_value"]
            if original_value.startswith("="):
                try:
                    index = Index.parse(original_value[1:])
                except ValueError as e:
                    raise e
                else:
                    row = index.row_label
                    col = index.column_label
                    entry = self.sheet.get(int(row), {})
                    formatted_value = entry[col]["formatted_value"]

            if formatted_value is None:
                return "Not formatted"
        return formatted_value


    def get_raw(self, index:Index) -> str:
        row = index.row_label
        col = index.column_label

        if self.sheet.get(int(row), -1) == -1:
            raise KeyError
        else:
            entry:dict[str, dict] = self.sheet.get(int(row), {})
            value:str = entry[col]["original_value"]
        return value