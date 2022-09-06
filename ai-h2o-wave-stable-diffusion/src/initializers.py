from h2o_wave import Q, ui


async def init_client(q:Q):
    q.page['meta'] = ui.meta_card(box='',
        title='Stable Diffusion | H2O.ai',
        layouts=[
            ui.layout(breakpoint='xs', zones=[
                ui.zone(name='main', size='100vh', zones=[
                    ui.zone(name='header', size='120px'),
                    ui.zone(name='body', size='1'),
                ])
            ])
        ]
    )

    q.page['header'] = ui.header_card(
        box='header',
        title='Stable Diffusion',
        subtitle='By H2O Wave, on H2O AI Cloud',
        image='https://wave.h2o.ai/img/h2o-logo.svg',
        items=[
            ui.button(
                name='stability.ai',
                label='Stability.Ai',
                path='https://stability.ai/'
            ),
            ui.button(
                name='ai-cloud',
                label='H2O AI Cloud',
                path='https://h2o.ai/platform/ai-cloud'
            ),
            ui.button(
                name='wave',
                label='H2O Wave',
                path='https://wave.h2o.ai/'
            )
        ]
    )
