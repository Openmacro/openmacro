import io
import os
import sys
import platform
from rich.console import Console
from rich.syntax import Syntax
from ..utils.general import lazy_import

class Computer:
    def __init__(self) -> None:
        self.platform = platform.uname()
        self.user = os.getlogin()
        self.os = f"{self.platform.system} {self.platform.version}"
        self.supported = ["python", "js"]
        self.globals = {"lazy_import": lazy_import}
        
        if self.platform.system == "Windows":
            self.supported += ["cmd", "powershell"]
        elif self.platform.system == "Darwin":
            self.supported += ["applescript"]
        elif self.platform.system == "Linux":
            self.supported += ["bash"]
            
    def md(self, code, format='python', console=Console()):
        console.print(Syntax(code, format, theme="github-dark", line_numbers=True))
        print()
        

    def run(self, code, format='python'):
        console = Console()
        if format == 'pseudocode':
            console.print(f'[bold #4a4e54]{chr(0x1F785)} Task plan in `{format}`...[/bold #4a4e54]')
            self.md(code, format, console)
            return None

        console.print(f'[bold #4a4e54]{chr(0x1F785)} Running `{format}`...[/bold #4a4e54]')
        self.md(code, format, console)
        
        output = ""
        
        if format == 'python':
            output = self.run_python(code)
        elif (format == 'bash') or (format == 'cmd') or (format == 'shell'):
            output = self.run_shell(code)
        elif format == 'applescript' and platform.system() == 'Darwin':
            output = self.run_applescript(code)
        elif format == 'js':
            output = self.run_js(code)
        elif format == 'powershell':
            output = self.run_powershell(code)
        else:
            output = f"Openmacro does not support the format: {format}"
        
        return output if output else "The following code did not generate any console text output, but may generate other output."
 

    def run_python(self, code):
        output = io.StringIO()
        stdout = sys.stdout
        sys.stdout = output
        try:
            exec(code, self.globals)
        except Exception as e:
            output.write(f"An error occurred: {e}")
        finally:
            sys.stdout = stdout
        return output.getvalue()

    def run_shell(self, code):
        try:
            result = os.system(code)
            return f"Command executed with exit code: {result}"
        except Exception as e:
            return f"An error occurred: {e}"

    def run_applescript(self, code):
        try:
            result = os.system(f'osascript -e "{code}"')
            return f"Command executed with exit code: {result}"
        except Exception as e:
            return f"An error occurred: {e}"

    def run_js(self, code):
        try:
            result = os.system(f'node -e "{code}"')
            return f"Command executed with exit code: {result}"
        except Exception as e:
            return f"An error occurred: {e}"
        
    def run_powershell(self, code):
        try:
            result = os.system(f'powershell -Command "{code}"')
            return f"Command executed with exit code: {result}"
        except Exception as e:
            return f"An error occurred: {e}"
