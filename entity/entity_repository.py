from base.search_criteria import SearchCriteria
from entity.entity import Entity
from entity.entity_collection import EntityCollection


class EntityRepository:

    __collection = EntityCollection()

    '''
    Create entity
    '''
    def create(self, data: dict) -> Entity:
        return Entity(data)

    '''
    Load entity from database by entity ID, 
    Raise error if ID not exists
    '''
    def get(self, entity_id: str) -> Entity:
        self.__collection.reset()
        self.__collection.add_field_to_filter(
            field='entity_id',
            value=entity_id,
            condition="eq"
        )
        self.__collection.load_collection()
        if self.__collection.count() < 1:
            raise ValueError(f"Entity with ID {entity_id} not found.")
        return self.__collection.get_first_item()

    '''
    Load entities collection from database by SearchCriteria
    '''
    def get_list(self, search_criteria: SearchCriteria) -> EntityCollection:
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
    Save entity
    '''
    def save(self, entity: Entity, commit: bool = True) -> None:
        self.__collection.get_resource().save(entity)
        if commit is True:
            self.__collection.get_resource().commit_transaction()

    '''
    Delete entity
    '''
    def delete(self, entity_id: int or str, commit: bool = True) -> None:
        self.__collection.get_resource().delete(entity_id)
        if commit is True:
            self.__collection.get_resource().commit_transaction()
