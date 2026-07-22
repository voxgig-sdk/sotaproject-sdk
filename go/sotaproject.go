package voxgigsotaprojectsdk

import (
	"github.com/voxgig-sdk/sotaproject-sdk/go/core"
	"github.com/voxgig-sdk/sotaproject-sdk/go/entity"
	"github.com/voxgig-sdk/sotaproject-sdk/go/feature"
	_ "github.com/voxgig-sdk/sotaproject-sdk/go/utility"
)

// Type aliases preserve external API.
type SotaprojectSDK = core.SotaprojectSDK
type Context = core.Context
type Utility = core.Utility
type Feature = core.Feature
type Entity = core.Entity
type SotaprojectEntity = core.SotaprojectEntity
type FetcherFunc = core.FetcherFunc
type Spec = core.Spec
type Result = core.Result
type Response = core.Response
type Operation = core.Operation
type Control = core.Control
type SotaprojectError = core.SotaprojectError

// BaseFeature from feature package.
type BaseFeature = feature.BaseFeature

func init() {
	core.NewBaseFeatureFunc = func() core.Feature {
		return feature.NewBaseFeature()
	}
	core.NewTestFeatureFunc = func() core.Feature {
		return feature.NewTestFeature()
	}
	core.NewPublicationEntityFunc = func(client *core.SotaprojectSDK, entopts map[string]any) core.SotaprojectEntity {
		return entity.NewPublicationEntity(client, entopts)
	}
}

// Constructor re-exports.
var NewSotaprojectSDK = core.NewSotaprojectSDK
var TestSDK = core.TestSDK
var NewContext = core.NewContext
var NewSpec = core.NewSpec
var NewResult = core.NewResult
var NewResponse = core.NewResponse
var NewOperation = core.NewOperation
var MakeConfig = core.MakeConfig

// No-arg convenience constructors. Go has no default-argument syntax,
// so these aliases let callers write `sdk.New()` / `sdk.Test()`
// instead of `sdk.NewSotaprojectSDK(nil)` / `sdk.TestSDK(nil, nil)`
// for the common no-options case.
func New() *SotaprojectSDK  { return NewSotaprojectSDK(nil) }
func Test() *SotaprojectSDK { return TestSDK(nil, nil) }
var NewBaseFeature = feature.NewBaseFeature
var NewTestFeature = feature.NewTestFeature
