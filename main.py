from attribute.attribute_repository import AttributeRepository
from attribute.attribute_set_repository import AttributeSetRepository

attr_repo = AttributeRepository()
attr = attr_repo.get("24")

attr_set_repo = AttributeSetRepository()
attr_set = attr_set_repo.get("2")

attr_set_repo.remove_from_set(attr_set,attr)