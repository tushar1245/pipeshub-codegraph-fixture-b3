local rate_limit = require("plugins.rate_limit")
local util = require("plugins.util")

local RATE = tonumber(os.getenv("RATE_LIMIT_PER_SEC") or "10")
local BURST = tonumber(os.getenv("RATE_LIMIT_BURST") or "20")

local function access()
  local key = util.client_key(ngx.req.get_headers(), ngx.var.remote_addr)
  if not rate_limit.check(key, RATE, BURST) then
    return ngx.exit(429)
  end
end

return {
  access = access,
}
