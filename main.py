from attribute.attribute_repository import AttributeRepository

repo = AttributeRepository()
attr = repo.get_by_name("first_name")
print(attr.to_dict())