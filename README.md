# export
This plugin is designed to bookend the workflow by providing a place where metadata and files for an article can be exported from Janeway. An example of a workflow that utilses the plugin would be:

*Submission -> Peer Review -> Export -> Loaded into a seperate production system*

## Installation
To install this plugin:
1. Clone it inside `janeway/src/plugins`.
2. From the main Janeway `src` directory run `python3 manage.py install_plugins export.
3. Reload your web server.

## Supported Formats
Currently the plugin supports exporting a zip file with either:
- HTML Metadata File
- CSV Metadata File

Alongside the metadata file all files that are linkes to the article will be added to the zip.
