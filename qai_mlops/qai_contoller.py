import os
import json
import requests

from pathlib import Path

from typing import Any, Dict, List, NamedTuple
 
from database import DatabaseHandler
from dotenv import load_dotenv


load_dotenv()


class QaiController:

    def __init__(self, db_path: Path) -> None:
        self.token = os.getenv('AIR_QUALITY_TOKEN')
        self.base_url = os.getenv('BASE_URL')
        self._db_handler = DatabaseHandler(db_path)

    


if __name__ == '__main__':
    qai = QaiController('.')
    api_res = qai.get_feed("milano")
    print(api_res['data']['aqi'])
    print(api_res['data']['time']['s'])
    print(qai._db_handler._db_path)