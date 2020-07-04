from utils import plugins

PLUGIN_NAME = 'Export Plugin'
DISPLAY_NAME = 'Export'
DESCRIPTION = 'A workflow element to export data.'
AUTHOR = 'Andy Byers'
VERSION = '0.1'
SHORT_NAME = 'export'
MANAGER_URL = 'export_manager'
JANEWAY_VERSION = "1.3.8"
IS_WORKFLOW_PLUGIN = True
JUMP_URL = 'export_article'
HANDSHAKE_URL = 'export_articles'
ARTICLE_PK_IN_HANDSHAKE_URL = True
STAGE = 'export_plugin'
KANBAN_CARD = 'export/elements/card.html'
DASHBOARD_TEMPLATE = 'export/elements/dashboard.html'


class ExportPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME
    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = JANEWAY_VERSION
    is_workflow_plugin = IS_WORKFLOW_PLUGIN
    stage = STAGE
    handshake_url = HANDSHAKE_URL
    article_pk_in_handshake_url = ARTICLE_PK_IN_HANDSHAKE_URL


export_plugin = ExportPlugin()


def install():
    export_plugin.install()


def hook_registry():
    export_plugin.hook_registry()


def register_for_events():
    pass
