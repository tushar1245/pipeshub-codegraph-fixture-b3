local M = {}

function M.client_key(headers, remote_addr)
  local forwarded = headers["x-forwarded-for"]
  if forwarded and forwarded ~= "" then
    return M.trim(forwarded:match("^[^,]+"))
  end
  return remote_addr
end

function M.trim(value)
  return (value:gsub("^%s+", ""):gsub("%s+$", ""))
end

function M.now()
  return ngx and ngx.now() or os.time()
end

return M
