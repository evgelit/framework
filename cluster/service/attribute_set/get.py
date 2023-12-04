from core.attribute.attribute_set_repository import AttributeSetRepository
from core.base.search_criteria import SearchCriteria


def execute(filters: list = None) -> dict:

    repository = AttributeSetRepository()
    result = {}
    if filters is None:
        search_criteria = SearchCriteria([])
    else:
        search_criteria = SearchCriteria(filters)
    attribute_set_collection = repository.get_list(
        search_criteria
    )
    for attribute_set in attribute_set_collection:
        attribute_set.attribute_id = int(attribute_set.attribute_id)
        result[attribute_set.name] = attribute_set.to_dict()
    return result
