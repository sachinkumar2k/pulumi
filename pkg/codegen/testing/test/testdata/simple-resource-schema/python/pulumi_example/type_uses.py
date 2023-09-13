# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *
from .resource import Resource

__all__ = ['TypeUsesArgs', 'TypeUses']

@pulumi.input_type
class TypeUsesArgs:
    def __init__(__self__, *,
                 bar: Optional[pulumi.Input['SomeOtherObjectArgs']] = None,
                 baz: Optional[pulumi.Input['ObjectWithNodeOptionalInputsArgs']] = None,
                 foo: Optional[pulumi.Input['ObjectArgs']] = None):
        """
        The set of arguments for constructing a TypeUses resource.
        """
        TypeUsesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bar=bar,
            baz=baz,
            foo=foo,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bar: Optional[pulumi.Input['SomeOtherObjectArgs']] = None,
             baz: Optional[pulumi.Input['ObjectWithNodeOptionalInputsArgs']] = None,
             foo: Optional[pulumi.Input['ObjectArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if bar is not None:
            _setter("bar", bar)
        if baz is not None:
            _setter("baz", baz)
        if foo is not None:
            _setter("foo", foo)

    @property
    @pulumi.getter
    def bar(self) -> Optional[pulumi.Input['SomeOtherObjectArgs']]:
        return pulumi.get(self, "bar")

    @bar.setter
    def bar(self, value: Optional[pulumi.Input['SomeOtherObjectArgs']]):
        pulumi.set(self, "bar", value)

    @property
    @pulumi.getter
    def baz(self) -> Optional[pulumi.Input['ObjectWithNodeOptionalInputsArgs']]:
        return pulumi.get(self, "baz")

    @baz.setter
    def baz(self, value: Optional[pulumi.Input['ObjectWithNodeOptionalInputsArgs']]):
        pulumi.set(self, "baz", value)

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input['ObjectArgs']]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input['ObjectArgs']]):
        pulumi.set(self, "foo", value)


class TypeUses(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bar: Optional[pulumi.Input[pulumi.InputType['SomeOtherObjectArgs']]] = None,
                 baz: Optional[pulumi.Input[pulumi.InputType['ObjectWithNodeOptionalInputsArgs']]] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['ObjectArgs']]] = None,
                 __props__=None):
        """
        Create a TypeUses resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TypeUsesArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a TypeUses resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TypeUsesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TypeUsesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TypeUsesArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bar: Optional[pulumi.Input[pulumi.InputType['SomeOtherObjectArgs']]] = None,
                 baz: Optional[pulumi.Input[pulumi.InputType['ObjectWithNodeOptionalInputsArgs']]] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['ObjectArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TypeUsesArgs.__new__(TypeUsesArgs)

            if not isinstance(bar, SomeOtherObjectArgs):
                bar = bar or {}
                def _setter(key, value):
                    bar[key] = value
                SomeOtherObjectArgs._configure(_setter, **bar)
            __props__.__dict__["bar"] = bar
            if not isinstance(baz, ObjectWithNodeOptionalInputsArgs):
                baz = baz or {}
                def _setter(key, value):
                    baz[key] = value
                ObjectWithNodeOptionalInputsArgs._configure(_setter, **baz)
            __props__.__dict__["baz"] = baz
            if not isinstance(foo, ObjectArgs):
                foo = foo or {}
                def _setter(key, value):
                    foo[key] = value
                ObjectArgs._configure(_setter, **foo)
            __props__.__dict__["foo"] = foo
        super(TypeUses, __self__).__init__(
            'example::TypeUses',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TypeUses':
        """
        Get an existing TypeUses resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TypeUsesArgs.__new__(TypeUsesArgs)

        __props__.__dict__["bar"] = None
        __props__.__dict__["baz"] = None
        __props__.__dict__["foo"] = None
        return TypeUses(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bar(self) -> pulumi.Output[Optional['outputs.SomeOtherObject']]:
        return pulumi.get(self, "bar")

    @property
    @pulumi.getter
    def baz(self) -> pulumi.Output[Optional['outputs.ObjectWithNodeOptionalInputs']]:
        return pulumi.get(self, "baz")

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Output[Optional['outputs.Object']]:
        return pulumi.get(self, "foo")

