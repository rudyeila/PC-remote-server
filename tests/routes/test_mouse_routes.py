import pytest
import json

class TestMouseRoute:
    MOUSE_ROUTE = "/mouse"

    def test_get_mouse(self, app, client):
        res = client.get(self.MOUSE_ROUTE)
        res_json = json.loads(res.get_data(as_text=True))
        x_pos = res_json.get('x')
        y_pos = res_json.get('y')

        assert x_pos is not None and isinstance(x_pos, (int, float))
        assert y_pos is not None and isinstance(y_pos, (int, float))


class TestMousePositionRoute:
    POSITION_ROUTE = "/mouse/position"

    def test_get_position(self, app, client):
        res = client.get(self.POSITION_ROUTE)
        res_json = json.loads(res.get_data(as_text=True))
        x_pos = res_json.get('x')
        y_pos = res_json.get('y')

        assert x_pos is not None and isinstance(x_pos, (int, float))
        assert y_pos is not None and isinstance(y_pos, (int, float))