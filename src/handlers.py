from h2o_wave import Q, ui, on, handle_on

from .samples import render_samples
from .params import render_params
from .diffuser import render_sd_page

from .utils import clear_page


async def render_page(q:Q):
    await clear_page(q)

    await render_params(q)
    await render_samples(q)

    await handle_on(q)


@on()
async def history(q:Q):
    q.page['meta'].notification_bar = ui.notification_bar(
        text='Feature coming soon',
        position='top-right'
    )
