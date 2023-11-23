from sqlalchemy import create_engine, Connection, Engine, text


class ResourceConnection:

    engine: Engine = None
    connection: Connection = None
    has_error: bool = False
    error: str = ""

    def __init__(
            self,
            user: str,
            password: str,
            host: str,
            database: str
    ):
        try:
            self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
            self.connection = self.engine.connect()
        except BaseException as e:
            self.has_error = True
            self.error = str(e)

    def query(self, query: str):
        self.connection.execute(text(query))
