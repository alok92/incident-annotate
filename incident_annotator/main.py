import argparse
import json
from datetime import datetime

GRAFANA_ANNOTATION_TEMPLATE = {
    "text": "",
    "tags": [],
    "time": 0,
    "timeEnd": 0,
    "isRegion": True
}

def parse_args():
    parser = argparse.ArgumentParser(description="Annotate incidents for Grafana dashboards or logs.")
    parser.add_argument("--start", required=True, help="Incident start time (e.g., 2024-07-01T10:00:00)")
    parser.add_argument("--end", required=True, help="Incident end time (e.g., 2024-07-01T10:30:00)")
    parser.add_argument("--summary", required=True, help="Incident summary or cause")
    parser.add_argument("--services", nargs="+", help="List of affected services")
    parser.add_argument("--output", choices=["json", "md"], default="json", help="Output format")
    parser.add_argument("--grafana", action="store_true", help="Output in Grafana annotation format")
    return parser.parse_args()

def to_unix_ms(timestamp: str) -> int:
    return int(datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").timestamp() * 1000)

def generate_markdown(summary: str, start: str, end: str, services=None) -> str:
    lines = ["## Incident Report", f"**Start:** {start}", f"**End:** {end}", f"**Summary:** {summary}"]
    if services:
        lines.append(f"**Services Affected:** {', '.join(services)}")
    return "\n\n".join(lines)

def generate_grafana_annotation(summary: str, start: str, end: str, services=None) -> dict:
    annotation = GRAFANA_ANNOTATION_TEMPLATE.copy()
    annotation["text"] = summary
    annotation["time"] = to_unix_ms(start)
    annotation["timeEnd"] = to_unix_ms(end)
    if services:
        annotation["tags"] = services
    return annotation

def main():
    args = parse_args()
    if args.grafana:
        annotation = generate_grafana_annotation(args.summary, args.start, args.end, args.services)
        print(json.dumps(annotation, indent=2))
    elif args.output == "md":
        md = generate_markdown(args.summary, args.start, args.end, args.services)
        print(md)
    else:
        data = {
            "summary": args.summary,
            "start": args.start,
            "end": args.end,
            "services": args.services or []
        }
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
