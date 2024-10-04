<div align="center">
  <a href="https://pypi.org/project/openmacro/">
    <img src="https://raw.githubusercontent.com/openmacro/openmacro/46bb3481766cb66983cb191db731c41f5f69d18d/docs/images/openmacro-title.svg" width="480" height="auto" alt="openmacro"/>
  </a>
</div>
<div align="center">
<a href="https://github.com/openmacro/openmacro/blob/main/LICENSE"><img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white&style=flat" alt="License"/></a>
  <a href="https://github.com/openmacro/openmacro/graphs/commit-activity"><img src="https://img.shields.io/github/commit-activity/m/openmacro/openmacro" alt="Commit Activity"/></a>
  <a href="https://github.com/openmacro/openmacro/commits/"><img src="https://img.shields.io/github/last-commit/openmacro/openmacro" alt="Last Commit"/></a>
  <a href="https://pypi.org/project/openmacro"><img src="https://img.shields.io/pypi/dm/openmacro" alt="Downloads"/></a>
  <a href="https://github.com/openmacro/openmacro/stargazers"><img src="https://img.shields.io/github/stars/openmacro/openmacro" alt="Stars"/></a>

</div>

##

<div align="center">
  <a href="https://pypi.org/project/openmacro/">
    <img src="https://raw.githubusercontent.com/openmacro/openmacro/main/docs/images/demo.png" height="auto" alt="openmacro"/>
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

## Quick Start
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

## Profiles
openmacro supports cli args and customised settings! You can view arg options by running:
```shell
macro --help
```
To add your own personalised settings and save it for the future, run:
```shell
macro --profile "path\to\profile.py" --save
```
Profiles are `python` files to allow dynamic integration and type safety (with TypedDict)! Better docs for Profiles will be added in upcoming versions.

What your `profile.py` might look like:
```python
# imports
from openmacro.profile import Profile
from openmacro.extensions import Browser, Email
from openmacro.utils import config

# pass kwargs to extensions
Email = config(Email, mail="amor.budiyanto@gmail.com", password="password")

# profile setup
profile: Profile = Profile(
    user = { 
        "name": "Amor, 
        "version": "1.0.0"
    },
    assistant = {
        "name": "Basil",
        "personality": "You have a kind, deterministic and professional attitude towards your work and respond in a formal, yet casual manner.",
        "messages": [],
        "breakers": ["the task is done.", 
                     "the conversation is done."]
    },
    safeguards = { 
        "timeout": 16, 
        "auto_run": True, 
        "auto_install": True 
    },
    paths = { 
        "prompts": "core/prompts",
    },
    extensions = {
        "Browser": Browser,
        "Email": Email
    },
    config = {
        "verbose": False,
        "dev": False
    },
    # you can specify custom paths to languages or add custom languages for openmacro to run!
    languages = {
      "python": ["C:\Windows\py.EXE", "-c"],
      "rust": ["cargo", "script", "-e"] # not supported by default, but can be added!
    }
)
```

If you want to build your own app with openmacro, you can simply extend your profile to use it:
```python
...

async def main():
    from openmacro.core import Openmacro

    macro = Openmacro(profile)
    macro.llm.messages = []

    async for chunk in macro.chat("Plot an exponential graph for me!", stream=True):
        print(chunk, end="")

import asyncio
asyncio.run(main)
```

You can also switch between profiles by running:
```shell
macro --switch "amor"
```

Profiles also support versions for modularity (uses the latest version by default).
```shell
macro --switch "amor:1.0.0"
```
> Note: All profiles are isolated. LTM from different profiles and versions are not shared.

To view all available profiles run:
```shell
macro --profiles
```

## Extensions
openmacro supports custom RAG extensions for modularity and theoretically infinite capabilities! By default, the `browser` and `email` extensions are installed.

### Writing Extensions
Write extensions using the template:
```python
class ExtensionName:
    def __init__(self):
        ...
      
    @staticmethod
    def load_instructions() -> str:
        return "<instructions>"
        
```
You can find examples [here](https://github.com/Openmacro/openmacro/tree/main/openmacro/extensions).

Upload your code to `pypi` for public redistribution using `twine` and `poetry`.
To add it to `openmacro.extensions` for profiles and `openmacro.apps` for the AI to use, run:

```shell
omi install <module_name>
```
or 
```shell
pip install <module_name>
omi add <module_name> 
```

You can test your extensions by installing it locally:
```shell
omi install .
```

## Todo's 
- [x] AI Interpreter
- [X] Web Search Capability
- [X] Async Chunk Streaming
- [X] API Keys Support
- [X] Profiles Support
- [X] Extensions API
- [ ] `WIP` Cost Efficient Long Term Memory & Context Manager
- [ ] Semantic File Search
- [ ] Optional Telemetry
- [ ] Desktop, Android & IOS App Interface

## Currently Working On
- Cost efficient long term memory and conversational context managers through vector databases. Most likely powered by [`ChromaDB`](https://github.com/chroma-core/chroma).

- Hooks API and Live Code Output Streaming

## Contact
You can contact me at [amor.budiyanto@gmail.com](mailto:amor.budiyanto@gmail.com)

## Contributions
This is my first major open-source project, so things might go wrong, and there is always room for improvement. You can contribute by raising issues, helping with documentation, adding comments, suggesting features or ideas, etc. Your help is greatly appreciated!

## Support
You can support this project by writing custom extensions for openmacro! openmacro aims to be community-powered, as its limitations are based on its capabilities. More extensions mean better chances of completing complex tasks. I will create an official verified list of openmacro extensions sometime in the future!