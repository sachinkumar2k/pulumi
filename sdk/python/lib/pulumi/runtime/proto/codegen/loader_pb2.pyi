"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2023, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Parameterization(google.protobuf.message.Message):
    """Parameterization specifies the name, version, and value for a parameterized package."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """the parameterized package name."""
    version: builtins.str
    """the parameterized package version."""
    value: builtins.bytes
    """the parameter value for the parameterized package."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
        value: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "value", b"value", "version", b"version"]) -> None: ...

global___Parameterization = Parameterization

@typing_extensions.final
class GetSchemaRequest(google.protobuf.message.Message):
    """GetSchemaRequest allows the engine to return a schema for a given package and version."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PACKAGE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    DOWNLOAD_URL_FIELD_NUMBER: builtins.int
    PARAMETERIZATION_FIELD_NUMBER: builtins.int
    package: builtins.str
    """the package name for the schema being requested."""
    version: builtins.str
    """the version for the schema being requested, must be a valid semver or empty."""
    download_url: builtins.str
    """the optional download url for the schema being requested."""
    @property
    def parameterization(self) -> global___Parameterization:
        """the parameterization for the schema being requested, can be empty."""
    def __init__(
        self,
        *,
        package: builtins.str = ...,
        version: builtins.str = ...,
        download_url: builtins.str = ...,
        parameterization: global___Parameterization | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["parameterization", b"parameterization"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["download_url", b"download_url", "package", b"package", "parameterization", b"parameterization", "version", b"version"]) -> None: ...

global___GetSchemaRequest = GetSchemaRequest

@typing_extensions.final
class GetSchemaResponse(google.protobuf.message.Message):
    """GetSchemaResponse returns the schema data for the requested package."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEMA_FIELD_NUMBER: builtins.int
    schema: builtins.bytes
    """the JSON encoded schema."""
    def __init__(
        self,
        *,
        schema: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["schema", b"schema"]) -> None: ...

global___GetSchemaResponse = GetSchemaResponse
