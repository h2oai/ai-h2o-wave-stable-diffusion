from h2o_wave import Q, ui
from .utils import gap
from .static import styles, artists

async def render_params(q):
    n_iter = q.args.n_iter or 2
    num_samples = q.args.num_samples or 3
    seed = q.args.seed or '1245'
    sampler = q.args.sampler or 'ddim'
    ddim_steps = q.args.ddim_steps or 10
    ddim_eta = q.args.ddim_eta or 0.0
    downsampling_factor = q.args.downsampling_factor or 8
    scale = q.args.scale or 7.5
    precision = q.args.precision or "autocast"
    
    latent_channels = q.args.latent_channels or 4
    img_height = q.args.img_height or 512
    img_width = q.args.img_width or 512



    q.page['params'] = ui.form_card('params', items=[
        ui.text_l('Model Parameters'),
        ui.separator(),
        ui.textbox(
            name='seed',
            label='Seed',
            mask='9  9  9  9',
            value=seed,
            width='30%',
        ),
        ui.slider(
            name='n_iter',
            label='Iterations',
            value=n_iter,
            min=0,
            max=10,
            tooltip='Sample this often'
        ),
        ui.slider(
            name='num_samples',
            label='Samples',
            value=num_samples,
            min=1,
            max=10,
            tooltip='How many samples to produce for each given prompt'
        ),
        
        ui.separator(),
        # *gap(2),
        ui.choice_group(
            name='sampler',
            label='Sampler',
            value=sampler,
            choices=[ui.choice('ddim', 'DDIM'), ui.choice('plms', 'PLMS')],
            inline=True,
            trigger=True,
            tooltip='Which sampling to use'
        ),  
        ui.inline([
            ui.spinbox(
                name='ddim_steps',
                label='DDIM Steps',
                value=ddim_steps,
                min=1,
                step=1,
                width='30%',
                visible=sampler=='ddim'
            ),
            *gap(5),
            ui.spinbox(
                name='ddim_eta',
                label='DDIM ETA',
                value=ddim_eta,
                min=0.0,
                step=0.1,
                width='30%',
                visible=sampler=='ddim'
            )
        ]),
        *gap(2),
        ui.slider(
            name='downsampling_factor',
            label='Downsampling Factor',
            value=downsampling_factor,
            min=0,
            max=10,
        ),
        ui.separator(),
        ui.choice_group(
            name='precision',
            label='Precision',
            value=precision,
            choices=[ui.choice('autocast', 'Autocast'), ui.choice('full', 'Full')],
            inline=True,
            tooltip='Evaluate at this precision'
        ),
        ui.spinbox(
            name='scale',
            label='Scale',
            value=scale,
            min=0.0,
            step=0.1,
            width='10%',
            # tooltip="Unconditional guidance scale: eps = eps(x, empty) + scale * (eps(x, cond) - eps(x, empty))"
        ),
        *gap(2),
        ui.slider(
            name='latent_channels',
            label='Latent Channels',
            value=latent_channels,
            min=0,
            max=10,
        ),
        ui.separator(),
        ui.inline([
            ui.spinbox(
                name='height',
                label='Image Height (px)',
                min=512,
                max=1024,
                value=img_height,
                width='250px',
            ),
            *gap(5),
            ui.spinbox(
                name='width',
                label='Image Width (px)',
                min=512,
                max=1024,
                value=img_width,
                width='250px',
            ),
            
        ]),
        
        
        
    ])


async def render_keywords(q:Q):
    q.page['meta'].side_panel = ui.side_panel(title='', items=[
        
        ui.button(
            name='append',
            label='Append to Prompt',
            icon='SkypeArrow',
            primary=True
        ),
        ui.separator('Prompt Suggestions'),
        ui.picker(
            name='styles',
            label='Styles',
            choices=[ui.choice(key, val) for key, val in styles.items()]
        ),
        ui.dropdown(
            name='artists',
            label='Artists',
            choices=[ui.choice(key, val) for key, val in artists.items()],
            placeholder='Select one or more',
            values=q.args.artists or []
        ),
        ui.separator(),
        ui.button(
            name='cancel',
            label='Cancel',
            icon='Cancel',
        ),
    ])
