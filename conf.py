from pathlib import Path

import toml

PROJ_DIR = Path(__file__).parent.absolute()
with open(PROJ_DIR / "pyproject.toml") as f:
    pyproj_file = toml.load(f)

project = "bodhilib-guide"
copyright = "2023, Amir Nagri"
author = "Amir Nagri"
release = pyproj_file["tool"]["poetry"]["version"]

extensions = [
    "myst_parser",
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

myst_enable_extensions = [
    "html_admonition",
    "colon_fence",
]

html_theme_options = {
    "repository_url": "https://github.com/BodhiSearch/bodhilib-guide",
    "show_navbar_depth": 2,
    "use_repository_button": True,
    "home_page_in_toc": True,
    "footer_start": ["footer.html"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/BodhiSearch/bodhilib",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/bodhilib/",
            "icon": "https://img.shields.io/pypi/dw/bodhilib",
            "type": "url",
        },
    ],
    "use_download_button": True,
    "use_fullscreen_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
}
html_logo = "placeholder-logo.svg"
nbsphinx_execute = "auto"
