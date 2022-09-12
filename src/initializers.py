from h2o_wave import Q, ui

async def init_client(q):
    await init_meta(q)
    
    q.client.prompt = 'spaceship, realistic'

    await render_header(q)

    await render_footer(q)


async def init_meta(q):
    q.page['meta'] = ui.meta_card(box='',
        title='Stable Diffusion | H2O.ai',
        theme='h2o-dark',
        layouts=[
            ui.layout(breakpoint='m', zones=[
                ui.zone(name='main', size='100vh', zones=[
                    ui.zone(name='header', size='165px'),
                    ui.zone(name='body', size='1', direction='row', zones=[
                        ui.zone(name='params', size='30%'),
                        ui.zone(name='image', size='70%'),
                    ]),
                    # ui.zone(name='image', size='1'),
                    ui.zone(name='footer')
                ])
            ])
        ]
    )


"""UI header with logo, titles, prompt field and actions"""
async def render_header(q:Q):
    # Logo, titles, prompt
    q.page['header'] = ui.header_card(
        box=ui.box('header', height='90px'),
        color='card',
        title='Stable Diffusion',
        subtitle='Make AI Art, powered by H2O AI Cloud',
        image='https://wave.h2o.ai/img/h2o-logo.svg',
        secondary_items=[
            ui.textbox(
                name='prompt',
                placeholder='I am thinking of...',
                value=q.args.prompt,
                width='600px',
            )
        ],
        # About the app and history
        items=[
            ui.mini_button(
                name='about',
                label='About',
                icon='info'
            ),
            ui.mini_button(
                name='history',
                label='History',
                icon='History',
            )
        ]
    )

    # Run-model and Prompt-tips buttons
    q.page['actions'] = ui.form_card(
        box=ui.box('header', height='65px'),
        items=[
            ui.buttons(justify='center', items=[
                ui.button(
                    name='generate',
                    label='Make AI Art',
                    icon='MachineLearning',
                    primary=True
                ),
                ui.button(
                    name='tips',
                    label='Prompt Tips',
                    icon='Lightbulb',
                )
            ])
        ]
    )


"""UI footer with Wave logo, and quick links for H2O.ai and Stability.Ai"""
async def render_footer(q:Q):
    q.page['footer'] = ui.footer_card('footer', '', items=[
        ui.inline(justify='between', items=[
            # Wave logo
            ui.inline([
                ui.text('<a href="https://wave.h2o.ai"> <img alt="h2o-wave" src="https://wave.h2o.ai/img/logo.svg" width="54"><a>'),
                ui.text('**Made with 💛**<br> by H2O Wave<br><br>')
            ]),
            ui.text('Copyright © 2022 <a href="https://h2o.ai/" target="_blank">H2O.ai</a>, Inc. All rights reserved'),
            # Quick links
            ui.inline([
                ui.links(label='Stability.ai', items=[
                    ui.link(label='Stability.Ai', path='https://stability.ai/', target='_blank'),
                    ui.link(label='Stable Diffusion', path='https://stability.ai/blog/stable-diffusion-public-release', target='_blank')
                ]),
                ui.links(label='H2O.ai', items=[
                    ui.link(label='H2O AI Cloud', path='https://h2o.ai/platform/ai-cloud', target='_blank'),
                    ui.link(label='90-day free trial', path='https://wave.h2o.ai/', target='_blank')
                ])
            ])
        ])
    ])

    # await render_images(q)
