from core.base.dto import DTO
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

    '''
    Creating DTO instance from loaded data
    '''
    def __next__(self):
        if len(self.data.index) == 0:
            raise StopIteration
        if self.iter < len(self.data.index):
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

    '''
    Set data to collection, updating iteration variables
    '''
    def set_data(self, data: DataFrame) -> None:
        self.data = data
        self.iter = 0
        self.iter_max = len(self.data.index) - 1

    '''
    Applying filters to data on collection load, 
    supported only when collection connected to database.
    
    Possible conditions:
        eq - equal
        neq - not equal
        gt - greater than
        lt - lower than
        gteq - greater than or equal
        lteq - lower than or equal
        in - in set
        not in - not in set
    '''
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

    '''
    Get first entity of collection   
    '''
    def get_first_item(self):
        return self.DTO(
            dict(
                zip(
                    self.data.columns,
                    self.data.iloc[0].tolist()
                )
            )
        )

    '''
    Changing set of values loaded to collection, 
    supported only when collection connected to database  
    '''
    def add_field_to_select(
        self,
        field: str or list
    ) -> None:
        if type(field) is list:
            self.fields = self.fields + field
        else:
            self.fields.append(field)

    '''
    Return number of collection's entities
    '''
    def count(self) -> int:
        return len(self.data.index)

    '''
    Reset current fields, filters and iterator
    '''
    def reset(self) -> None:
        self.iter = 0
        self.filters = []
        self.fields = []
