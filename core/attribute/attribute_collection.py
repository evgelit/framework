from core.base.collection import Collection
from core.attribute.attribute import Attribute
from core.attribute.attribute_resource import AttributeResource


class AttributeCollection(Collection):

    DTO: Attribute = Attribute
    __resource: AttributeResource = AttributeResource()

    '''
    Create single attribute entity
    '''
    def __next__(self) -> Attribute:
        return super().__next__()

    '''
    Get first item from collection
    '''
    def get_first_item(self) -> Attribute:
        return super().get_first_item()

    '''
    Load collection data from database 
    '''
    def load_collection(self) -> None:
        data = self.__resource.load(
            self.fields,
            self.filters,
        )
        self.set_data(data)

    '''
    Get current collection resource
    '''
    def get_resource(self) -> AttributeResource:
        return self.__resource

