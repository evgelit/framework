from base.collection import Collection
from attribute.attribute_set import AttributeSet
from attribute.attribute_collection import AttributeCollection
from attribute.attribute_set_resource import AttributeSetResource


class AttributeSetCollection(Collection):

    DTO: AttributeSet = AttributeSet
    resource: AttributeSetResource = AttributeSetResource()
    attribute_collections: dict = {}

    def __next__(self) -> AttributeSet:
        if self.iter <= self.iter_max:
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

    def get_resource(self) -> AttributeSetResource:
        return self.resource
