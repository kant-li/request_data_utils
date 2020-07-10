"""
utils to handle request data
"""

from typing import Dict
import json
from flask import request


class RequestData:
    def __init__(self, data: Dict = None):
        if not data:
            data = {}
        self.data = data

    def get(self, key: str, default: str = "") -> (str, bool):
        """get string from data"""
        try:
            return str(self.data.get(key, default)), True
        except ValueError:
            return default, False

    def get_float(self, key: str, default: float = 0) -> (float, bool):
        """get float from data"""
        try:
            return float(self.data.get(key, default)), True
        except ValueError:
            return default, False

    def get_int(self, key: str, default: int = 0) -> (int, bool):
        """get int from data"""
        try:
            return int(float(self.data.get(key, default))), True
        except ValueError:
            return default, False

    def get_json(self, key: str):
        """get json object from data"""
        value = self.data.get(key, "")
        if isinstance(value, (dict, list)):
            return value, True
        try:
            return json.loads(value), True
        except json.JSONDecodeError:
            return {}, False


def get_request_data() -> RequestData:
    """get request data"""
    if request.method == "GET":
        data = request.args
    else:
        data = request.get_json()
        if data is None:
            data = request.form.to_dict(flat=True)

    return RequestData(data)
