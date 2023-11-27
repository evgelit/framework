from attribute.attribute import Attribute
from attribute.attribute_set import AttributeSet
from attribute.attribute_resource import AttributeResource
from pandas import DataFrame, read_sql
from base.resource import Resource


class AttributeSetResource(Resource):

    ATTRIBUTE_SET_TABLE = "attribute_set"
    ATTRIBUTE_RELATION_TABLE = "attribute_set_attribute_id"

    '''
    Load attribute set from database
    '''
    def load(
            self,
            fields: list,
            filters: list
    ) -> DataFrame:
        query = (f"SELECT {self.prepare_fields(fields)} "
                 f"FROM {self.ATTRIBUTE_SET_TABLE} "
                 f"{self.prepare_filters(filters)}")
        return read_sql(
            query,
            con=self.resource_connection.engine
        )

    '''
    Load attributes related to attribute set 
    '''
    def load_relations(
            self,
            attribute_set_id: list
    ) -> DataFrame:
        filter_ = [
            {
                "field": "attribute_set_id",
                "value": attribute_set_id,
                "condition": "in"
            }
        ]
        query = (f"SELECT * "
                 f"FROM {self.ATTRIBUTE_RELATION_TABLE} as art"
                 f" LEFT JOIN {AttributeResource.ATTRIBUTE_TABLE} as a ON a.attribute_id = art.attribute_id"
                 f" {self.prepare_filters(filter_)}")
        return read_sql(
            query,
            con=self.resource_connection.engine
        )

    '''
    Save attribute set to database
    '''
    def save(
            self, attribute_set: AttributeSet
    ) -> None:
        attribute_set_id = attribute_set.attribute_set_id if attribute_set.attribute_set_id is not None else "NULL"
        query = (f"INSERT INTO {self.ATTRIBUTE_SET_TABLE} VALUES "
                 f"('{attribute_set_id}',"
                 f"'{attribute_set.name}')"
                 f" ON DUPLICATE KEY UPDATE"
                 f" name='{attribute_set.name}'")
        self.resource_connection.query(query)

    '''
    Remove attribute set from database
    '''
    def delete(
            self,
            attribute_set_id: str
    ) -> None:
        query = (f"DELETE FROM {self.ATTRIBUTE_SET_TABLE} "
                 f"WHERE attribute_set_id={attribute_set_id}")
        self.resource_connection.query(query)

    '''
    Connect attribute with attribute set
    '''
    def link(self, attribute: Attribute, attribute_set: AttributeSet) -> None:
        self.unlink(attribute, attribute_set)
        query = (f"INSERT INTO {self.ATTRIBUTE_RELATION_TABLE} VALUES "
                 f"('{attribute_set.attribute_set_id}',"
                 f"'{attribute.attribute_id}')")
        self.resource_connection.query(query)

    '''
    Remove connection between attribute and attribute set
    '''
    def unlink(self, attribute, attribute_set) -> None:
        query = (f"DELETE FROM {self.ATTRIBUTE_RELATION_TABLE} "
                 f"WHERE attribute_id={attribute.attribute_id} "
                 f"AND attribute_set_id={attribute_set.attribute_set_id}")
        self.resource_connection.query(query)

