# Task

An Apache access log is available at:

```
/app/access.log
```

Parse the log and create:

```
/app/report.json
```

The output must be valid JSON with exactly these fields:

```json
{
  "total_requests": 0,
  "unique_ips": 0,
  "top_path": ""
}
```

Success criteria

1. Count every request.
2. Count unique client IP addresses.
3. Determine the most frequently requested path.
4. Save the JSON as `/app/report.json`.