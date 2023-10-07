---
title: Installation
---

# Installation

[bodhilib](https://pypi.org/project/bodhilib/) and [bodhiext.*](https://pypi.org/project/bodhiext.all/) are available on PyPI as Python packages. Below are the step-by-step instructions for installing bodhilib and bodhiext plugin packages to get you started.

## Requirements

The `bodhilib` library requires Python 3.8 or above. You can download the latest version of Python [here](https://www.python.org/downloads/).

## Installing bodhilib

`bodhilib` can be installed using pip, a Python package installer. To install, execute the following command in your terminal:

```shell
pip install bodhilib
```

This command will download the latest stable version of bodhilib and install it on your system.

We recommend using [poetry](https://python-poetry.org/) for managing your Python projects and their dependencies. Since the plugins are loaded at runtime dynamically from `sys.path`, sharing dependencies between projects can cause unforeseen issues. Also, bodhilib checks all the installed libraries when discovering plugins at boot time. Having a large number of packages installed might cause longer boot time.

To install using poetry, execute the following command in your terminal:

```shell
poetry add bodhilib
```

## Installing bodhiext.all

The `bodhiext.*` packages are a family of plugin packages developed by the bodhilib team. They provide independent implementations for the most frequently used and most popular components when building Generative AI/LLM-based apps. We are working on building a Marketplace for plugins, where you can browse and discover the plugins for your use-case.

If you are exploring and prefer not to be bothered by installing packages as you need them, you can install all the packages offered by `bodhiext.*` by installing the `bodhiext.all` package. To do this, run the following command in your terminal:

```shell
pip install bodhiext.all
```

```{admonition} Caution
:class: warning

Installing `bodhiext.all` will download all the plugin packages developed by the `bodhilib` team. Be aware that these packages and their dependencies might consume a significant amount of your bandwidth and disk space.
```

## Installing individual bodhiext package
For production apps, it is advisable to install only the specific plugin packages that your app requires. Once you have decided on the plugin you need, you can install it independently, along with its dependencies. For example, if you are using `OpenAI` as your LLM service, you can install the plugin package individually as follows:


```shell
pip install bodhiext.openai
```

or if you are using poetry, add it to your dependency with -

```shell
poetry add bodhiext.openai
```

## Verifying the Installation
Once you've installed the packages, you can verify your installation by running the following command in your Python environment:

```python
import bodhilib
```

You can verify that the plugin package is properly installed by attempting to import it. For example, if you have installed `bodhiext.openai`, you can verify the installation by executing the following in your Python environment:

```python
import bodhiext.openai
```

If the commands execute without an error, congratulations! You've successfully installed bodhilib along with its plugin package.
