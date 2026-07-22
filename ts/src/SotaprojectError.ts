
import { Context } from './Context'


class SotaprojectError extends Error {

  isSotaprojectError = true

  sdk = 'Sotaproject'

  code: string
  ctx: Context

  constructor(code: string, msg: string, ctx: Context) {
    super(msg)
    this.code = code
    this.ctx = ctx
  }

}

export {
  SotaprojectError
}

