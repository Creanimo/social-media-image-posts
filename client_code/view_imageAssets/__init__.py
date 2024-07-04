from ._anvil_designer import view_imageAssetsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_imageAssets(view_imageAssetsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = anvil.server.call('get_image_cards')

  def outlined_button_1_click(self, **event_args):
    open_form('edit_imageAsset')
