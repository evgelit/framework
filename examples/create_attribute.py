from attribute.attribute_repository import AttributeRepository
from attribute.attribute_collection import AttributeCollection
from base.search_criteria import SearchCriteria

# Get collection by repository
search_criteria = SearchCriteria([])
attribute_repository = AttributeRepository()
attribute_collection = attribute_repository.get_list(search_criteria)

for attribute in attribute_collection:
    print(attribute.to_dict())

print("#######")

# Get collection directly
attribute_collection = AttributeCollection()
attribute_collection.load_collection()

for attribute in attribute_collection:
    print(attribute.to_dict())

print("#######")

# Get only attributes with type varchar
attribute_collection = AttributeCollection()
attribute_collection.add_field_to_filter('attribute_type', 'varchar')
attribute_collection.load_collection()

for attribute in attribute_collection:
    print(attribute.to_dict())
