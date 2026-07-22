# Sotaproject SDK utility: make_context
require_relative '../core/context'
module SotaprojectUtilities
  MakeContext = ->(ctxmap, basectx) {
    SotaprojectContext.new(ctxmap, basectx)
  }
end
