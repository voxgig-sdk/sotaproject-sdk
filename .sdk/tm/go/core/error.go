package core

type SotaprojectError struct {
	IsSotaprojectError bool
	Sdk              string
	Code             string
	Msg              string
	Ctx              *Context
	Result           any
	Spec             any
}

func NewSotaprojectError(code string, msg string, ctx *Context) *SotaprojectError {
	return &SotaprojectError{
		IsSotaprojectError: true,
		Sdk:              "Sotaproject",
		Code:             code,
		Msg:              msg,
		Ctx:              ctx,
	}
}

func (e *SotaprojectError) Error() string {
	return e.Msg
}
