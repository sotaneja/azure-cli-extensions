# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MaintenanceClientConfiguration
from .operations import PublicMaintenanceConfigurationOperations
from .operations import ApplyUpdateOperations
from .operations import ConfigurationAssignmentOperations
from .operations import MaintenanceConfigurationOperations
from .operations import OperationOperations
from .operations import UpdateOperations
from . import models


class MaintenanceClient(object):
    """Maintenance Client.

    :ivar public_maintenance_configuration: PublicMaintenanceConfigurationOperations operations
    :vartype public_maintenance_configuration: maintenance_client.operations.PublicMaintenanceConfigurationOperations
    :ivar apply_update: ApplyUpdateOperations operations
    :vartype apply_update: maintenance_client.operations.ApplyUpdateOperations
    :ivar configuration_assignment: ConfigurationAssignmentOperations operations
    :vartype configuration_assignment: maintenance_client.operations.ConfigurationAssignmentOperations
    :ivar maintenance_configuration: MaintenanceConfigurationOperations operations
    :vartype maintenance_configuration: maintenance_client.operations.MaintenanceConfigurationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: maintenance_client.operations.OperationOperations
    :ivar update: UpdateOperations operations
    :vartype update: maintenance_client.operations.UpdateOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MaintenanceClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.public_maintenance_configuration = PublicMaintenanceConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.apply_update = ApplyUpdateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configuration_assignment = ConfigurationAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.maintenance_configuration = MaintenanceConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.update = UpdateOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MaintenanceClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
