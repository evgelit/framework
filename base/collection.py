from base.dto import DTO
from typing import Any


class Collection:

    data: [DTO] = []
    filtered: [DTO]
    filters: list = []

    def __init__(self, data: [DTO]):
        self.data = data

    def add_field_to_filter(
            self,
            field: str,
            condition: str,
            value: Any
    ) -> None:
        self.filters.append(
            {
                'field': field,
                'condition': condition,
                'value': value
            }
        )

    def apply_filters(self) -> None:
        pass
