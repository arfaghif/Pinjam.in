import mysql.connector
class DB:
  def __init__(self, password, database):
    self.database = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=password,
      database=database
    )
    self.cursor = self.database.cursor()

  def navigateDatabase(self,query):
    self.cursor.execute(query)
    self.database.commit()
    # for el in self.cursor:
    #   print(el)

  def getData(self,query,data):
    self.cursor.execute(query)
    self.queryResult(data)
  
  def insertDatabase(self,query,val):
    self.cursor.execute(query,val)
    self.database.commit()

  def queryResult(self,data):
    for el in self.cursor:
      data.append(el)
    return data