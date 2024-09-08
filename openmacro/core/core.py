from ..core.utils.computer import Computer
from ..core.utils.llm import LLM, to_lmc, interpret_input
from ..core.utils.general import load_settings
from ..core.utils.extensions import Extensions
from pathlib import Path
import asyncio
import os

class Profile:
    """
    store apikeys here. this is temp since its a bad setup omg.
    """
    def __init__(self, config_file= None, keys: dict ={}):
        
        self.settings = load_settings(file=config_file)
        self.keys = keys
        if not keys:
            self.keys = self.settings["defaults"]
            
            
    def __str__(self):
        return f'Profile({self.keys})'

class Openmacro:
    """
    The core of all operations occurs here.
    Where the system breaks down requests from the user and executes them.
    """
    def __init__(
            self,
            messages: list | None = None,
            history_dir: Path | None = None,
            skills_dir: Path | None = None,
            prompts_dir: Path | None = None,
            extensions_dir: Path | None= None,
            verbose: bool = False,
            local: bool = False,
            computer = None,
            profile = None,
            dev = True,
            llm = None,
            tasks = False,
            breakers = ("the task is done.", "the conversation is done.")) -> None:
        
        # settings
        self.profile = Profile() if profile is None else profile
        self.settings = self.profile.settings
        self.dev = dev
        
                
        # memory + history
        self.prompts_dir = Path(Path(__file__).parent, "prompts") if prompts_dir is None else prompts_dir

        self.extensions = Extensions()
        self.computer = Computer(self.extensions) if computer is None else computer
        

        # experimental
        self.local = local

        # prompts
        self.prompts = {}
        prompts = os.listdir(self.prompts_dir)
        for filename in prompts:
            with open(Path(self.prompts_dir, filename), "r") as f:
                self.prompts[filename.split('.')[0]] = f.read().strip()
        
        self.prompts['initial'] = self.prompts['initial'].format(assistant=self.settings['assistant']['name'],
                                                                 personality=self.settings['assistant']['personality'],
                                                                 username=self.computer.user,
                                                                 os=self.computer.os)
        
        self.prompts['interface'] = self.prompts['initial'] + '\n' + self.prompts['interface']
        
        self.prompts['initial'] += "\n\n" + self.prompts['instructions'].format(supported=self.computer.supported,
                                                                                extensions=self.extensions.load_instructions())
        
        # utils
        self.llms = {
            "interface": None,
            "computer": None,
            "ltm": None
        }
        self.name = self.settings['assistant']['name']
        self.llm = LLM(self.profile, messages=messages, verbose=verbose, system=self.prompts['initial']) if llm is None else llm
        
        self.tasks = tasks

        # logging + debugging
        self.verbose = verbose
        
        # loop breakers
        self.breakers = breakers

        self.llm.messages = [] if messages is None else messages
        
        self.queue = []
        
        
    async def streaming_chat(self, 
                             message: str = None, 
                             remember=True,
                             timeout=16,
                             lmc=False):
    
        response, notebooks = "", {}
        for _ in range(timeout):
            async for chunk in self.llm.chat(message=message, 
                                             stream=True,
                                             remember=remember, 
                                             lmc=lmc):
                response += chunk
                yield chunk
                
            # because of this, it's only partially async
            # will fix in future versions
            lmc = False
            
            for chunk in interpret_input(response): 
                if chunk.get("type", None) == "code":
                    language, code = chunk.get("format"), chunk.get("content")
                    if language in notebooks:
                        notebooks[language] += "\n\n" + code
                    else:
                        notebooks[language] = code
                
                elif "let's run the code" in chunk.get("content").lower():
                    for language, code in notebooks.items():
                        output = self.computer.run(code, format=language, display=False)
                        message, lmc = to_lmc(output, role="computer", format="output"), True
                        if self.dev:
                            yield message
                    notebooks = {}
                    
            response = ""
            if not lmc or chunk.get("content", "").lower().endswith(self.breakers):
                return
    
        raise Warning("Openmacro has exceeded it's timeout stream of thoughts!")
    
    async def _gather(self, gen):
        return await "".join([chunk async for chunk in gen])

    def chat(self, 
             message: str | None = None, 
             stream: bool = False,
             remember: bool = True,
             lmc: bool = False,
             timeout=16):
        
        gen = self.streaming_chat(message, remember, timeout, lmc)
        if stream: return gen
        return asyncio.run(self._gather(self, gen))