import configparser
import json
from pathlib import Path


from typing import Any, Dict, List, NamedTuple

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_qai.json"
)


def get_database_path(config_file: Path) -> Path:
    """Return the current path for the database"""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    """Create database"""
    try: 
        db_path.write_text("[]")
        return "SUCCESS"
    except OSError:
        return "DB Writing Error"


class DBResponse(NamedTuple):
    qai_list: List[Dict[str, Any]]
    error: int


class DatabaseHandler:
    """
    Database handler class
    """
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_qai(self) -> DBResponse:
        """
        Read qai from db
        :params self
        """
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), "SUCCESS")
                except json.JSONDecodeError:
                    return DBResponse([],"JSON Error")
        except OSError:
            return DBResponse([], "DB Read error")

    def write_qai(self, qai_list: List[Dict[str, Any]]) -> DBResponse:
        """
        Write daily qai to db
        :params qai list, self
        """
        try:
            with self._db_path.open("w") as db:
                print(qai_list)
                json.dump(qai_list, db, indent=4)
            return DBResponse(qai_list, "SUCCESS")
        except OSError:
            return DBResponse(qai_list, "DB WRITE ERROR")
            