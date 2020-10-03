import pathlib
import os
from dotenv import load_dotenv 

PROJECT_DIR = pathlib.Path(__file__).parents[2]
TEST_DIR = PROJECT_DIR / "tests"

env_path = PROJECT_DIR / '.env'
load_dotenv(dotenv_path=env_path)

DEBUG = os.getenv('DEBUG')