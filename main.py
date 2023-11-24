from attribute.attribute_repository import AttributeRepository
from base.collection import Collection

repo = AttributeRepository()
attr1 = repo.create(
    {
        "name": "first_name",
        "attribute_type": "varchar"
    }
)
attr2 = repo.create(
    {
        "name": "last_name",
        "attribute_type": "varchar"
    }
)

collection = Collection(
    [attr1, attr2]
)

