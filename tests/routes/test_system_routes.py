import pytest
import json
import sys


# https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a
def test_base(app, client):
    """Make sure server is running"""
    res = client.get("/")
    assert res.status_code == 200
    expected = "Hello, World!"
    assert expected == res.get_data(as_text=True)


class TestVolumeRoute:
    VOLUME = "/system/volume"

    def test_get_volume(self, app, client):
        # Test route to get volume level
        res = client.get(TestVolumeRoute.VOLUME)
        assert res.status_code == 200

        # Make sure volume is part of of the response and the value is 0 <= volume <= 1.0
        res_json = json.loads(res.get_data(as_text=True))
        volume = res_json.get("volume")
        mute = res_json.get("mute")
        assert (volume is not None) and (mute is not None)
        assert volume >= 0.0 and volume <= 1.0
        assert isinstance(mute, int)


class TestVolumeLevelRoute:
    VOLUME_LEVEL = "/system/volume/level"

    def test_get_volume(self, app, client):
        # Test route to get volume level
        res = client.get(TestVolumeLevelRoute.VOLUME_LEVEL)
        assert res.status_code == 200

        # Make sure volume is part of of the response and the value is 0 <= volume <= 1.0
        res_json = json.loads(res.get_data(as_text=True))
        volume = res_json.get("volume")
        assert volume is not None
        assert volume >= 0.0 and volume <= 1.0

    def test_set_volume(self, app, client):
        # Make sure volume is unmuted.
        res = client.put(TestVolumeLevelRoute.VOLUME_LEVEL, json={"volume": 0.1})
        assert res.status_code == 200

        # Make sure volume is part of of the response and the value is almost equal to 0.1
        # Almost equal because floating point numbers can differ in the trailing digits
        res_json = json.loads(res.get_data(as_text=True))
        volume = res_json.get("volume")
        assert volume is not None
        expected = 0.1

        # Add margin for error due to numbers being float. We only care for the first few digits after the comma
        assert abs(expected - volume) < 0.00001

    def test_set_volume_illegal_value(self, app, client):
        # get current volume
        res = client.get(TestVolumeLevelRoute.VOLUME_LEVEL)
        assert res.status_code == 200

        res_json = json.loads(res.get_data(as_text=True))
        volume_old = res_json.get("volume")

        # try setting illegal value to volume
        res = client.put(TestVolumeLevelRoute.VOLUME_LEVEL, json={"volume": -0.5})
        assert res.status_code == 500

        # get volume again to make sure it didnt change
        res = client.get(TestVolumeLevelRoute.VOLUME_LEVEL)
        assert res.status_code == 200
        res_json = json.loads(res.get_data(as_text=True))
        volume_new = res_json.get("volume")

        # Make sure volume didn't change
        assert volume_old == volume_new


class TestMuteRoute:
    MUTE = "/system/volume/mute"

    def test_get_mute(self, app, client):
        # Make sure volume is unmuted.
        res = client.post(TestMuteRoute.MUTE, json={"mute": False})
        assert res.status_code == 200

        # Test route to get mute status
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