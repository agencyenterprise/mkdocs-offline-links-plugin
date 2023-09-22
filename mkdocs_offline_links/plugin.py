from mkdocs.config import base, config_options
from mkdocs.plugins import BasePlugin


class OfflineLinksConfig(base.Config):
    enabled = config_options.Type(bool, default=True)


class OfflineLinksPlugin(BasePlugin[OfflineLinksConfig]):
    """A MkDocs plugin to make links to other pages in the site work offline.

    Works by changing all directory links to their corresponding index.html.
    """

    def on_files(self, files, config):
        if not self.config.enabled:
            return files

        for file in files.documentation_pages():
            file.url = file.dest_uri
        return files
