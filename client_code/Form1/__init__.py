from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.gef = [(GID,Freie_Zellen, Besetzte_Zellen,Direktor,Name) for GID,Freie_Zellen, Besetzte_Zellen,Direktor,Name in anvil.server.call("get_gefaengnisse") ]
    # Any code you write here will run before the form opens.
    gefa = []
    #self.zele = [(ZID, GID, anz_häft) for ZID, GID, anz_häft in anvil.server.call("get_zellen")]

    for i in self.gef:
      gefa.append(i[4])
    self.gefaengnisse_drop_down.items = gefa
    self.label_direktor.text = f"{self.gef[0][3]}" 
    self.label_freie_zellen.text = f"{self.gef[0][1]}"
    #self.repeating_zellen.items = [{'zellennummer': {y[0]}, 'anzahl_häftlinge': {y[2]}}
     #                              for y in self.zele
      #                            ]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_direktor.text = "" 
    self.label_freie_zellen.text = ""
    selectedvalue = self.gefaengnisse_drop_down.selected_value
    for x in self.gef:
      if selectedvalue == x[4]:
        self.label_direktor.text  = f"{x[3]}"
        self.label_freie_zellen.text = f"{x[1]}"
    

 



  
 
