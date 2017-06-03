from .default import list_view
from .default import detail_view
from .default import create_view
from .default import update_view


def includeme(config):
    config.add_view(list_view, route_name="list")
    config.add_view(detail_view, route_name="detail")
    config.add_view(create_view, route_name="new")
    config.add_view(update_view, route_name="edit")
