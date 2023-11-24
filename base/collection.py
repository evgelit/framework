from base.dto import DTO
from typing import Any
from pandas import DataFrame


class Collection:

    DTO: DTO = DTO

    data: DataFrame = DataFrame()
    iter: int = 0
    iter_max: int = 0
    filters: list = []
    fields: list = []

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter <= self.iter_max:
            result = self.DTO(
                dict(
                    zip(
                        self.data.columns,
                        self.data.iloc[self.iter].tolist()
                    )
                )
            )
            self.iter += 1
            return result
        else:
            raise StopIteration

    def set_data(self, data: DataFrame) -> None:
        self.data = data
        self.iter_max = len(self.data.index) - 1

    # conditions:
    #    eq - equal
    #    neq - not equal
    #    gt - greater than
    #    lt - lower than
    #    gteq - greater than or equal
    #    lteq - lower than or equal
    #    in - in set
    #    not in - not in set
    def add_field_to_filter(
        self,
        field: str,
        value: Any,
        condition: str = "eq",
    ):
        self.filters.append(
            {
                "field": field,
                "value": value,
                "condition": condition,
            }
        )

    def add_field_to_select(
        self,
        field: str or list
    ):
        if type(field) is list:
            self.fields = self.fields + field
        else:
            self.fields.append(field)

    def reset(self) -> None:
        self.filters = []
