# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_material

# -- Project information -----------------------------------------------------

project = 'Python dataframe interchange protocol'
copyright = '2021, Consortium for Python Data API Standards'
author = 'Consortium for Python Data API Standards'

# The full version, including alpha/beta/rc tags
release = '2021-DRAFT'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# MyST options
myst_heading_anchors = 3
myst_enable_extensions = ["colon_fence"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Material theme options (see theme.conf for more information) ------------
html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Python dataframe interchange protocol',

    # Set you GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    #'base_url': 'https://project.github.io/project',

    # Set the color and the accent color (see
    # https://material.io/design/color/the-color-system.html)
    'color_primary': 'indigo',
    'color_accent': 'green',

    # Set the repo location to get a badge with stats
    #'repo_url': 'https://github.com/project/project/',
    #'repo_name': 'Project',

    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "repo_type": "github",
    "touch_icon": "images/apple-icon-152x152.png",
    "theme_color": "#2196f3",
    "master_doc": False,

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,

    "nav_links": [
        {"href": "index", "internal": True, "title": "Dataframe interchange protcol"},
        {
            "href": "https://data-apis.org",
            "internal": False,
            "title": "Consortium for Python Data API Standards",
        },
    ],
    "heroes": {
        "index": "A protocol for zero-copy data interchange between Python dataframe libraries",
        #"customization": "Configuration options to personalize your site.",
    },

    #"version_dropdown": True,
    #"version_json": "_static/versions.json",
    "table_classes": ["plain"],
}


todo_include_todos = True
#html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        "",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", ""),
    "dudir": ("http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s", ""),
}
