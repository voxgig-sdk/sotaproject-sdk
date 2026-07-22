# Sotaproject SDK utility: make_context

from core.context import SotaprojectContext


def make_context_util(ctxmap, basectx):
    return SotaprojectContext(ctxmap, basectx)
