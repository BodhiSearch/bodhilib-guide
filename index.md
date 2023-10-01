---
title: bodhilib guide
---

```{toctree}
:hidden:
:maxdepth: 2

installation/index
getting-started/index
deep-dive/index
```

# bodhilib

[bodhilib](https://bodhilib-guide.readthedocs.io/) is an open-source, python library, built using plugin-architecture, and provides simple and uniform interfaces to interact with various Language Models(LLMs) and the eco-system (Prompt Engineering, VectorDB, RAG, Semantic Search).

## Why bodhilib?

1. **Open Source**

   **bodhilib** is open-source under the MIT licence. We are inspired by the previous generation of developers and their amazing contributions to Open Source. This is our way of giving back.

1. **Plugin Architecture**

   **bodhilib** uses the python plugin architecture. The core library bodhilib defines the primary interfaces for interacting with the LLM ecosystem, keeping it lightweight and slim. So if you just install `bodhilib`, you get a very light-weight and slim library that does nothing 😀.

   All functionalities are provided through plugin implementations. Even the plugins developed by the bodhilib team are published as a separate `bodhiext.*` and need to be installed explicitly.

   This architecture levels the playing field, allowing us (bodhilib team) to compete with other plugin developers in terms of functionality, performance, and other advantages.

1. **Pythonic, Uniform and Composable Interface**

   **bodhilib** provides a uniform interface for interacting with various LLM components. This allows developer to focus on the task at hand rather than the specifics of the underlying API. This also enables companies to switch service providers with minimal code adjustments.

   We have strived to keep the design of bodhilib’s interfaces simple, Pythonic, and composable. Inspired by functional programming and design philosophy, we’ve looked to languages like Haskell to design bodhilib’s interface. We hope you find using bodhilib to be easy and enjoyable.

   For an overview of bodhilib components, see [Getting Started](getting-started/index.md) guide.

## Contributing

If you’re interested in contributing to bodhilib, please see our [Contributing Guide](contributing/index).

## Contact

Follow us on twitter [@BodhilibAI](https://twitter.com/BodhilibAI) for updates.
