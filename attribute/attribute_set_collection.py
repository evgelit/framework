from base.collection import Collection
from attribute.attribute_set import AttributeSet
from attribute.attribute_collection import AttributeCollection
from attribute.attribute_set_resource import AttributeSetResource


class AttributeSetCollection(Collection):
    DTO: AttributeSet = AttributeSet
    resource: AttributeSetResource = AttributeSetResource()
    attribute_collections: dict = {}

    '''
    Create single attribute set entity and connect collection of related attributes
    '''
    def __next__(self) -> AttributeSet:
        if len(self.data.index) == 0:
            raise StopIteration
        if self.iter < len(self.data.index):
            attr_set_id = self.data.iloc[self.iter]['attribute_set_id']
            result = self.DTO(
                dict(
                    zip(
                        self.data.columns.tolist() + ["attribute_collection"],
                        self.data.iloc[self.iter].tolist() + [self.attribute_collections[attr_set_id]]
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
    def get_first_item(self) -> AttributeSet:
        return super().get_first_item()

    '''
    Load collection data from database 
    '''
    def load_collection(self) -> None:
        data = self.resource.load(
            self.fields,
            self.filters,
        )
        relations = self.resource.load_relations(
            data["attribute_set_id"].tolist()
        )
        for att_set_id in data['attribute_set_id']:
            attributes = relations[relations["attribute_set_id"] == att_set_id].drop(
                'attribute_set_id',
                axis=1
            )
            attr_collection = AttributeCollection()
            attr_collection.set_data(attributes)
            self.attribute_collections[att_set_id] = attr_collection
        self.set_data(data)

    '''
    Get current collection resource
    '''
    def get_resource(self) -> AttributeSetResource:
        return self.resource
