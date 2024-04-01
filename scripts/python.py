header = """
    __                __                           __  __                       
   / /_  __  ______  / /____  _____   ____ _____ _/ /_/ /_  ___  ________  _____
  / __ \/ / / / __ \/ __/ _ \/ ___/  / __ `/ __ `/ __/ __ \/ _ \/ ___/ _ \/ ___/
 / / / / /_/ / / / / /_/  __/ /     / /_/ / /_/ / /_/ / / /  __/ /  /  __/ /    
/_/ /_/\__,_/_/ /_/\__/\___/_/      \__, /\__,_/\__/_/ /_/\___/_/   \___/_/     
                                   /____/                                     
"""

# HELPERS ---------------------------------------------------------------------

from pathlib import Path

path_to_import = lambda p: p[p.find("app") :].split(".py")[0].replace("/", ".")

print("=====> IMPORTING MODELS.....")
model_paths = Path(__file__).parent.parent.glob("app/api/v1/**/models.py")

# Sort to make sure we don't have random circular imports
model_paths = list(model_paths)
model_paths.sort()

for path in model_paths:
    module_name = path_to_import(str(path))
    import_statement = f"from {module_name} import *"
    print(import_statement)
    exec(import_statement)
print()

# ENV WARNINGS ----------------------------------------------------------------

import os
import sys

env = os.environ.get("ENV", "")
if env.upper() not in ["DEV", "DEVELOPMENT", ""]:
    sys.ps1 = f"{env} >>> "
    sys.ps2 = f"{env} ... "

if env.upper() not in ["DEV", "DEVELOPMENT", ""]:
    env_banner_line = " ".join([env] * 10)
    env_banner = "\n".join([env_banner_line] * 5)
    print(env_banner)
    print()

# DB SESSION ------------------------------------------------------------------

from app.database import db

session = next(db())

print("======> ACCESS DATABASE WITH `session`")

# -----------------------------------------------------------------------------

print(header)


import logging

from fastapi.logger import logger

logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
