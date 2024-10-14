from openmacro.profile import Profile
from openmacro.utils import USERNAME, ROOT_DIR
from openmacro.extensions import BrowserKwargs
from pathlib import Path

profile: Profile = Profile(
    user = { 
        "name": USERNAME, 
        "version": "1.0.0"
    },
    assistant = {
        "name": "Basil",
        "personality": "You have a kind, deterministic and professional attitude towards your work and respond in a concise, short, formal, yet casual manner.",
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
        "prompts": Path(ROOT_DIR, "core", "prompts"),
    },
    config = {
        "telemetry": False,
        "ephemeral": False,
        "verbose": True,
        "local": False,
        "dev": False,
        "conversational": True,
    },
    extensions = {
        "Browser": BrowserKwargs(engine="google")
    },
    tts = {
        "enabled": False,
        "engine": "SystemEngine"
    }
)