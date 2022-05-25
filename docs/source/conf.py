# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EM3566 User Manual'
copyright = '2022, Boardcon Embedded Design'
author = 'Boardcon'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# Html logo in drawer.
# Fit in the drawer at the width of image is 240 px.

import sphinx_rtd_theme
html_use_index = True
html_show_sphinx = True

html_logo = 'image/boardcon-logo.png'

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
