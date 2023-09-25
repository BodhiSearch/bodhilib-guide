---
title: Installation
---

# Installation

```{toctree}
:hidden:

Marketplace
```

`bodhilib` and `bodhiext.*` are available on pypi as python packages. Here are the step-by-step instructions for installing bodhilib and bodhiext plugin packages and getting started.

## Requirements
The bodhilib library requires Python 3.8 or above. You can download the latest version of Python [here](https://www.python.org/downloads/).

## Installing bodhilib

bodhilib can be installed using pip, a python package installer. To install, just run the following command in your terminal:

```shell
pip install bodhilib
```

This command will download the latest stable version of bodhilib and install it on your system.

We suggest you use **poetry** for managing your python project and its dependencies. Since the plugins are loaded at runtime dynamically from `sys.path`, sharing the dependencies between project can cause unforseen issues. To install using poetry, run the following command in your terminal:
```shell
poetry add bodhilib
```

## Installing bodhiext.all
`bodhiext.*` are family of plugin packages developed by the bodhilib team, and provides independent implementations for most frequently used and most popular components when building a GenerativeAI/LLM based apps. You can browse and search for the available plugin packages in the [Marketplace](Marketplace).

If you are exploring, and need not be bothered by installing packages as you need them, you can install all the packages offered by `bodhiext.*` by installing `bodhiext.all` package. To install `bodhiext.all` package, run the following command in your terminal:

```shell
pip install bodhiext.all
```

```{admonition} Caution
:class: warning

`bodhiext.all` installs all the plugin packages developed by bodhilib team. These packages and its dependencies might use a lot of your bandwidth and disk space.
```

## Installing individual bodhiext package
If you are installing dependencies for your production app, it is better to install the specific plugin package required by your app. Once you have finalized on the plugin you need, you can install it independently, along with its dependencies. For e.g. if you are using `OpenAI` as your LLM service, you can individually install the plugin package as -

```shell
pip install bodhiext.openai
```

or if you are using poetry, add it to your dependency as -

```shell
poetry add bodhiext.openai
```

## Verifying the Installation
Once you've installed the packages, you can verify your installation by running the following command in your Python environment:

```python
import bodhilib
```

You can verify the plugin package is properly installed by trying to import it. For e.g. if you have installed `bodhiext.openai`, you can verify the installation by running the following in your python environment:

```python
import bodhiext.openai
```

If commands execute without an error, congratulations! You've successfully installed bodhilib along with its plugin package.
