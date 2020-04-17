from DB import *
class Akun:
  def __init__(self, database):
    self.loginSession=None
    self.database=database
    self.account=[]
    self.getAccount()
  
  def getDatabase(self):
    return self.database
  
  def getAccount(self):
    self.database.getData("select username,password from akun", self.account)

  def register(self, username, password):
    if (self.loginSession==None):
      sql = "INSERT INTO akun (username, password) VALUES (%s, %s)"
      val = (username, password)
      self.database.insertDatabase(sql,val)
      print("Berhasil register")
      # print(self.database.cursor.rowcount, "record inserted.")
      self.getAccount()
      self.login(username, password)
    else:
      print("logout terlebih dahulu")
  
  def login(self,username,password):
    if (self.loginSession==None):
      for key,val in self.account:
        if (username==key):
          if (password==val):
            self.loginSession = (key, val)
            # print(self.loginSession)
            print("Login Berhasil")
          else:
            print("password salah")
    else:
      print("logout terlebih dahulu")

  def logout(self):
    self.loginSession=None
