import logging
logging.basicConfig(filename='app.log', 
                    level=logging.INFO, 
                    filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

class Operation:

    def add_film_to_company(self, engine, table, match, newfilm):
        try:
            print(table)
            print(match)
            print(newfilm)
            stmt = select(table).where(table.contact_email == match)
            with Session(engine) as session:
                for row in session.execute(stmt):
                    row[0].films.append(newfilm)

                session.commit()
            return "success"
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to add film to company: \n{ex}"
            )
            return "failed"

    def get_films_of_company(self, engine, table, email):
        ''' gets all the films of a company'''
        try:
            stmt = select(table).where(table.contact_email == email)
            with Session(engine) as session:
                for row in session.scalars(stmt):
                    print(row.films)

        except Exception as ex:
            logging.error(
                f"ERROR: Unable to get films of a company: \n{ex}"
            )

    def get_company_of_film(self, engine, table, id):
        ''' gets the company to which film belongs.  '''
        try:
            stmt = select(table).where(table.id == id)
            with Session(engine) as session:
                for row in session.scalars(stmt):
                    print(row.company)

        except Exception as ex:
            logging.error(
                f"ERROR: Unable to get film of a company: \n{ex}"
            )

    
    def insert_data(self, engine, table, data):
        try:
            stmt = (
                insert(table).
                values(data)
            )
            with Session(engine) as session:
                session.execute(stmt)
                session.commit()
            
            return "success"
        
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to create row of table: {table}, \n{ex}"
            )
            return "failed"

    def create_data(self, engine, tables) -> bool:
        try:
            with Session(engine) as session:
                session.add_all(tables)    
                session.commit()
                return True

        except Exception as ex:
            logging.error(
                f"ERROR: Unable to create table in DB: \n{ex}"
            )
            return False

    
    def get_role_ids(self, engine, table, param, table1_email):
        try:
            with Session(engine) as session:
                stmt1 = session.query(table).filter(getattr(table, param) == table1_email).first()
                return stmt1.id
            
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to get role IDs: \n{ex}"
            )
            

    def create_role_user_film(self, engine, table1, param1, value1,
                    table2, param2, value2, 
                    final_table, role) -> str:
        try:
            user_id = self.get_role_ids(engine, table1, param1, value1)
            film_id = self.get_role_ids(engine, table2, param2, value2)

            mapping = final_table(user_id=user_id, film_id=film_id, role=role)
            self.create_data(engine=engine, tables=[mapping])
            return "success"
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to create role: \n{ex}"
            )
            return "failed"
    
    def create_role_user_company(self, engine, table1, param1, value1,
                    table2, param2, value2, 
                    final_table, role) -> str:
        try:
            user_id = self.get_role_ids(engine, table1, param1, value1)
            company_id = self.get_role_ids(engine, table2, param2, value2)

            mapping = final_table(user_id=user_id, company_id=company_id, role=role)
            self.create_data(engine=engine, tables=[mapping])
            return "success"
        
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to create role: \n{ex}"
            )
            return "failed"

    def read_data(self, engine, table, limit=10):
        try:
            with Session(engine) as session:
                users = session.query(table).limit(limit).all()
                res = []
                for user in users:
                    res.append(user)

                return res
        
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to read rows of table: {table}, \n{ex}"
            )


    def read_filtered_role(self, engine, table, param, value) -> list:
        try:
            with Session(engine) as session:
                row_to_read = session.query(table).filter(getattr(table, param) == value).all()
                res = []
                for row in row_to_read:
                    res.append(row)
        
            return res
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to read rows of table: {table}, \n{ex}"
            )


    def update_data(self, engine, table, param, value, data) -> str:
        try:
            with Session(engine) as session:
                row_to_update = session.query(table).filter(getattr(table, param) == value).first()

                if row_to_update:
                    for col, val in data.items():
                        setattr(row_to_update, col, val)

                    session.commit()
                    print(f"Updated successfully: data: {data}")
                    return "success"
                else:
                    print("Row not found.")
                    return "failed"
        
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to update row of table: {table}, \n{ex}"
            )
    

    def delete_data(self, engine, table, param, value) -> str:
        try:
            with Session(engine) as session:
                row_to_delete = session.query(table).filter(getattr(table, param) == value).first()
                
                if row_to_delete:
                    session.delete(row_to_delete)
                    session.commit()
                    print("deleted successfully.")
                    return "success"
                else:
                    print("Row not found.")
                    return "failed"
        
        except Exception as ex:
            logging.error(
                f"ERROR: Unable to read rows of table: {table}, \n{ex}"
            )


