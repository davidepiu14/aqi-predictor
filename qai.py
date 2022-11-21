import os
import json
import requests

from dotenv import load_dotenv


load_dotenv()


class QaiWrapper:

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
        return json.loads(res.text)


if __name__ == '__main__':
    qai = QaiWrapper()
    api_res = qai.get_feed("milano")
    print(api_res['data']['aqi'])
    print(api_res['data']['time']['s'])