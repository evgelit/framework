class DTO:

    DATA_MAP = {}

    """
    Setting to DTO attributes and values
    Input example: data = {"code": "value"} 
    """
    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    """
    Return DTO attributes as list
    """
    def to_list(self) -> list:
        values = []
        for attr in self.DATA_MAP:
            if attr not in self.__dict__:
                values.append(None)
                continue
            values.append(self.__dict__[attr])
        return values

    """
    Return DTO attributes as dictionary
    """
    def to_dict(self) -> list:
        values = {}
        for attr in self.DATA_MAP:
            if attr not in self.__dict__:
                values[attr] = None
                continue
            values[attr] = self.__dict__[attr]
        return values
