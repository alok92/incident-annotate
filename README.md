[![CI](https://github.com/alok92/incident-annotator/actions/workflows/ci.yml/badge.svg)](https://github.com/alok92/incident-annotate/blob/main/.github/workflows/ci.yml)

# 📍 Incident Annotator

> A simple Python CLI to annotate Grafana dashboards or logs with incident metadata.

### ✨ Features

- Annotate incidents with start/end time, summary, and affected services
- Output in:
  - JSON (default)
  - Markdown (`--output md`)
  - Grafana annotation format (`--grafana`)

### 🚀 Usage

```bash
python -m incident_annotator.main \
  --start 2025-07-05T10:00:00 \
  --end 2025-07-05T10:30:00 \
  --summary "Database outage due to network partition" \
  --services database api \
  --grafana
```

### 🔧 Output Example (Grafana)

```json
{
  "text": "Database outage due to network partition",
  "tags": ["database", "api"],
  "time": 1751699400000,
  "timeEnd": 1751701200000,
  "isRegion": true
}
```

### 🧪 Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 📄 License

MIT © [Alok](https://github.com/alok92)
