from h2o_wave import Q, ui, on, handle_on
from .utils import center
from .initializers import render_header

from .static import styles, artists

from .samples import render_samples
from .params import render_params, render_keywords
# from .diffuser import render_sd_page
from .model import run_model
from .images import render_images

from .utils import clear_page


async def render_page(q:Q):
    await clear_page(q)

    await render_params(q)

    await handle_on(q)


@on()
async def about(q:Q):
    q.page['meta'].dialog = ui.dialog(
        title='About Stable Diffusion by H2O Wave',
        closable=True,
        items=[
            ui.separator(),
            *center([
                ui.text("""
A latent text-to-image diffusion model capable of generating photo-realistic images given any text input.

This AI app uses Stability Ai's Stable Diffusion Model (1.4) and made with H2O Wave, an open-source Python development framework for fast and easy development of real-time interactive AI apps with sophisticated visualizations.

With this app, you can create stunning AI art in real-time.

This app is powered by the the H2O AI Cloud, which solves complex business problems and accelerates the discovery of new ideas with results you can understand and trust.
                """)
            ])
        ]
    )



@on()
async def history(q:Q):
    q.page['meta'].notification_bar = ui.notification_bar(
        text='Feature coming soon',
        position='top-right'
    )


@on()
async def generate(q:Q):
    await run_model(q)


@on('prev')
@on('next')
@on('#{num}')
async def render_image(q:Q):
    await render_samples(q)

@on()
async def tips(q:Q):
    await render_keywords(q)

@on()
async def append(q:Q):
    
    if q.args.styles:
        q.client.prompt += ', ' ; q.client.prompt += ", ".join([styles[style] for style in q.args.styles])
    if q.args.artists:
        q.client.prompt += ', ' ; q.client.prompt +=  ", ".join([artists[artist] for artist in q.args.artists])
    

    await render_header(q)
