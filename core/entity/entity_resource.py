from core.entity.entity import Entity
from pandas import DataFrame, read_sql, isna
from core.base.resource import Resource
from core.attribute.attribute_resource import AttributeResource


class EntityResource(Resource):
    ENTITY: Entity = Entity

    ENTITY_TABLE = f"{ENTITY.entity_type}_entity"
    VARCHAR_TABLE = f"{ENTITY.entity_type}_varchar_value"
    NUMERICAL_TABLE = f"{ENTITY.entity_type}_numerical_value"

    '''
    Load entity data from database
    '''
    def load(
            self,
            fields: list,
            filters: list
    ) -> DataFrame:
        query = f"SELECT * FROM {self.ENTITY_TABLE}"
        if len(filters) > 0:
            entity_ids = self.filter_attributes(filters)
            if len(entity_ids) == 0:
                return DataFrame(columns=["entity_id", "attribute_set_id"])
            else:
                entity_ids = ",".join([str(x) for x in entity_ids])
                query += f" WHERE entity_id IN ({entity_ids})"
        result = read_sql(
            query,
            con=self.resource_connection.engine
        )
        return result

    def filter_attributes(
        self,
        filters: list
    ):
        field_to_filter = []
        for filter_ in filters:
            field_to_filter.append(filter_["field"])
        field_to_filter = "'" + "','".join(field_to_filter) + "'"
        query = (f"SELECT e.entity_id, vv.value as varchar_value, nv.value as numerical_value, a.name "
                 f"FROM {AttributeResource.ATTRIBUTE_TABLE} as a "
                 f"LEFT JOIN {self.VARCHAR_TABLE} AS vv ON vv.attribute_id=a.attribute_id "
                 f"LEFT JOIN {self.NUMERICAL_TABLE} AS nv ON nv.attribute_id=a.attribute_id "
                 f"LEFT JOIN {self.ENTITY_TABLE} AS e ON vv.entity_id=e.entity_id OR nv.entity_id=e.entity_id "
                 f"WHERE a.name IN ({field_to_filter})")
        attributes = read_sql(
            query,
            con=self.resource_connection.engine
        )
        attributes["value"] = attributes['varchar_value'].fillna(attributes['numerical_value'])
        attributes = (attributes.drop("varchar_value", axis=1)
                      .drop("numerical_value", axis=1))
        ids = None
        for filter_ in filters:
            filtering = attributes[attributes['name'] == filter_["field"]]
            if filter_["condition"] == "eq":
                filtering = filtering[filtering['value'] == filter_['value']]
            elif filter_["condition"] == "neq":
                filtering = filtering[filtering['value'] != filter_['value']]
            elif filter_["condition"] == "lt":
                filtering = filtering[float(filtering['value']) < float(filter_['value'])]
            elif filter_["condition"] == "gt":
                filtering = filtering[float(filtering['value']) > float(filter_['value'])]
            elif filter_["condition"] == "lteq":
                filtering = filtering[float(filtering['value']) <= float(filter_['value'])]
            elif filter_["condition"] == "gteq":
                filtering = filtering[float(filtering['value']) >= float(filter_['value'])]
            elif filter_["condition"] == "in":
                filtering = filtering[filtering['value'] in filter_['value']]
            elif filter_["condition"] == "not in":
                filtering = filtering[float(filtering['value']) not in filter_['value']]
            if ids is None:
                ids = filtering["entity_id"].tolist()
            else:
                ids = set(ids).intersection(filtering["entity_id"].tolist())
        return list(ids)

    def load_attributes(self, entity_ids: str, attr_set_ids: str):
        query = (
            f"SELECT e.entity_id, a.name, vv.value as varchar_value, nv.value as numerical_value"
            f" FROM attribute_set_attribute_id AS asai "
            f"LEFT JOIN attribute AS a ON a.attribute_id=asai.attribute_id "
            f"LEFT JOIN {self.ENTITY_TABLE} AS e ON e.attribute_set_id = asai.attribute_set_id "
            f"LEFT JOIN {self.VARCHAR_TABLE} AS vv ON vv.attribute_id=asai.attribute_id AND vv.entity_id=e.entity_id "
            f"LEFT JOIN {self.NUMERICAL_TABLE} AS nv ON nv.attribute_id=asai.attribute_id AND nv.entity_id=e.entity_id "
            f"WHERE e.attribute_set_id IN ({attr_set_ids}) and e.entity_id IN ({entity_ids})")
        attributes = read_sql(
            query,
            con=self.resource_connection.engine
        )
        attributes["value"] = attributes['varchar_value'].fillna(attributes['numerical_value'])
        attributes = (attributes.drop("varchar_value", axis=1)
                      .drop("numerical_value", axis=1))
        return attributes

    '''
    Save entity data to database
    '''
    def save(
            self, entity: Entity
    ) -> None:
        entity_id = entity.entity_id if entity.entity_id is not None else "NULL"
        query = (f"INSERT INTO {self.ENTITY_TABLE} VALUES"
                 f" ({entity_id},'{entity.attribute_set_id}')"
                 f" ON DUPLICATE KEY UPDATE"
                 f" attribute_set_id='{entity.attribute_set_id}'")
        self.resource_connection.query(query)
        self.resource_connection.commit()
        if entity_id == "NULL":
            entity_data = read_sql(
                f"SELECT MAX(entity_id) as entity_id from {self.ENTITY_TABLE}",
                con=self.resource_connection.engine
            )
            entity_id = entity_data["entity_id"][0]
        attr_codes = "'" + "','".join(entity.attributes.keys()) + "'"
        query = (f"SELECT a.attribute_id, a.name, a.attribute_type  FROM {AttributeResource.ATTRIBUTE_TABLE} as a "
                 f"WHERE a.name IN ({attr_codes})")
        attributes = read_sql(
            query,
            con=self.resource_connection.engine
        )
        for index, attribute in attributes[attributes['attribute_type'] == "varchar"].iterrows():
            if isna(entity.attributes[attribute['name']]):
                continue
            prepared_data = (f"(NULL,"
                             f"'{entity_id}',"
                             f"'{entity.attributes[attribute['name']]}',"
                             f"'{attribute['attribute_id']}')")
            query = (f"INSERT INTO {self.VARCHAR_TABLE} VALUES"
                     f" {prepared_data}"
                     f" ON DUPLICATE KEY UPDATE"
                     f" value='{entity.attributes[attribute['name']]}'")
            self.resource_connection.query(query)
        for index, attribute in attributes[attributes['attribute_type'] == "numerical"].iterrows():
            if isna(entity.attributes[attribute['name']]):
                continue
            prepared_data = (f"(NULL,"
                             f"'{entity_id}',"
                             f"'{entity.attributes[attribute['name']]}',"
                             f"'{attribute['attribute_id']}')")
            query = (f"INSERT INTO {self.NUMERICAL_TABLE} VALUES"
                     f" {prepared_data}"
                     f" ON DUPLICATE KEY UPDATE"
                     f" value='{entity.attributes[attribute['name']]}'")
            self.resource_connection.query(query)

    '''
    Delete entity
    '''
    def delete(
            self,
            entity_id: str
    ) -> None:
        query = (f"DELETE FROM {self.ENTITY_TABLE} "
                 f"WHERE entity_id={entity_id}")
        self.resource_connection.query(query)
