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

[bodhilib](https://bodhilib.bodhisearch.com) is an open-source, python library, built using plugin-architecture, and provides simple and consistent interfaces to interact with various Language Models(LLMs) and its eco-system (Prompt Engineering, VectorDB, RAG, Semantic Search). 

## Why bodhilib?

1. Open Source

    **bodhilib** is completely open-source under the MIT licence. We feel we owe it to the previous generation of developers who have contributed so much in form of Open Source. This is our humble attempt to contribute in turn.


1. Plugin Architecture

    **bodhilib** is built on top of plugin architecture. The core library `bodhilib` only defines the core interfaces for interacting with LLMs eco-system. So if you just install `bodhilib`, you get a very light-weight and slim library that does nothing 😀.

    All the functionalities are provided by the plugin implementations. Even the bodhilib team developed plugins are published as a separate `bodhiext.*` packages.

    We hope to provide the best implementation for interacting with any of the components in LLM eco-system. But with plugin architecture, we have to compete with other plugin developers on the same level playing field in terms of functionality, performance and other advantages.

    To see a long list of benefits of plugin architecture, check out [Benefits of Plugin Architecture](architecture/Benefits_of_Plugin_Architecture).

    If you are planning to build your own plugin, check out the [Plugin Developer Guide](plugins/Plugin_Developer_Guide).

1. Pythonic, Uniform and Composable Inteface

    **bodhilib** provides a Uniform interface for interacting with various LLM components. This allows developer to focus on the task at hand rather than the specifics of the underlying API. It also offers companies to switch to other service providers without making big changes to their code bases.

    We have tried our best to keep the design of bodhilib interfaces simple, pythonic and composable. We are hugely inspired by the functional programming and design philosophy, and looked at Haskell and other strict functional languages to design the interface for bodhilib. With this, we hope you find using bodhilib easy and pleasant.

    To get an overview of the bodhilib components, check out the detailed article on [Models, Components, Interfaces and Composable Design](deep-dive/Components_and_Interface) here.

    To see the inspiration and ideas behind the interface design for bodhilib, check out the detailed article on [Composable Design](architecture/Composable_Design) here.


## Contributing

To contribute to bodhilib, check out [Contributing Guide](contributing/Contributing)

## Contact

Follow us on twitter [@BodhilibAI](https://twitter.com/BodhilibAI) for updates.
