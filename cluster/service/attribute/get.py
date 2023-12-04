from core.attribute.attribute_repository import AttributeRepository
from core.base.search_criteria import SearchCriteria


def execute(filters: list = None) -> dict:

    repository = AttributeRepository()
    result = {}
    if filters is None:
        search_criteria = SearchCriteria([])
    else:
        search_criteria = SearchCriteria(filters)
    attribute_collection = repository.get_list(
        search_criteria
    )
    for attribute in attribute_collection:
        attribute.attribute_id = int(attribute.attribute_id)
        result[attribute.name] = attribute.to_dict()
    return result
