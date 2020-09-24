import pytest
import json

from controllers.mouse_controller import LEFT_CLICK, RIGHT_CLICK, MIDDLE_CLICK, DOUBLE_CLICK

class TestMouseRoute:
    MOUSE_ROUTE = "/mouse"

    def test_get_mouse(self, app, client):
        res = client.get(self.MOUSE_ROUTE)
        assert res.status_code == 200

        res_json = json.loads(res.get_data(as_text=True))
        x_pos = res_json.get('x')
        y_pos = res_json.get('y')

        assert x_pos is not None and isinstance(x_pos, (int, float))
        assert y_pos is not None and isinstance(y_pos, (int, float))


class TestMousePositionRoute:
    POSITION_ROUTE = "/mouse/position"

    def test_get_position(self, app, client):
        res = client.get(self.POSITION_ROUTE)
        assert res.status_code == 200

        res_json = json.loads(res.get_data(as_text=True))
        x_pos = res_json.get('x')
        y_pos = res_json.get('y')

        assert x_pos is not None and isinstance(x_pos, (int, float))
        assert y_pos is not None and isinstance(y_pos, (int, float))

    def test_move_mouse_relative(self, app, client):
        res = client.get(self.POSITION_ROUTE)
        assert res.status_code == 200
        res_json = json.loads(res.get_data(as_text=True))
        x_old = res_json.get('x')
        y_old = res_json.get('y')
        
        res = client.post(self.POSITION_ROUTE, json={"x": 100, "y": 100})
        assert res.status_code == 200
        res_json = json.loads(res.get_data(as_text=True))
        x_new = res_json.get('x')
        y_new = res_json.get('y')
        assert x_new is not None and isinstance(x_new, (int, float))
        assert y_new is not None and isinstance(y_new, (int, float))
        expected_x = x_old + 100
        expected_y = y_old + 100

        assert x_new == expected_x
        assert y_new == expected_y
        
        # restore mouse position
        res = client.post(self.POSITION_ROUTE, json={"x": x_old, "y": y_old, "absolute": True})


    def test_move_mouse_absolute(self, app, client):
        res = client.get(self.POSITION_ROUTE)
        assert res.status_code == 200
        res_json = json.loads(res.get_data(as_text=True))
        x_old = res_json.get('x')
        y_old = res_json.get('y')
        
        expected_x = 0
        expected_y = 0
        res = client.post(self.POSITION_ROUTE, json={"x": expected_x, "y": expected_y, "absolute": True})
        assert res.status_code == 200
        res_json = json.loads(res.get_data(as_text=True))
        x_new = res_json.get('x')
        y_new = res_json.get('y')
        assert x_new is not None and isinstance(x_new, (int, float))
        assert y_new is not None and isinstance(y_new, (int, float))
        assert x_new == expected_x
        assert y_new == expected_y

        # restore mouse position
        res = client.post(self.POSITION_ROUTE, json={"x": x_old, "y": y_old, "absolute": True})


class TestMouseButtonsRoute:
    BUTTONS_ROUTE = "/mouse/buttons"

    def test_clicks(self, app, client):
        buttons = [LEFT_CLICK, RIGHT_CLICK, MIDDLE_CLICK, DOUBLE_CLICK]
        for button in buttons: 
            res = client.post(self.BUTTONS_ROUTE, json={"action": button})
            assert res.status_code == 200

            res_json = json.loads(res.get_data(as_text=True))
            expected_json = {"action": button, "result": "success"}
            assert res_json == expected_json

