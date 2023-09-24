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
    "nbsphinx",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
