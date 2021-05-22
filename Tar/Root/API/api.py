import json
import os
import re

from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource

from Config.config import URL_PATH, TARSIUM_INPUT_PATH


app = Flask(__name__)
api = Api(app)


def update_json():
    displayed_data = dict()
    try:
        displayed_data['dirname'] = TARSIUM_INPUT_PATH
        displayed_data['timestamp'] = str(datetime.now())
        displayed_data['file_count'] = len(os.listdir(TARSIUM_INPUT_PATH))
        displayed_data['avg_format_files'] = len([f for f in os.listdir(TARSIUM_INPUT_PATH) if re.search('.json', f)]) / \
                                             displayed_data['file_count']
        return displayed_data
    except Exception as error:
        displayed_data['exception'] = str(error)
        return displayed_data


class TarsiumApi(Resource):

    def get(self):
        updated_json = update_json()
        return updated_json


def start_app(logger):
    logger.info('Started running api...')
    try:
        app.run()
    except Exception as error:
        logger.error('An error occurred while running tarsium api...\r\n\t'
                     f'Exception: {error}')


api.add_resource(TarsiumApi, URL_PATH)
