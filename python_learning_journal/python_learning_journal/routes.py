def includeme(config):
    config.add_static_view('static', 'python_learning_journal:static', cache_max_age=3600)
    config.add_route('list', '/')
    config.add_route('detail', '/entry/{id:\d+}')
    config.add_route('new', '/entry/new')
    config.add_route('edit', '/entry/edit/{id:\d+}')
