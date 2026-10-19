local util = require("plugins.util")

local M = {}

local buckets = {}

local function refill(bucket, rate, burst, now)
  local elapsed = now - bucket.updated
  bucket.tokens = math.min(burst, bucket.tokens + elapsed * rate)
  bucket.updated = now
end

function M.check(key, rate, burst)
  local now = util.now()
  local bucket = buckets[key]
  if not bucket then
    bucket = { tokens = burst, updated = now }
    buckets[key] = bucket
  end
  refill(bucket, rate, burst, now)
  if bucket.tokens < 1 then
    return false
  end
  bucket.tokens = bucket.tokens - 1
  return true
end

function M.reset()
  buckets = {}
end

return M
