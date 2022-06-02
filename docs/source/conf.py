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

# -- Options for HTML output

html_theme = "jekyll-theme-modernist"



