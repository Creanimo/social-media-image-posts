from ._anvil_designer import view_imageAssetsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_imageAssets(view_imageAssetsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = []

    for row in app_tables.images.search():
      self.repeating_panel_1.items.append({'name': row['name']})
