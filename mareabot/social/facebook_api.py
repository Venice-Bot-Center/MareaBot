import facebook
from mareabot.config import FACEBOOK_PAGE as PAGE, FACEBOOK_TOKEN as TOKEN


def facebook_post_page(msg):
    return get_api().put_wall_post(msg)


def get_api():
    graph = facebook.GraphAPI(TOKEN)
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == PAGE:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph
