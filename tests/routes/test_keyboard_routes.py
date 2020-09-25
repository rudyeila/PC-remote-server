import json 
import keyboard

class TestKeyboardRoute:
    KEYBOARD_ROUTE = "/keyboard"

    def test_press_key(self, app, client):
        keys = ["shift", "ctrl", "alt"]

        for key in keys: 
            res = client.post(self.KEYBOARD_ROUTE, json={"hotkey": key})
            assert res.status_code == 200
            expected = {"hotkey": key, "status": "success"}
            res_json = json.loads(res.get_data(as_text=True))
            assert expected == res_json
            # make sure key is released 
            assert not keyboard.is_pressed(key) 

    def test_press_and_hold_key(self, app, client):
        keys = ["shift", "ctrl", "alt"]

        for key in keys: 
            res = client.post(self.KEYBOARD_ROUTE, json={"hold": True, "hotkey": key})
            assert res.status_code == 200
            expected = {"hold": True, "hotkey": key, "status": "success"}
            res_json = json.loads(res.get_data(as_text=True))
            print(res_json)
            assert expected == res_json

            # release key 
            keyboard.release(key)
            assert keyboard.is_pressed(key) == False