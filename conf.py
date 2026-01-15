# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'FreeTaxUSA 2025 Tax Filing Guide'
copyright = '2025, Independent Help Guide'
author = 'FreeTaxUSA Help Center (Unofficial)'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = []

# Allow raw HTML in reStructuredText files
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (recommended for Read the Docs)
# html_theme = 'sphinx_rtd_theme'

# Page titles
html_title = "How to File Taxes with FreeTaxUSA in 2025 – Complete Guide"
html_short_title = "FreeTaxUSA 2025 Guide"

# Favicon (place file in _static or root directory)
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML (needed for CTA buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (optional)
# html_static_path = ['_static']
