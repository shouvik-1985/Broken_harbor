import json
from pathlib import Path


def test_report_exists():
    assert Path("/app/report.json").exists(), "report.json not found"


def test_report_contents():
    with open("/app/report.json") as f:
        report = json.load(f)

    expected = {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }

    assert report == expected