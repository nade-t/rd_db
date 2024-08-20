import sqlalchemy as db
import pymysql

user = "root"
password = "admin"
host = "localhost"
db_name = "rd_scoring"
engine = db.create_engine("mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name), echo=False)
metadata = db.MetaData()
skater_table = db.Table("skater", metadata, autoload_with=engine)
connection = engine.connect()

class Skater():
    """
    Skater class.
    Skater number - a unique number that can have up to 4 digits. 01, 001 and 1 are treated as unique items.
    Skater name - the skater name
    """
    

    def __init__(self):
        self.sk_number = input("Enter skater number: ") 

        while not Skater.valid_sk_number(self.sk_number):
                print("Skater number must be a maximum of 4 digits")
                self.sk_number = input("Enter skater number: ")

        if not Skater.unique_sk_number(self.sk_number):
            print(f"""
                Number {self.sk_number} already exists in the database.
                Amend or view their details from the skater menu.
                """)
            return



        self.sk_name = input("Enter skater name: ")
        while len(self.sk_name) == 0:
                print("Skater name cannot be blank")
                self.sk_name = input("Enter skater name: ")        
        print(f"""
              Confirm new skater details:
              Skater number: {self.sk_number}
              Skater name: {self.sk_name}

              Press Y to save to the database or N to return to the skater menu.
              """)
        choice = input()
        if choice.lower() == "y":
              print("saving to database")
              Skater.insert_into_db(self.sk_number, self.sk_name)
              
        else:
              return

    def unique_sk_number(sk_number):
        check_num =  db.exists().where(skater_table.columns.skater_number == sk_number)

        if check_num is None:
            return True
        else:
            return False


    def valid_sk_number(sk_number):
         return sk_number.isnumeric() and len(sk_number) < 5
        

    def insert_into_db(sk_number, sk_name):
        """
        Takes a skater number and skater name as parameters.
        Inserts the values into the database.
        """
        db_command = db.insert(skater_table).values(skater_number = sk_number, skater_name = sk_name)
        connection.execute(db_command)
        connection.commit()