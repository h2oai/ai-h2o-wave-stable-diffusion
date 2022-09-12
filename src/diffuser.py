import os
from h2o_wave import Q, ui, on, handle_on
from .utils import center, gap
import shutil

async def render_sd_page(q:Q):
    widgets = await get_prompt_widgets(q)

    await handle_on(q)

    if q.client.output_widgets:
        widgets.extend([
            *q.client.output_widgets
    ])

    q.page['body'] = ui.form_card('body', items=widgets)



@on('generate')
async def generate(q:Q):
    widgets = await get_prompt_widgets(q)
    widgets.extend([
        *gap(5),
        *center([
            ui.progress(
                label='Running Stable Diffusion Model. Making  AI Art.',
                width='70%'
            )
        ])
    ])
    q.page['body'] = ui.form_card('body', items=widgets)
    await q.page.save()

    await run_model(q)


@on('width')
async def render(q:Q):
    width = q.args.width or 300
    q.client.output_widgets = widgets = [
        *gap(5),
        *center([
            ui.image(
                title='image2',
                path=q.client.image,
                width=f'{width}'
            )
        ]),
        *gap(5),
        *center([
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



async def get_prompt_widgets(q:Q):
    return []
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
        *center([
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

async def run_model(q:Q):
    try:
        print("Starting model run")
        os.mkdir('output')
        os.system(" ".join([
            'cd',
            'stable-diffusion-main',
            '&&'
            'ldm_env2/bin/python',
            'scripts/txt2img.py',
            '--skip_grid',
            '--n_samples',
            '1',
            '--prompt',
            f'"{q.args.prompt}"',
            '--outdir',
            '"../output/"'
        ]))

        file = os.listdir('output/samples')[0]
        q.client.image = img_path = (await q.site.upload([f'output/samples/{file}']))[0]

        shutil.rmtree('output')
        print("finished model run")

        width = q.args.width or 300

        q.client.output_widgets = widgets = [
             *gap(5),
            *center([
                ui.image(
                    title='image2',
                    path=img_path,
                    width=f'{width}'
                )
            ]),
            *gap(5),
            *center([
                ui.slider(
                    name='width',
                    label='Width',
                    value=width,
                    min=10,
                    max=800,
                    trigger=True,
                    width='50%',
                )
            ])
       ]

    except Exception as e:
        print(f"Failed to run the model. {e}")
