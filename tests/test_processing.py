from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    assert filter_by_state(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        ]
    ) == [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


def test_sort_by_date():
    assert sort_by_date(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        ]
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
