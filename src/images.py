from h2o_wave import Q, ui
from .utils import center, gap

async def render_images(q:Q):
    if not q.client.image_icon:
        q.client.image_icon = (await q.site.upload(['static/image_icon.png']))[0]

    
    q.page['image'] = ui.form_card('image', items=[
        *gap(12),
        # ui.message_bar(text='Please enter a prompt to generate images'),
        *gap(5),
        *center([ui.image('', path=q.client.image_icon, width='30%')]),
        *center([ui.text('Your images will appear here')]),
    ])
