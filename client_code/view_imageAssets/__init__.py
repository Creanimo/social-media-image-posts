from ._anvil_designer import view_imageAssetsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_imageAssets(view_imageAssetsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = (
     {'from': 'Joe', 'subject': 'Latest tech report'},
     {'from': 'Sally', 'subject': 'Movie night on Friday?'},
     {'from': 'Ada', 'subject': 'My top 10 cat videos'},
   )
