from h2o_wave import Q, app, main
from .initializers import init_client
from .handlers import render_page
from .utils import error

@app('/')
async def serve(q:Q):
    try:
        # init client and user if not already done so
        if not q.client.initialized:
            await init_client(q)
            q.client.initialized = True

        # render main page
        await render_page(q)

    except Exception as err:
        await error(q, str(err))

    # save the page
    await q.page.save()
