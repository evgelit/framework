from core.resource.connection_factory import create as create_connection
from core.resource.resource_connection import ResourceConnection


class Resource:

    OPERATORS = {
        "eq": "=",
        "neq": "<>",
        "gt": ">",
        "gteq": ">=",
        "lt": "<",
        "lteq": "<=",
    }

    resource_connection: ResourceConnection

    def __init__(self):
        self.resource_connection = create_connection()

    def prepare_fields(self, fields: list) -> str:
        if len(fields) == 0:
            return "*"
        return ", ".join(fields)

    def prepare_filters(self, filters: list) -> str:
        if len(filters) == 0:
            return ""
        prepared_filters = []
        for filter_ in filters:
            if filter_["condition"] in self.OPERATORS:
                prepared_filters.append(
                    " ".join(
                        [
                            filter_["field"],
                            self.OPERATORS[filter_["condition"]],
                            "'" + filter_["value"] + "'"
                        ]
                    )
                )
                continue
            prepared_filter = (
                    filter_["field"] + " "
                    + filter_["condition"] + "("
                    + ",".join(["'" + str(val) + "'" for val in filter_["value"]]) + ")"
            )
            prepared_filters.append(prepared_filter)
        return "WHERE " + " AND ".join(prepared_filters)

    def commit_transaction(self) -> None:
        self.resource_connection.commit()
