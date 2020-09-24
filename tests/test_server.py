import pytest
import json
import sys

sys.path.insert(0, "../")


# https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a


def test_base(app, client):
    """Make sure server is running"""
    res = client.get("/")
    assert res.status_code == 200
    expected = "Hello, World!"
    assert expected == res.get_data(as_text=True)



class TestMuteRoute:
    MUTE = "/system/volume/mute"

    # Test mute 
    def test_get_mute(self, app, client):
        # Make sure volume is unmuted.
        res = client.post(TestMuteRoute.MUTE, json={"mute": False})
        print(res.status_code)
        print(res.data)
        assert res.status_code == 200


        res = client.get(TestMuteRoute.MUTE)
        assert res.status_code == 200
        expected = {"mute": False}
        assert expected == json.loads(res.get_data(as_text=True))

    def test_toggle_mute(self, app, client):
        # First read current mute status 
        res = client.get(TestMuteRoute.MUTE)
        body = json.loads(res.get_data(as_text=True))
        mute_status = body.get("mute")
        assert mute_status is not None, "Failed to get mute status"

        # Toggle mute 
        res = client.post(TestMuteRoute.MUTE)
        assert res.status_code == 200

        # Expect new mute status to be the opposite of the one before toggling
        expected = {"mute": not mute_status}
        assert expected == json.loads(res.get_data(as_text=True))

        # Unmute
        client.post(TestMuteRoute.MUTE, json={"mute": False})

    def test_set_mute(self, app, client):
        # Start unmuted
        res = client.post(TestMuteRoute.MUTE, json={"mute": False})
        assert res.status_code == 200

        # Mute 
        res = client.post(TestMuteRoute.MUTE, json={"mute": True})
        assert res.status_code == 200
        expected = {"mute": True}
        assert expected == json.loads(res.get_data(as_text=True))

        # Unmute 
        res = client.post(TestMuteRoute.MUTE, json={"mute": False})
        assert res.status_code == 200
        expected = {"mute": False}
        assert expected == json.loads(res.get_data(as_text=True))