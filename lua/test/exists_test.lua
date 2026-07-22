-- Sotaproject SDK exists test

local sdk = require("sotaproject_sdk")

describe("SotaprojectSDK", function()
  it("should create test SDK", function()
    local testsdk = sdk.test(nil, nil)
    assert.is_not_nil(testsdk)
  end)
end)
