from incident_annotator.main import generate_markdown, generate_grafana_annotation

def test_grafana_annotation_basic():
    summary = "Test incident"
    start = "2025-07-05T10:00:00"
    end = "2025-07-05T10:30:00"
    services = ["api", "db"]
    ann = generate_grafana_annotation(summary, start, end, services)
    assert ann["text"] == summary
    assert ann["tags"] == services
    assert ann["time"] < ann["timeEnd"]
    assert ann["isRegion"] is True

def test_markdown_output():
    summary = "Latency spike"
    start = "2025-07-05T09:00:00"
    end = "2025-07-05T09:15:00"
    services = ["cache"]
    md = generate_markdown(summary, start, end, services)
    assert "Latency spike" in md
    assert "2025-07-05T09:00:00" in md
    assert "cache" in md
