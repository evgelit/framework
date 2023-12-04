from core.base.collection import Collection
from core.entity.entity import Entity
from core.entity.entity_resource import EntityResource
from pandas import DataFrame
from numpy import nan


class EntityCollection(Collection):

    DTO: Entity = Entity
    __resource: EntityResource = EntityResource()
    __attributes: DataFrame = DataFrame()

    '''
    Create single entity from loaded data
    '''
    def __next__(self) -> Entity:
        if len(self.data.index) == 0:
            raise StopIteration
        if self.iter < len(self.data.index):
            entity_id = self.data.iloc[self.iter]['entity_id']
            attributes = dict(
                zip(
                    self.__attributes[self.__attributes['entity_id'] == entity_id]['name'].tolist(),
                    self.__attributes[self.__attributes['entity_id'] == entity_id]['value'].tolist()
                )
            )
            result = self.DTO(
                dict(
                    zip(
                        self.data.columns.tolist() + ['entity_type', 'attributes'],
                        self.data.iloc[self.iter].tolist() + [Entity.entity_type, attributes]
                    )
                )
            )
            self.iter += 1
            return result
        else:
            raise StopIteration

    '''
    Get first item from collection
    '''
    def get_first_item(self) -> Entity:
        entity_id = self.data.iloc[0]['entity_id']
        attributes = dict(
            zip(
                self.__attributes[self.__attributes['entity_id'] == entity_id]['name'].tolist(),
                self.__attributes[self.__attributes['entity_id'] == entity_id]['value'].tolist()
            )
        )
        return self.DTO(
            dict(
                zip(
                    self.data.columns.tolist() + ['entity_type', 'attributes'],
                    self.data.iloc[self.iter].tolist() + [Entity.entity_type, attributes]
                )
            )
        )

    '''
    Load collection data from database 
    '''
    def load_collection(self) -> None:
        data = self.__resource.load(
            self.fields,
            self.filters,
        )
        self.__attributes = self.__resource.load_attributes(
            ",".join([str(entity_id) for entity_id in data['entity_id'].tolist()]),
            ",".join([str(set_id) for set_id in data['attribute_set_id'].tolist()])
        )
        self.__attributes = self.__attributes.replace(nan, None)
        self.set_data(data)

    '''
    Get current collection resource
    '''
    def get_resource(self) -> EntityResource:
        return self.__resource
