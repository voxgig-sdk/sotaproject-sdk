# Sotaproject SDK utility: make_context

from projectname_sdk.core.context import SotaprojectContext


def make_context_util(ctxmap, basectx):
    return SotaprojectContext(ctxmap, basectx)
