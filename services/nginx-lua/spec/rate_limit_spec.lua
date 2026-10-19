local rate_limit = require("plugins.rate_limit")

describe("rate_limit.check", function()
  before_each(function()
    rate_limit.reset()
  end)

  it("allows a burst and then throttles", function()
    for _ = 1, 3 do
      assert.is_true(rate_limit.check("client-a", 0, 3))
    end
    assert.is_false(rate_limit.check("client-a", 0, 3))
  end)
end)
