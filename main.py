from attribute.attribute_repository import AttributeRepository

repo = AttributeRepository()
attr = repo.create(
    {
        "name": "first_name",
        "attribute_type": "varchar"
    }
)

print(type(attr), attr.name)
