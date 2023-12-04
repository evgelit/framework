from core.attribute.attribute_repository import AttributeRepository

attribute_repository = AttributeRepository()

attribute_data = {
    "name": "sample_attribute",
    "attribute_type": "varchar"
}

attribute = attribute_repository.create(attribute_data)
attribute_repository.save(attribute)

attribute = attribute_repository.get_by_name("sample_attribute")

print(attribute.to_dict())

attribute_repository.delete(attribute.attribute_id)
