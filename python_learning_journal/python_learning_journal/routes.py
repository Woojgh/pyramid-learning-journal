def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new-entry')
    config.add_route('update_view', '/journal/{id:\d+}/edit-entry')
    config.add_route('login_view', '/login')
    config.add_route('logout_view', '/logout')

    config.add_route('api_journal_list', '/api/v1/journals')