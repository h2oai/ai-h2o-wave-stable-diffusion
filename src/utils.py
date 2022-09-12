from h2o_wave import Q, ui, on


async def error(q:Q, err:str):
    q.page['meta'].notification_bar = ui.notification_bar(
        type='error',
        text='Oops, something went wrong',
        position='top-center'
    )

    print(f"ERROR: {err}")


def gap(size:int):
    return [ui.text('') for _ in range(size)]


def center(items, gap_size:int=0):
    return [ui.inline(justify='center', items=items), *gap(gap_size)]


async def clear_page(q:Q):
    q.page['meta'].dialog = None
    q.page['meta'].notification_bar = None
    q.page['meta'].side_panel = None


async def render_about_dialog(q:Q):
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


async def render_FCS_notification(q:Q):
    q.page['meta'].notification_bar = ui.notification_bar(
        text='Feature coming soon',
        position='top-right'
    )


@on()
async def about(q:Q):
    await render_about_dialog(q)


@on()
async def history(q:Q):
    await render_FCS_notification(q)
