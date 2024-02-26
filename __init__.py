from database.connect import Connection
from database.operations import Operation
from database.models import Base


connection_obj = Connection()
engine = connection_obj.connect()

print("====>>> Create Tables")
Base.metadata.create_all(bind=engine)

query = Operation()
