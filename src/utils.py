from h2o_wave import Q, ui


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
