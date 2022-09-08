import os
from h2o_wave import Q, ui
from .utils import center, gap


async def render_samples(q:Q):
    images = q.client.images
    if not images:
        images = q.client.images = await get_images(q)
    
    num = int(q.args.num or 0)
    widgets=[
        # gap
        *gap(5),
        ui.inline(justify='center', items=[
            ui.label(f'Image {num+1} of {len(images)}')
        ]),
        *gap(1),
        # image
        *center([
            ui.text(f'<img src="{images[num]}" width="512" height="512">')
        ]),
        *gap(1),
        ui.inline(justify='center', items=[
            ui.button(
                name='num',
                value=f'{num-1}',
                #label='Previous',
                disabled=(num == 0),
                primary=True,
                icon='DoubleChevronLeft8'
            ),
            *gap(3),
            ui.button(
                name='download',
                #primary=True,
                icon='OpenInNewTab',
                label='Open',
                path=images[int(q.args.button or 1)-1],
            ),
            *gap(3),
            ui.button(
                name='num',
                value=f'{num+1}',
                #label='Next',
                disabled=(num == len(images)-1),
                primary=True,
                icon='DoubleChevronRight8'
            )
        ])
    ]

    q.page['image'] = ui.form_card('image', items=widgets)




async def get_images(q:Q):
    files = os.listdir('output/samples')
    filepaths = [f'output/samples/{file}' for file in files]
    images = await q.site.upload(filepaths)
    return images
