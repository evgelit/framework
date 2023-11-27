class SearchCriteria:

    filters: list

    """
        Input example:
        [
            {"field": "field1", "value": "value1", "condition": "eq"},
            {"field": "field2", "value": "value2", "condition": "neq"},
            {"field": "field3", "value": "value3", "condition": "gteq"},
            {"field": "field4", "value": ["value1", "value12", "value3"], "condition": "in"},
        ]
        Allowed conditions:
            eq - equal
            neq - not equal
            gt - greater than
            lt - lower than
            gteq - greater than or equal
            lteq - lower than or equal
            in - in set
            not in - not in set
    """
    def __init__(self, filters: list):
        self.filters = filters
