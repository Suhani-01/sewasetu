# Sewa Setu — Old Age Pension Portal

Handover copy. Vendor maintenance contract ended 31/01/2026.

## Running

```
docker compose up --build
```

- Portal: http://localhost:8000
- SMS gateway console (simulated telecom): http://localhost:8000/__gateway/ —
  "sent" OTPs appear here once delivered. The gateway runs on the internal
  network and is served through the portal, so only one port is exposed.
- Database: Postgres, loaded from `seed/seed.sql` on first boot

Production server logs (Jan–Jun 2026) are provided in `logs/`.

Listen to `dc-briefing.mp3` first (the DC's briefing), then read `BRIEF.md`.





The things i did for issue after holi :
1. Extract archieve log from logs/sewaset-logs........
this file contains : ._README.txt
    README.txt
    ._cron.log
    cron.log ( we need this )
    ._nginx-access.log.gz
    nginx-access.log.gz
    ._sewasetu-app.log.gz
    sewasetu-app.log.gz

command on terminal :
  New-Item -ItemType Directory -Force logs\extracted
  tar -xzf logs/sewasetu-logs-jan-jun-2026.tar.gz -C logs\extracted