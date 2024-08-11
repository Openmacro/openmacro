# openmacro
> [!NOTE]  
> Project is in its early stage of development.

openmacro is a multiplatform personal agent which allows LLMs to run code locally. Open Macro aims to act as a personal agent capable of completing and automating simple to complex tasks autonomously via self prompting.

You can chat with Open Macro through the official desktop application here. Or communicate through the terminal by running `macro`.

This provides a cli natural-language interface and toolset for you to:

+ Complete and automate simple to complex tasks.
+ Control a Chromium browser to perform tasks and research.
+ Control desktop applications through vision and pyautogui.
+ Manipulate files including photos, videos, PDFs, etc.

By default, if no api keys for models are provided, the following will be used powered by HuggingFace:
+ LLM: [Llama3.1-70B](https://huggingface.co/spaces/orionai/llama-3.1-70b-demo)
+ Code: [CodeQwen1.5-7B](https://huggingface.co/spaces/Qwen/CodeQwen1.5-7b-Chat-demo)
+ Vision: [Qwen-VL-Max](https://huggingface.co/spaces/Qwen/Qwen-VL-Max)

This project is heavily inspired by Open Interpreter. 

### Todo's 
- [x] AI Intepreter
- [x] CLI Interface
- [ ] API Keys Support
- [ ] Extensions Feature
- [ ] Web Search Capability
- [ ] Full Browser Control
- [ ] Chunk Streaming and Smart Stalling 
- [ ] Semantic File Search
- [ ] App Interface
...