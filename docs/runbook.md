# Runbook

- Payments failing: check the gateway health at `/healthz` on the Go
  gateway, then the Stripe status page.
- Cache stampede: lower `CACHE_TTL` and restart the API.
