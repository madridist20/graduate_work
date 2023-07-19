import requests
from dotenv import load_dotenv

load_dotenv()


def test_success_create_room(access_headers):
    response = requests.post(
        f"http://localhost/cinema_v1/room/b8e8169d-c58d-4d63-81e3-789468881e1c",
        headers=access_headers,
    )
    resp = response.json()
    assert resp["success"] is True


def test_get_all_rooms(access_headers):
    """
    test all rows
    """
    response = requests.get(
        "http://localhost/cinema_v1/rooms/",
        headers=access_headers,
    )
    resp = response.json()
    assert len(resp) == 1


def test_get_specific_room(access_headers):
    response = requests.get(
        f"http://localhost/cinema_v1/room/b8e8169d-c58d-4d63-81e3-789468881e1c",
        headers=access_headers,
    )
    resp = response.json()
    assert resp["success"] is True
    assert resp["film_work_uuid"] == "b8e8169d-c58d-4d63-81e3-789468881e1c"


def test_get_nonexistent_room(access_headers):
    response = requests.get(
        "http://localhost/cinema_v1/room/nonexistent_room",
        headers=access_headers,
    )
    resp = response.json()
    assert resp["success"] is False
    assert resp["errors"] == ["Room does not exist!"]


def test_delete_room(access_headers):
    response = requests.delete(
        f"http://localhost/cinema_v1/room/b8e8169d-c58d-4d63-81e3-789468881e1c",
        headers=access_headers,
    )
    resp = response.json()
    assert resp["success"] is True


def test_delete_nonexistent_room(access_headers):
    response = requests.delete(
        "http://localhost/cinema_v1/room/nonexistent_room",
        headers=access_headers,
    )
    resp = response.json()
    assert resp["success"] is False
    assert resp["errors"] == ["Room does not exist!"]
