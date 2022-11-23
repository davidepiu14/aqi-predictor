import os
import json
import requests

from pathlib import Path

from typing import Any, Dict, List, NamedTuple
 
from database import DatabaseHandler
from dotenv import load_dotenv


load_dotenv()


class QaiController:

    def __init__(self) -> None:
        self.token = os.getenv('AIR_QUALITY_TOKEN')
        self.base_url = os.getenv('BASE_URL')
    
    def get_feed(self, city: str) -> str:
        """
        Get qai feed
        :params city
        :return string
        """
        res = requests.get(f"{self.base_url}{city}/?token={self.token}")
        match res['status']:
            case 'ok':
                feed = {
                    ''
                }
        return json.loads(res.text)
    

if __name__ == "__main__":
    qaic = QaiController()
    print(qaic.get_feed("roma"))
    

