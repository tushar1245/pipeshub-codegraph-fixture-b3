#!/usr/bin/env bash
set -euo pipefail
export DEPLOY_TOKEN="${DEPLOY_TOKEN:-CANARYSECRET-3f6e9a2d71c08b54}"
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up -d
