def to_mesh_code(latitude: float, longitude: float, level: int) -> int:
    """緯度経度から指定次の地域メッシュコードを算出する。

    Args:
        longitude: 世界測地系の経度(度単位)
        latitude: 世界測地系の緯度(度単位)
        level: 地域メッシュコードの次数
                3次(1km四方):3
                4次(500m四方):4
                5次(250m四方):5
    Return:
        指定次の地域メッシュコード
    """
    if not 0 <= latitude < 66.66:
        raise ValueError("the latitude is out of bound.")

    if not 100 <= longitude < 180:
        raise ValueError("the longitude is out of bound.")
    if not (level in [3, 4, 5]):
        raise ValueError("invalid argument, level must be one of 3, 4, 5")

    # (1)緯度より p, q, r, s, t を算出
    p, a = divmod(latitude * 60, 40)
    q, b = divmod(a, 5)
    r, c = divmod(b * 60, 30)
    s, d = divmod(c, 15)
    t = d // 7.5

    # (2)経度よりu, v, w, x, y を算出
    u, f = divmod(longitude - 100, 1)
    v, g = divmod(f * 60, 7.5)
    w, h = divmod(g * 60, 45)
    x, i = divmod(h, 22.5)
    y = i // 11.25

    # (3) s, x より m を算出，t, y より n を算出
    m = (s * 2) + (x + 1)
    n = (t * 2) + (y + 1)

    mesh_code_str = (str(int(p)) + str(int(u)) + str(int(q)) + str(int(v)) +
                     str(int(r)) + str(int(w)) + str(int(m)) + str(int(n)))
    return int(mesh_code_str[:level + 5])
