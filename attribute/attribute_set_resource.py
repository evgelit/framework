from resource.connection_factory import create as create_connection
from resource.resource_connection import ResourceConnection
from attribute.attribute_set import AttributeSet
from attribute.attribute_resource import AttributeResource
from pandas import DataFrame, read_sql
from base.resource import Resource


class AttributeSetResource(Resource):

    ATTRIBUTE_SET_TABLE = "attribute_set"
    ATTRIBUTE_RELATION_TABLE = "attribute_set_attribute_id"

    resource_connection: ResourceConnection

    def __init__(self):
        self.resource_connection = create_connection()

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

    def load_relations(
            self,
            attribute_set_id: list
    ) -> DataFrame:
        filter = [
            {
                "field": "attribute_set_id",
                "value": attribute_set_id,
                "condition": "in"
            }
        ]
        query = (f"SELECT * "
                 f"FROM {self.ATTRIBUTE_RELATION_TABLE} as art"
                 f" LEFT JOIN {AttributeResource.ATTRIBUTE_TABLE} as a ON a.attribute_id = art.attribute_id"
                 f" {self.prepare_filters(filter)}")
        return read_sql(
            query,
            con=self.resource_connection.engine
        )

    def save(
            self, attribute: AttributeSet
    ) -> None:
        pass

