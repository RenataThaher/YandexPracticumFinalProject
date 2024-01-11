import data
import send_requests


def positive_assert_create_order(
    firstName=None,
    lastName=None,
    address=None,
    metroStation=None,
    phone=None,
    rentTime=None,
    deliveryDate=None,
    comment=None,
    color=None
):
    body = {}
    if firstName:
        body['firstName'] = firstName
    if lastName:
        body['lastName'] = lastName
    if address:
        body['address'] = address
    if metroStation:
        body['metroStation'] = metroStation
    if phone:
        body['phone'] = phone
    if rentTime:
        body['rentTime'] = rentTime
    if deliveryDate:
        body['deliveryDate'] = deliveryDate
    if comment:
        body['comment'] = comment
    if color:
        body['color'] = color

    response = send_requests.create_order(body=body)

    assert response.status_code == 201

    track_number = response.json()['track']

    assert track_number is not None

    return track_number


def positive_assert_get_order(track_number):
    response = send_requests.get_order_by_track_number(track_number)

    assert response.status_code == 200

    return response.json()


# Рената Дахер, 12-я когорта — Финальный проект. Инженер по тестированию плюс
def test_happy():
    body = {
        'firstName': 'Alexander',
        'lastName': 'Naumov'
    }

    track_number = positive_assert_create_order(**body)
    response_order = positive_assert_get_order(track_number)

    order = response_order['order']

    for key, value in order.items():
        if key in body:
            assert body[key] == value
        elif key in data.CREATE_ORDER_DATA:
            assert data.CREATE_ORDER_DATA[key] == value
