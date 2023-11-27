from attribute.attribute import Attribute
from pandas import DataFrame, read_sql
from base.resource import Resource


class AttributeResource(Resource):
    ATTRIBUTE_TABLE = "attribute"

    '''
    Load attribute data from database
    '''
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
        attribute_id = attribute.attribute_id if attribute.attribute_id is not None else "NULL"
        query = (f"INSERT INTO {self.ATTRIBUTE_TABLE} VALUES "
                 f"({attribute_id},"
                 f"'{attribute.name}',"
                 f"'{attribute.attribute_type}',"
                 f"'{attribute.source_model}')"
                 f" ON DUPLICATE KEY UPDATE"
                 f" name='{attribute.name}',"
                 f" attribute_type='{attribute.attribute_type}',"
                 f" source_model='{attribute.source_model}'")
        self.resource_connection.query(query)

    def delete(
            self,
            attribute_id: str
    ) -> None:
        query = (f"DELETE FROM {self.ATTRIBUTE_TABLE} "
                 f"WHERE attribute_id={attribute_id}")
        self.resource_connection.query(query)
