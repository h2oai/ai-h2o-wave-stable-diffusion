from h2o_wave import Q, ui, on
from .images import render_samples
from .utils import gap
from .initializers import render_header
from .static import styles, artists
import os
import shutil


async def run_model(q:Q):
    # Check for input
    if not await validate_prompt_entry(q):
        return
    
    await render_progress(q)

    # run model
    await model_predict(q)

    await render_samples(q)



async def validate_prompt_entry(q:Q):
    if not q.args.prompt:
        q.page['meta'].notification_bar = ui.notification_bar(
            type='error',
            text='Please enter a prompt',
            position='top-center'
        )
        return False

    q.client.prompt = q.args.prompt
    return True


async def render_progress(q:Q):
    q.page['image'] = ui.form_card('image', items=[
        *gap(5),
        ui.progress(
            label='Running model to make AI Art',
            caption="Please wait, this could take a few minutes..."
        )
    ])
    
    await q.page.save()


async def model_predict(q:Q):
    if os.path.exists('output2'):
        shutil.rmtree('output2', ignore_errors=False)
    
    q.client.images = None
    q.client.prompt = ""
    os.mkdir('output2')

    os.system(" ".join([
        'cd',
        'stable-diffusion-main',
        '&&'
        'ldm_env2/bin/python',
        'scripts/txt2img.py',
        '--skip_grid',
        # '--plms',
        '--n_samples',
        '5',
        '--ddim_steps',
        '10',
        '--n_iter',
        '1',
        '--prompt',
        f'"{q.args.prompt}"',
        '--outdir',
        '"../output2"'
    ]))


    print("finished model run")



@on()
async def generate(q:Q):
    await run_model(q)


@on()
async def append(q:Q):

    if q.args.styles:
        q.client.prompt += ', ' ; q.client.prompt += ", ".join([styles[style] for style in q.args.styles])
    if q.args.artists:
        q.client.prompt += ', ' ; q.client.prompt +=  ", ".join([artists[artist] for artist in q.args.artists])


    await render_header(q)
