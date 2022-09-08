from h2o_wave import Q, ui

async def render_params(q):
    q.page['params'] = ui.form_card('params', items=[
        ui.text_l('Model Parameters'),
        ui.separator(),
        ui.toggle(
            name='plms',
            label='plms sampling',
            value=q.args.plms or True,
            disabled=True,
        ),
        ui.slider(
            name='n_samples',
            label='Number of Images',
            value=q.args.n_samples or 5,
            min=1,
            max=10,
            disabled=True
        ),
        ui.spinbox(
            name='height',
            label='Image Height (px)',
            min=512,
            max=1024,
            value=q.args.height or 512,
            disabled=True,
            width='30%',
        ),
        ui.spinbox(
            name='width',
            label='Image Width (px)',
            min=512,
            max=1024,
            value=q.args.width or 512,
            disabled=True,
            width='30%',
        ),
    ])