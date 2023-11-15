import string
from dateutil.parser import parse

alphabet: list[str] = [a for a in string.ascii_uppercase]
concept_dict: dict[str, int]  = {}

for i, j in enumerate(alphabet):
    concept_dict[j] = int(i)


def get_column_num(column:str, n:int) -> int:
    column_ = column.upper()
    if len(column_) == 1:
        n += (concept_dict[column_])
        return n
    else:
        n += (len(concept_dict)) * (concept_dict[column_[0]]+1)
    return get_column_num(column_[1:], n)


def get_index_label(row: int, column:int)->tuple:
    row_ = row+1
    id_ = divmod(column, 26)
    if id_[0] >= 1:
        col_ = alphabet[(id_[0]-1)] + alphabet[(id_[1])]
    else:
        col_ = alphabet[id_[1]]
    return (str(row_), str(col_))


#Returns labels separated into literal row and column as passed
def get_row_column_from_label(label:str) -> tuple:
    row: list[str]=[]
    col: list[str]=[]
    for i in range(len(label)):
        if label[i].isnumeric():
            row.append(label[i])
        elif label[i].isalpha():
            col.append(label[i])
        else:
            raise ValueError()
    return "".join(row), "".join(col)


def check_spec(type_:str, spec:str) -> bool:
    if type_ == "number":
        if spec.startswith("%") and spec.endswith("f"):
            return True
        else:
            raise ValueError
        
    if type_ == "date":
            if spec.startswith("%"):
                return True
            else:
                raise ValueError
    return False

def formatted_value(type_, value, spec):
    if type_ == "date":
        try:
            date_ = parse(value)
            value_ = date_.strftime(spec)
        except ValueError as e:
            raise e
    elif type_ == "number":
        try:
            value_ = spec%value
        except ValueError as e:
            raise e
    else:
        raise ValueError
    return value_
