from helpers import get_column_num, get_index_label, get_row_column_from_label


class Index:
    def __init__(self, row, column):
        self.row = row
        self.col = column
        self.row_label = str(int(self.row)+1)
        self.row_label, self.column_label = get_index_label(int(self.row), self.col)
        self.index_label = "".join([self.column_label, self.row_label])

    def __str__(self) -> str:
        return self.index_label
    
    def __repr__(self) -> str:
         return f"Index(row={self.row}, col={self.col})"
    
    def __add__(self, other) -> 'Index':
        if isinstance(other, Index):
            return Index(self.row + other.row, self.col + other.col)
        elif isinstance(other, tuple):
            return Index(self.row + other[0], self.col + other[1])
        else:
            raise ValueError
        
    def max(self, other) -> 'Index':
        if isinstance(other, Index):
            return Index(self.row if self.row > other.row else other.row, self.col if self.col > other.col else other.col)
        elif isinstance(other, tuple):
            return Index(self.row if self.row > other[0] else other[0], self.col if self.col > other[1] else other[1])
        else:
            raise ValueError


    def min(self, other) -> 'Index':
        if isinstance(other, Index):
            return Index(self.row if self.row < other.row else other.row, self.col if self.col < other.col else other.col)
        elif isinstance(other, tuple):
            return Index(self.row if self.row < other[0] else other[0], self.col if self.col < other[1] else other[1])
        else:
            raise ValueError
        

    @classmethod
    def parse(cls, label) -> 'Index':
        row, column_ = get_row_column_from_label(label)
        row = int(row)
        col = get_column_num(column_, 0)
        # return f"Index(row={int(row_)-1}, col={column})"
        return Index(row-1, col)