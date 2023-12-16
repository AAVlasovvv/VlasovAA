def custom_sum(*args):
    for v in args:
        # Which is better?

        # # This:
        # if not isinstance(v, (int, float)):
        #     raise TypeError

        # Or this?
        assert isinstance(v, (int, float))

    s = 0
    for v in args:
        s += v
    return s


custom_sum('ada', 3, 5 , 'frgg')