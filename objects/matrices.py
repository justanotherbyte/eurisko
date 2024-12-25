from typing import Callable, Union
from operator import add, sub, mul

Number = int | float


def dot_product(arr1: list[Number], arr2: list[Number]) -> Number:
    assert len(arr1) == len(
        arr2
    ), "Two arrays must be the same size to compute dot product"
    return sum(arr1[idx] * arr2[idx] for idx in range(len(arr1)))


class Matrix:
    def __init__(self, values: list[list[Number]]):
        self.values = values
        self.dim = (len(values), len(values[0]))

    @property
    def rows(self) -> list[list[Number]]:
        return self.values

    @property
    def columns(self) -> list[list[Number]]:
        rows, cols = self.dim
        col_mat = []
        for colidx in range(cols):
            col = []
            for rowidx in range(rows):
                col.append(self.values[rowidx][colidx])

            col_mat.append(col)

        return col_mat

    @property
    def transpose(self) -> "Matrix":
        return Matrix(self.columns)

    def __repr__(self) -> str:
        return "\n".join("  ".join(map(str, x)) for x in self.values)

    def _callable_operation(
        self, operation: Callable[[Number, Number], Number], other: "Matrix"
    ):
        assert self.dim == other.dim, "Dimensions must match"

        rows, cols = self.dim
        new_matrix = []
        for ridx in range(rows):
            row = []
            for cidx in range(cols):
                row.append(operation(self.values[ridx][cidx], other.values[ridx][cidx]))

            new_matrix.append(row)

        return Matrix(new_matrix)

    def __add__(self, other: "Matrix") -> "Matrix":
        return self._callable_operation(add, other)

    def __sub__(self, other: "Matrix") -> "Matrix":
        return self._callable_operation(sub, other)

    def __mul__(self, other: Union["Matrix", Number]) -> "Matrix":
        rows, cols = self.dim
        if isinstance(other, Number):
            multiplier = Matrix([[other] * cols] * rows)
            return self._callable_operation(mul, multiplier)

        orows, _ = other.dim

        assert cols == orows, "Columns of A must much rows of B"

        new_matrix = []

        for row in self.values:
            new_row = []
            for col in other.columns:
                new_row.append(dot_product(row, col))

            new_matrix.append(new_row)

        return Matrix(new_matrix)


A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix([[7, 8], [9, 10], [11, 12]])
