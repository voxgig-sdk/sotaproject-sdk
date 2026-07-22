# Sotaproject SDK exists test

require "minitest/autorun"
require_relative "../Sotaproject_sdk"

class ExistsTest < Minitest::Test
  def test_create_test_sdk
    testsdk = SotaprojectSDK.test(nil, nil)
    assert !testsdk.nil?
  end
end
