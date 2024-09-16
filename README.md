<div align="center">
  <a href="https://pypi.org/project/openmacro/">
    <img src="https://raw.githubusercontent.com/Openmacro/openmacro/46bb3481766cb66983cb191db731c41f5f69d18d/docs/images/openmacro-title.svg" width="480" height="auto" alt="Openmacro"/>
  </a>
</div>
<div align="center">
<a href="https://github.com/Openmacro/openmacro/blob/main/LICENSE"><img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white&style=flat" alt="License"/></a>
  <a href="https://github.com/Openmacro/openmacro/graphs/commit-activity"><img src="https://img.shields.io/github/commit-activity/m/Openmacro/openmacro" alt="Commit Activity"/></a>
  <a href="https://github.com/Openmacro/openmacro/commits/"><img src="https://img.shields.io/github/last-commit/Openmacro/openmacro" alt="Last Commit"/></a>
  <a href="https://pypi.org/project/openmacro"><img src="https://img.shields.io/pypi/dm/openmacro" alt="Downloads"/></a>
  <a href="https://github.com/Openmacro/openmacro/stargazers"><img src="https://img.shields.io/github/stars/Openmacro/openmacro" alt="Stars"/></a>

</div>

##

<div align="center">
  <a href="https://pypi.org/project/openmacro/">
    <img src="https://raw.githubusercontent.com/Openmacro/openmacro/main/docs/images/demo.png" height="auto" alt="Openmacro"/>
  </a>
</div>

<br>

> Project is in its early stage of development.

openmacro is a multimodal personal agent that allows LLMs to run code locally. openmacro aims to act as a personal agent capable of completing and automating simple to complex tasks autonomously via self prompting.

This provides a cli natural-language interface for you to:

+ Complete and automate simple to complex tasks.
+ Analyse and plot data.
+ Browse the web for the latest information.
+ Manipulate files including photos, videos, PDFs, etc.

At the moment, openmacro only supports API keys for models powered by SambaNova. Why? Because it’s free, fast, and reliable, which makes it ideal for testing as the project grows! Support for other hosts such as OpenAI and Anthropic is planned to be added in future versions.

This project is heavily inspired by [`Open Interpreter`](https://github.com/OpenInterpreter/open-interpreter) ❤️

### Quick Start
To get started with openmacro, get a free API key by creating an account at [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/). 

Next, install and start openmacro by running:
```shell
pip install openmacro
macro --api_key "YOUR_API_KEY"
```
> Not working? Raise an issue [here](https://github.com/amooo-ooo/openmacro/issues/new) or try this out instead:
```shell
py -m pip install openmacro
py -m openmacro --api_key "YOUR_API_KEY"
```
> Note: You only need to pass `--api_key` once! Next time simply call `macro` or `py -m openmacro`.

### Personalisation
Openmacro supports cli args and customised settings! You can view arg options by running:
```shell
macro --help
```
To append your own personalised settings and save it for the future, run:
```shell
macro --config "path\to\config.toml" --save
```

What your personalised `config.toml` might look like:
```toml
[assistant]
name="Basil"
personality="You have a kind, deterministic and professional attitude towards your work and respond in a formal, yet casual manner."
```

### Todo's 
- [x] AI Intepreter
- [X] Web Search Capability
- [X] Async Chunk Streaming
- [X] API Keys Support
- [ ] `WIP` Cost Efficient Long Term Memory & Context Manager
- [ ] `WIP` Extensions API (Openmacro Package Index)
- [ ] Semantic File Search
- [ ] Optional Telemetry
- [ ] Desktop, Android & IOS App Interface

### Currently Working On
Currently, focusing on a refined system for Extensions, so anyone can build extensions for openmacro.

- Working on `browser` which is the official openmacro browser extension powered by Playwright, Bs4 and Markdownify.

- Working on `ompi` which is the Openmacro Package Index. Similar to Python's `pypi`, users can install third-party extensions to integrate with their openmacro assistant.

- Cost efficient long term memory and conversational context managers through vector databases. Most likely powered by [`ChromaDB`](https://github.com/chroma-core/chroma).

### Contact
You can contact me at [amor.budiyanto@gmail.com](mailto:amor.budiyanto@gmail.com)
