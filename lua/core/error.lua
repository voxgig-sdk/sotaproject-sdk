-- Sotaproject SDK error

local SotaprojectError = {}
SotaprojectError.__index = SotaprojectError


function SotaprojectError.new(code, msg, ctx)
  local self = setmetatable({}, SotaprojectError)
  self.is_sdk_error = true
  self.sdk = "Sotaproject"
  self.code = code or ""
  self.msg = msg or ""
  self.ctx = ctx
  self.result = nil
  self.spec = nil
  return self
end


function SotaprojectError:error()
  return self.msg
end


function SotaprojectError:__tostring()
  return self.msg
end


return SotaprojectError
