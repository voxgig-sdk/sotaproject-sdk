# Sotaproject SDK feature factory

require_relative 'feature/base_feature'
require_relative 'feature/test_feature'


module SotaprojectFeatures
  def self.make_feature(name)
    case name
    when "base"
      SotaprojectBaseFeature.new
    when "test"
      SotaprojectTestFeature.new
    else
      SotaprojectBaseFeature.new
    end
  end
end
