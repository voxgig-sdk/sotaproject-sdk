# Sotaproject SDK utility registration
require_relative '../core/utility_type'
require_relative 'clean'
require_relative 'done'
require_relative 'make_error'
require_relative 'feature_add'
require_relative 'feature_hook'
require_relative 'feature_init'
require_relative 'fetcher'
require_relative 'make_fetch_def'
require_relative 'make_context'
require_relative 'make_options'
require_relative 'make_request'
require_relative 'make_response'
require_relative 'make_result'
require_relative 'make_point'
require_relative 'make_spec'
require_relative 'make_url'
require_relative 'param'
require_relative 'prepare_auth'
require_relative 'prepare_body'
require_relative 'prepare_headers'
require_relative 'prepare_method'
require_relative 'prepare_params'
require_relative 'prepare_path'
require_relative 'prepare_query'
require_relative 'graphql'
require_relative 'result_basic'
require_relative 'result_body'
require_relative 'result_headers'
require_relative 'transform_request'
require_relative 'transform_response'

SotaprojectUtility.registrar = ->(u) {
  u.clean = SotaprojectUtilities::Clean
  u.done = SotaprojectUtilities::Done
  u.make_error = SotaprojectUtilities::MakeError
  u.feature_add = SotaprojectUtilities::FeatureAdd
  u.feature_hook = SotaprojectUtilities::FeatureHook
  u.feature_init = SotaprojectUtilities::FeatureInit
  u.fetcher = SotaprojectUtilities::Fetcher
  u.make_fetch_def = SotaprojectUtilities::MakeFetchDef
  u.make_context = SotaprojectUtilities::MakeContext
  u.make_options = SotaprojectUtilities::MakeOptions
  u.make_request = SotaprojectUtilities::MakeRequest
  u.make_response = SotaprojectUtilities::MakeResponse
  u.make_result = SotaprojectUtilities::MakeResult
  u.make_point = SotaprojectUtilities::MakePoint
  u.make_spec = SotaprojectUtilities::MakeSpec
  u.make_url = SotaprojectUtilities::MakeUrl
  u.param = SotaprojectUtilities::Param
  u.prepare_auth = SotaprojectUtilities::PrepareAuth
  u.prepare_body = SotaprojectUtilities::PrepareBody
  u.prepare_headers = SotaprojectUtilities::PrepareHeaders
  u.prepare_method = SotaprojectUtilities::PrepareMethod
  u.prepare_params = SotaprojectUtilities::PrepareParams
  u.prepare_path = SotaprojectUtilities::PreparePath
  u.prepare_query = SotaprojectUtilities::PrepareQuery
  u.graphql_body = SotaprojectUtilities::GraphqlBody
  u.graphql_errors = SotaprojectUtilities::GraphqlErrors
  u.result_basic = SotaprojectUtilities::ResultBasic
  u.result_body = SotaprojectUtilities::ResultBody
  u.result_headers = SotaprojectUtilities::ResultHeaders
  u.transform_request = SotaprojectUtilities::TransformRequest
  u.transform_response = SotaprojectUtilities::TransformResponse
}
