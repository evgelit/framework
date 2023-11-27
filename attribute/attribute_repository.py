from base.search_criteria import SearchCriteria
from attribute.attribute import Attribute
from attribute.attribute_collection import AttributeCollection


class AttributeRepository:

    __collection = AttributeCollection()

    '''
    Create attribute entity
    '''
    def create(self, data: dict) -> Attribute:
        return Attribute(data)

    '''
    Load attribute entity from database by ID, 
    Raise error if ID not exists
    '''
    def get(self, attribute_id: str) -> Attribute:
        self.__collection.reset()
        self.__collection.add_field_to_filter(
            field='attribute_id',
            value=attribute_id,
            condition="eq"
        )
        self.__collection.load_collection()
        if self.__collection.count() < 1:
            raise ValueError(f"Attribute with ID {attribute_id} not found.")
        return self.__collection.get_first_item()

    '''
    Load attribute entity from database by name, 
    Raise error if name not exists
    '''
    def get_by_name(self, name: str) -> Attribute:
        self.__collection.reset()
        self.__collection.add_field_to_filter(
            field='name',
            value=name,
            condition="eq"
        )
        self.__collection.load_collection()
        if self.__collection.count() < 1:
            raise ValueError(f"Attribute with name {name} not found.")
        return self.__collection.get_first_item()

    '''
    Load attribute collection from database by SearchCriteria
    '''
    def get_list(self, search_criteria: SearchCriteria) -> AttributeCollection:
        self.__collection.reset()
        for filter_ in search_criteria.filters:
            self.__collection.add_field_to_filter(
                field=filter_['field'],
                value=filter_['value'],
                condition=filter_['condition'],
            )
        self.__collection.load_collection()
        return self.__collection

    '''
    Save attribute entity
    '''
    def save(self, attribute: Attribute, commit: bool = True) -> None:
        self.__collection.get_resource().save(attribute)
        if commit is True:
            self.__collection.get_resource().commit_transaction()

    '''
    Delete attribute entity
    '''
    def delete(self, attribute_id: int or str, commit: bool = True) -> None:
        self.__collection.get_resource().delete(attribute_id)
        if commit is True:
            self.__collection.get_resource().commit_transaction()
