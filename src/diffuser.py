import os
import random
from turtle import width
from h2o_wave import Q, ui, on, handle_on
from .utils import inline_center, gap


async def render_diffuser(q:Q):
    widgets = await get_prompt_widgets(q)

    await handle_on(q)

    if q.client.output_widgets:
        widgets.extend([
            *q.client.output_widgets
    ])

    q.page['body'] = ui.form_card('body', items=widgets)


@on()
async def about(q:Q):
    q.page['meta'].dialog = ui.dialog(
        title='About Stable Diffusion by H2O Wave',
        closable=True,
        items=[
            ui.separator(),
            *inline_center([
                ui.text("""
A latent text-to-image diffusion model capable of generating photo-realistic images given any text input.

This AI web app is made with H2O Wave, an open-source Python development framework for fast and easy development of real-time interactive AI apps with sophisticated visualizations.

With this app, you can get creative and create stunning AI art within in real-time.

This app is powered by the the H2O AI Cloud, which solves complex business problems and accelerates the discovery of new ideas with results you can understand and trust.
                """)
            ])
        ]
    )


@on('generate')
async def generate(q:Q):
    os.system("echo Hello from the other side!")
    os.system("make run_sd")
    widgets = await get_prompt_widgets(q)
    widgets.extend([
        *gap(5),
        *inline_center([
            ui.progress(
                label='Running Stable Diffusion Model. Making  AI Art.',
                width='70%'
            )
        ])
    ])
    q.page['body'] = ui.form_card('body', items=widgets)
    await q.page.save()

    q.client.image='https://wave.h2o.ai/img/logo.svg' \
        if random.randint(1,2) == 1 else 'https://wave.h2o.ai/img/h2o-logo.svg'
    
    await q.sleep(2)
    await render(q)


@on('width')
async def render(q:Q):
    width = q.args.width or 300
    q.client.output_widgets = widgets = [
        *gap(5),
        *inline_center([
            ui.image(
                title='image2',
                path=q.client.image,
                width=f'{width}'
            )
        ]),
        *gap(5),
        *inline_center([
            ui.slider(
                name='width',
                label='Width',
                value=width,
                min=10,
                max=800,
                trigger=True,
                width='50%'
            )
        ]),
        
    ]



    q.page['body'] = ui.form_card('body', items=widgets)


async def get_prompt_widgets(q:Q):

    return [
    *gap(1),
        ui.inline(justify='end', items=[
            ui.button(
                name='about',
                label='About',
                icon='Info'
            )
        ]),
        *gap(3),
        *inline_center([
            ui.textbox(
                name='prompt',
                label='',
                placeholder='I am thinking of...',
                value=q.args.prompt,
                width='50%'
            ),
            *gap(2),
            ui.button(
                name='generate',
                label='Make AI Art',
                icon='MachineLearning',
                primary=True
            )
        ])
    ]
