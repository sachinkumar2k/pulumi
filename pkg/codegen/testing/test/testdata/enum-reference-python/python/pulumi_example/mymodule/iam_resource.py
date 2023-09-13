# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
import pulumi_google_native

__all__ = ['IamResourceArgs', 'IamResource']

@pulumi.input_type
class IamResourceArgs:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input['pulumi_google_native.iam.v1.AuditConfigArgs']] = None):
        """
        The set of arguments for constructing a IamResource resource.
        """
        IamResourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            config=config,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             config: Optional[pulumi.Input['pulumi_google_native.iam.v1.AuditConfigArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if config is not None:
            _setter("config", config)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['pulumi_google_native.iam.v1.AuditConfigArgs']]:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['pulumi_google_native.iam.v1.AuditConfigArgs']]):
        pulumi.set(self, "config", value)


class IamResource(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['pulumi_google_native.iam.v1.AuditConfigArgs']]] = None,
                 __props__=None):
        """
        Create a IamResource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[IamResourceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a IamResource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IamResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IamResourceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['pulumi_google_native.iam.v1.AuditConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IamResourceArgs.__new__(IamResourceArgs)

            if not isinstance(config, pulumi_google_native.iam.v1.AuditConfigArgs):
                config = config or {}
                def _setter(key, value):
                    config[key] = value
                pulumi_google_native.iam.v1.AuditConfigArgs._configure(_setter, **config)
            __props__.__dict__["config"] = config
        super(IamResource, __self__).__init__(
            'example:myModule:IamResource',
            resource_name,
            __props__,
            opts,
            remote=True)

