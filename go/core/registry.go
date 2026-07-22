package core

var UtilityRegistrar func(u *Utility)

var NewBaseFeatureFunc func() Feature

var NewTestFeatureFunc func() Feature

var NewPublicationEntityFunc func(client *SotaprojectSDK, entopts map[string]any) SotaprojectEntity

