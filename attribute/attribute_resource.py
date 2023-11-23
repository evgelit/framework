from base.search_criteria import SearchCriteria
from attribute.attribute import Attribute


class AttributeResource:

    def load(self, search_criteria: SearchCriteria):
        pass

    def save(self, attribute: Attribute) -> None:
        pass
