from h2o_wave import Q, handle_on
from .params import params_card
from .model import *
from .images import images_card
from .utils import clear_page


async def render_page(q:Q):
    # Close dialog, side_panel, and/or notification bar
    await clear_page(q)
    # Render model params card on the left
    await params_card(q)
    # Render images (or placeholder for the images) on the right
    await images_card(q)
    # Handle query args for params, model, images, and utils
    await handle_on(q)
