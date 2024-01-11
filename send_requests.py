import copy

import requests

import data
import configuration


def create_order(body):
    updated_body = copy.copy(data.CREATE_ORDER_DATA)

    if body:
        updated_body.update(body)

    response = requests.post(
        url=configuration.STAND_URL + configuration.CREATE_ORDER_URL,
        json=updated_body
    )

    return response


def get_order_by_track_number(track_number):
    response = requests.get(
        url=configuration.STAND_URL + configuration.GET_ORDER_BY_TRACK_URL,
        params={
            't': track_number
        }
    )

    return response

