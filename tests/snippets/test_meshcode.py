import pytest

from src.snippets.meshcode import to_mesh_code


@pytest.mark.parametrize(('args', 'expected'), [
    ({"lat": 35.70078, "lon": 139.71475, "level": 3}, 53394547),
    ({"lat": 35.70078, "lon": 139.71475, "level": 4}, 533945471),
    ({"lat": 35.70078, "lon": 139.71475, "level": 5}, 5339454711),
    ({"lat": 35.658581, "lon": 139.745433, "level": 3}, 53393599),
    ({"lat": 35.658581, "lon": 139.745433, "level": 4}, 533935992),
    ({"lat": 35.658581, "lon": 139.745433, "level": 5}, 5339359921),
    ({"lat": 34.987574, "lon": 135.759363, "level": 3}, 52353680),
    ({"lat": 34.987574, "lon": 135.759363, "level": 4}, 523536804),
    ({"lat": 34.987574, "lon": 135.759363, "level": 5}, 5235368041),
])
def test_to_mesh_code(args: dict, expected: int):
    assert to_mesh_code(args["lat"], args["lon"], args["level"]) == expected


@pytest.mark.parametrize(('args', 'expected'), [
    ({"lat": 70.2, "lon": 139.71475, "level": 3}, "the latitude is out of bound."),
    ({"lat": 35.70078, "lon": 180.9, "level": 4}, "the longitude is out of bound."),
    ({"lat": 35.70078, "lon": 139.71475, "level": 1}, "invalid argument, level must be one of 3, 4, 5"),
])
def test_to_mesh_code_err(args: dict, expected: int):
    with pytest.raises(Exception) as err:
        _ = to_mesh_code(args["lat"], args["lon"], args["level"])
    assert str(err.value) == expected
