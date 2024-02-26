from sqlalchemy import create_engine

class Connection:
    def __init__(self, url:str = None) -> None:
        if url and isinstance(url, str):
            self.url = url
        else:
            # for sharing purpose url is kept here, otherwise we should keep it in env files.
            # self.url = "sqlite:///mygreen.db"
            self.url = "postgresql+psycopg2://greenlit_star_user:GCG2vjRcyGVJ5K49xYq9QC8QYw5mNepY@dpg-cndv6r0l6cac73bh4ma0-a.oregon-postgres.render.com/greenlit_star"

    def get_connection(self) -> None:
        return create_engine(
            url = self.url,
            echo = True
        )

    def connect(self):
        try:
            engine = self.get_connection()
            print("Connection to DB is successfully.")
            return engine
        except Exception as ex:
            print("Connection failed. ERROR(s): \n", ex)
