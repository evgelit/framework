class DTOValidator:

    REQUIRED = []
    DATA_MAP = {}

    def _validate(self):
        miss_attr = self.REQUIRED - self.__dict__.keys()
        if len(miss_attr) > 0:
            raise Exception(f"Required attributes \"{', '.join(miss_attr)}\" not set")
        unknown_attr = self.__dict__.keys() - self.DATA_MAP.keys()
        if len(unknown_attr) > 0:
            raise Exception(
                f"Unknown attributes \"{', '.join(unknown_attr)}\" "
                f"for {self.__class__.__name__}"
            )
        for key, data_type in self.DATA_MAP.items():
            if key not in self.__dict__:
                continue
            if type(self.__dict__[key]) not in data_type:
                raise Exception(
                    f"Unexpected type for attribute \"{key}\" "
                    f"got {str(type(self.__dict__[key]))}, "
                    f"expected {', '.join([str(x) for x in data_type])}"
                )

