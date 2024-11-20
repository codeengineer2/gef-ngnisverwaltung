import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT GID,Freie_Zellen, Besetzte_Zellen,Direktor,Name FROM Gefaengnisse"))
  cursor.close()
  print("Daten erhalten", res)
  
  return res
#@anvil.server.callable
# def get_zellen(row="x"):
#   conn = sqlite3.connect(data_files["prison_management.db"])
#   cursor = conn.cursor()
#   res = list(cursor.execute("SELECT ZID,GID,anz_häft FROM Zellen"))
#   cursor.close()
#   print("Daten erhalten", res)