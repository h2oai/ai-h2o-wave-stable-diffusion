from h2o_wave import Q, ui


async def init_client(q:Q):
    q.page['meta'] = ui.meta_card(box='',
        title='Stable Diffusion | H2O.ai',
        layouts=[
            ui.layout(breakpoint='xs', zones=[
                ui.zone(name='main', size='100vh', zones=[
                    ui.zone(name='header', size='120px'),
                    ui.zone(name='body', size='1', zones=[
                        ui.zone(name='params', size='50%'),
                        ui.zone(name='image', size='50%'),
                    ]),
                    ui.zone(name='footer')
                ])
            ]),
            ui.layout(breakpoint='m', zones=[
                ui.zone(name='main', size='100vh', zones=[
                    ui.zone(name='header', size='120px'),
                    ui.zone(name='body', size='1', direction='row', zones=[
                        ui.zone(name='params', size='50%'),
                        ui.zone(name='image', size='50%'),
                    ]),
                    ui.zone(name='footer')
                ])
            ])
        ]
    )

    q.page['header'] = ui.header_card(
        box='header',
        title='Stable Diffusion',
        subtitle='Make AI Art, powered by H2O AI Cloud',
        image='https://wave.h2o.ai/img/h2o-logo.svg',
        secondary_items=[
            ui.textbox(
                name='prompt',
                label='',
                placeholder='I am thinking of...',
                value=q.args.prompt,
                width='500px',
            ),
            ui.button(
                name='generate',
                label='Make',
                icon='MachineLearning',
            )
        ],
        items=[
            ui.button(
                name='history',
                label='History', icon='History',
                primary=True
            )
        ]
    )

    q.page['footer'] = ui.footer_card('footer',
        caption='',
        items=[
            ui.inline(justify='between', items=[
                ui.inline([
                    ui.text('<a href="https://wave.h2o.ai"> <img alt="h2o-wave" src="https://wave.h2o.ai/img/logo.svg" width="54"><a>'),
                    ui.text('**Made with 💛**<br> by H2O Wave<br><br>')
                ]),
                ui.text('Copyright © 2022 <a href="https://h2o.ai/" target="_blank">H2O.ai</a>, Inc. All rights reserved'),
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