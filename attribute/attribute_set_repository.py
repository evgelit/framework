from base.search_criteria import SearchCriteria
from attribute.attribute_set import AttributeSet
from attribute.attribute import Attribute
from attribute.attribute_set_collection import AttributeSetCollection


class AttributeSetRepository:

    __collection = AttributeSetCollection()

    '''
    Create attribute set entity
    '''
    def create(self, data: dict) -> AttributeSet:
        return AttributeSet(data)

    '''
    Load attribute set entity from database by ID, 
    Raise error if ID not exists
    '''
    def get(self, attribute_set_id: str) -> AttributeSet:
        self.__collection.reset()
        self.__collection.add_field_to_filter(
            field='attribute_set_id',
            value=attribute_set_id,
            condition="eq"
        )
        self.__collection.load_collection()
        if self.__collection.count() < 1:
            raise ValueError(f"Attribute set with ID {attribute_set_id} not found.")
        return self.__collection.get_first_item()

    '''
    Load attribute set entity with attributes from database by name, 
    Raise error if name not exists
    '''
    def get_by_name(self, name: str) -> AttributeSet:
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
    Load attribute set collection with attributes from database by SearchCriteria
    '''
    def get_list(self, search_criteria: SearchCriteria) -> AttributeSetCollection:
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
    Save attribute set entity
    '''
    def save(self, attribute_set: AttributeSet, commit: bool = True) -> None:
        self.__collection.get_resource().save(attribute_set)
        if commit is True:
            self.__collection.get_resource().commit_transaction()

    '''
    Delete attribute set entity
    '''
    def delete(self, attribute_set_id: str, commit: bool = True) -> None:
        self.__collection.get_resource().delete(attribute_set_id)
        if commit is True:
            self.__collection.get_resource().commit_transaction()

    '''
    Add attribute to attribute set
    '''
    def add_to_set(
            self,
            attribute_set: AttributeSet,
            attribute: Attribute,
            commit: bool = True
    ) -> None:
        self.__collection.get_resource().link(attribute, attribute_set)
        if commit is True:
            self.__collection.get_resource().commit_transaction()

    '''
    Remove attribute from attribute set
    '''
    def remove_from_set(
            self,
            attribute_set: AttributeSet,
            attribute: Attribute,
            commit: bool = True
    ) -> None:
        self.__collection.get_resource().unlink(attribute, attribute_set)
        if commit is True:
            self.__collection.get_resource().commit_transaction()
