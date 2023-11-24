from base.collection import Collection
from attribute.attribute import Attribute
from attribute.attribute_resource import AttributeResource


class AttributeCollection(Collection):

    DTO: Attribute = Attribute
    resource: AttributeResource = AttributeResource()

    def __next__(self) -> Attribute:
        return super().__next__()

    def load_collection(self) -> None:
        data = self.resource.load(
            self.fields,
            self.filters,
        )
        self.set_data(data)
