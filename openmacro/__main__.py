import argparse
from .core import cli
import shutil
from .core.core import Openmacro, Profile
from .core.utils.general import ROOT_DIR
import asyncio
import os

from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Description of your script.")
    
    parser.add_argument('--default', action='store_true', help='Switch back to default settings.')
    parser.add_argument('--api_key', type=str, help='Set your API KEY for SambaNova API.')
    parser.add_argument('--save', action='store_true', help='Save current `config.toml` settings for future uses.')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode for debugging.')
    parser.add_argument('--config', type=str, help='Path to a `config.toml` file for custom settings.')

    args = parser.parse_args()
    
    kwargs = {'verbose': args.verbose}
    if args.default:
        return kwargs
    
    path = args.config if args.config else 'config.toml'
    root = Path(ROOT_DIR, 'config.toml')
    
    if args.api_key:
        with open(Path(ROOT_DIR, '.env'), 'w') as f:
            f.write(f'API_KEY="{args.api_key}"')
        os.environ['API_KEY'] = args.api_key
    
    if not Path(path).is_file():
        path = root
        
    if not root.is_file():
        root.touch()
            
    kwargs['profile'] = Profile(root)
    
    if args.save and args.config:
        shutil.copyfile(args.config, str(root))
    return kwargs


def main():
    args = parse_args()
    macro = Openmacro(**args)
    asyncio.run(cli.main(macro))

if __name__ == "__main__":
    main()
