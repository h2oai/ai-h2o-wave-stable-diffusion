from h2o_wave import Q, ui
from .samples import render_samples
from .utils import gap
import os
import shutil

async def run_model(q:Q):
    # Check for input
    if not await validate_prompt_entry(q):
        return
    
    await render_progress(q)

    # run model
    await launch_model(q)

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


async def launch_model(q:Q):
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