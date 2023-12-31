from core.attribute.attribute_repository import AttributeRepository
from core.attribute.attribute_collection import AttributeCollection
from core.base.search_criteria import SearchCriteria

'''
 Example 1
 Get collection by repository
'''
search_criteria = SearchCriteria([])
attribute_repository = AttributeRepository()
attribute_collection = attribute_repository.get_list(search_criteria)

for attribute in attribute_collection:
    print(attribute.to_dict())

print("#######")

'''
 Example 2
 Get collection directly
'''
attribute_collection = AttributeCollection()
attribute_collection.load_collection()

for attribute in attribute_collection:
    print(attribute.to_dict())

print("#######")

'''
 Example 3
 Get only attributes with type varchar by collection
'''
attribute_collection = AttributeCollection()
attribute_collection.add_field_to_filter('attribute_type', 'varchar')
attribute_collection.load_collection()

for attribute in attribute_collection:
    print(attribute.to_dict())

print("#######")

'''
 Example 3
 Get only attributes with type numerical and ID greater than 20 by repository
'''
search_criteria = SearchCriteria(
    [
        {
            'field': 'attribute_type',
            'value': 'numerical',
            'condition': 'eq'
        },
        {
            'field': 'attribute_id',
            'value': '20',
            'condition': 'gt'
        }
    ]
)
attribute_repository = AttributeRepository()
attribute_collection = attribute_repository.get_list(search_criteria)

for attribute in attribute_collection:
    print(attribute.to_dict())
