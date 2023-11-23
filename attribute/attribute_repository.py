from base.search_criteria import SearchCriteria
from attribute.attribute import Attribute
from attribute.attribute_collection import AttributeCollection


class AttributeRepository:

    def create(self, data: dict) -> Attribute:
        return Attribute(data)

    def get(self, attribute_id: int) -> Attribute:
        pass

    def get_by_name(self, name: str) -> Attribute:
        pass

    def get_list(self, search_criteria: SearchCriteria) -> AttributeCollection:
        pass

    def save(self, attribute: Attribute) -> None:
        pass

    def delete(self, attribute_id: int) -> None:
        pass
