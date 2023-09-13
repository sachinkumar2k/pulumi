# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'TopLevel',
]

@pulumi.output_type
class TopLevel(dict):
    def __init__(__self__, *,
                 buzz: Optional[str] = None):
        TopLevel._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            buzz=buzz,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             buzz: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if buzz is not None:
            _setter("buzz", buzz)

    @property
    @pulumi.getter
    def buzz(self) -> Optional[str]:
        return pulumi.get(self, "buzz")


