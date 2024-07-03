from .utils.engines import Search
from .utils.computer import Computer
from .utils.model import Model
from pathlib import Path
import asyncio
import os

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
            verbose: bool = False,
            local: bool = False,
            computer = None,
            browser = None,
            model = None,
            tasks = False) -> None:
        
        # utils
        self.browser = Search() if browser is None else browser
        self.computer = Computer() if computer is None else computer
        self.model = Model(messages=messages) if model is None else model

        self.tasks = tasks

        # logging + debugging
        self.verbose = verbose
        
        # memory + history
        self.history_dir = Path(Path(__file__).parent, "memory", "history") if history_dir is None else history_dir
        self.skills_dir = Path(Path(__file__).parent, "memory", "skills") if skills_dir is None else skills_dir
        self.prompts_dir = Path(Path(__file__).parent, "prompts") if prompts_dir is None else prompts_dir
        
        self.model.messages = [] if messages is None else messages

        # experimental
        self.local = local

        # prompts
        self.prompts = {}
        prompts = os.listdir(self.prompts_dir)
        for filename in prompts:
            with open(Path(self.prompts_dir, filename), "r") as f:
                self.prompts[filename.split('.')[0]] = f.read().strip()

    def render_prompt(self):
        pass
        

    def classify(self, message):
        """
        Classify whether the message is either a question, task or routine.
        """
        response = self.model.raw_chat(message, 
                                       remember=False, 
                                       system=self.prompts["classify"])
        return response

    def chat(self, 
            message: str = None, 
            display: bool = True, 
            stream: bool = False):
    
        mode = self.classify(message)
        mode = mode.lower()
        if self.verbose:
            print('Determined conversation type:', mode)
    
        if mode == "chat":
            self.run_chat(message, display)
        elif mode == "task":
            self.run_task(message, display)
        elif mode == "routine":
            self.run_routine(message, display)
        else:
            raise ValueError("Invalid classification of message.")


    def run_chat(self, message, display):
        response = self.model.chat(message)

        if display:
            print(response)
        return

    def run_task(self):
        # doing task for the first time, load `initial_task.txt`
        if not self.tasks:
            pass
        pass

    def run_routine(self):
        pass
