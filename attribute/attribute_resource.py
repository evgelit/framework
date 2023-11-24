from resource.connection_factory import create as create_connection
from resource.resource_connection import ResourceConnection
from attribute.attribute import Attribute
from pandas import DataFrame, read_sql
from base.resource import Resource

class AttributeResource(Resource):

    ATTRIBUTE_TABLE = "attribute"

    resource_connection: ResourceConnection

    def __init__(self):
        self.resource_connection = create_connection()

    def load(
            self,
            fields: list,
            filters: list
    ) -> DataFrame:
        query = (f"SELECT {self.prepare_fields(fields)} "
                 f"FROM {self.ATTRIBUTE_TABLE} "
                 f"{self.prepare_filters(filters)}")
        return read_sql(
            query,
            con=self.resource_connection.engine
        )

    def save(
            self, attribute: Attribute
    ) -> None:
        pass

