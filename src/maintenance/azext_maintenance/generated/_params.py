# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_maintenance.action import AddExtensionProperties


def load_arguments(self, _):

    with self.argument_context('maintenance public-maintenance-configuration show') as c:
        c.argument('resource_name', type=str, help='Resource Identifier', id_part='name')

    with self.argument_context('maintenance apply-update show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
        c.argument('apply_update_name', options_list=['--name', '-n', '--apply-update-name'], type=str, help=''
                   'applyUpdate Id')

    with self.argument_context('maintenance apply-update create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')

    with self.argument_context('maintenance apply-update update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')

    with self.argument_context('maintenance apply-update get-parent') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
        c.argument('apply_update_name', options_list=['--name', '-n', '--apply-update-name'], type=str, help=''
                   'applyUpdate Id')

    with self.argument_context('maintenance configuration-assignment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')

    with self.argument_context('maintenance configuration-assignment create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
        c.argument('configuration_assignment_name', options_list=['--name', '-n', '--configuration-assignment-name'],
                   type=str, help='Configuration assignment name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('maintenance_configuration_id', type=str, help='The maintenance configuration Id')
        c.argument('resource_id', type=str, help='The unique resourceId')

    with self.argument_context('maintenance configuration-assignment update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
        c.argument('configuration_assignment_name', options_list=['--name', '-n', '--configuration-assignment-name'],
                   type=str, help='Configuration assignment name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('maintenance_configuration_id', type=str, help='The maintenance configuration Id')
        c.argument('resource_id', type=str, help='The unique resourceId')

    with self.argument_context('maintenance configuration-assignment delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
        c.argument('configuration_assignment_name', options_list=['--name', '-n', '--configuration-assignment-name'],
                   type=str, help='Unique configuration assignment name')

    with self.argument_context('maintenance configuration-assignment list-parent') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')

    with self.argument_context('maintenance maintenance-configuration show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='Resource Identifier')

    with self.argument_context('maintenance maintenance-configuration create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='Resource Identifier')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('namespace', type=str, help='Gets or sets namespace of the resource')
        c.argument('extension_properties', action=AddExtensionProperties, nargs='*', help='Gets or sets '
                   'extensionProperties of the maintenanceConfiguration Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('maintenance_scope', arg_type=get_enum_type(['All', 'Host', 'Resource', 'InResource', 'OSImage', ''
                                                                'Extension', 'InGuestPatch', 'SQLDB', ''
                                                                'SQLManagedInstance']), help='Gets or sets '
                   'maintenanceScope of the configuration')
        c.argument('visibility', arg_type=get_enum_type(['Custom', 'Public']), help='Gets or sets the visibility of '
                   'the configuration')
        c.argument('maintenance_window_start_date_time', type=str, help='Effective start date of the maintenance '
                   'window in YYYY-MM-DD hh:mm format. The start date can be set to either the current date or future '
                   'date. The window will be created in the time zone provided and adjusted to daylight savings '
                   'according to that time zone.')
        c.argument('maintenance_window_expiration_date_time', type=str, help='Effective expiration date of the '
                   'maintenance window in YYYY-MM-DD hh:mm format. The window will be created in the time zone '
                   'provided and adjusted to daylight savings according to that time zone. Expiration date must be set '
                   'to a future date. If not provided, it will be set to the maximum datetime 9999-12-31 23:59:59.')
        c.argument('maintenance_window_duration', type=str, help='Duration of the maintenance window in HH:mm format. '
                   'If not provided, default value will be used based on maintenance scope provided. Example: 05:00.')
        c.argument('maintenance_window_time_zone', type=str, help='Name of the timezone. List of timezones can be '
                   'obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific '
                   'Standard Time, UTC, W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.')
        c.argument('maintenance_window_recur_every', type=str, help='Rate at which a Maintenance window is expected to '
                   'recur. The rate can be expressed as daily, weekly, or monthly schedules. Daily schedule are '
                   'formatted as recurEvery: [Frequency as integer][\'Day(s)\']. If no frequency is provided, the '
                   'default frequency is 1. Daily schedule examples are recurEvery: Day, recurEvery: 3Days.  Weekly '
                   'schedule are formatted as recurEvery: [Frequency as integer][\'Week(s)\'] [Optional comma '
                   'separated list of weekdays Monday-Sunday]. Weekly schedule examples are recurEvery: 3Weeks, '
                   'recurEvery: Week Saturday,Sunday. Monthly schedules are formatted as [Frequency as '
                   'integer][\'Month(s)\'] [Comma separated list of month days] or [Frequency as '
                   'integer][\'Month(s)\'] [Week of Month (First, Second, Third, Fourth, Last)] [Weekday '
                   'Monday-Sunday]. Monthly schedule examples are recurEvery: Month, recurEvery: 2Months, recurEvery: '
                   'Month day23,day24, recurEvery: Month Last Sunday, recurEvery: Month Fourth Monday.')

    with self.argument_context('maintenance maintenance-configuration update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='Resource Identifier')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('namespace', type=str, help='Gets or sets namespace of the resource')
        c.argument('extension_properties', action=AddExtensionProperties, nargs='*', help='Gets or sets '
                   'extensionProperties of the maintenanceConfiguration Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('maintenance_scope', arg_type=get_enum_type(['All', 'Host', 'Resource', 'InResource', 'OSImage', ''
                                                                'Extension', 'InGuestPatch', 'SQLDB', ''
                                                                'SQLManagedInstance']), help='Gets or sets '
                   'maintenanceScope of the configuration')
        c.argument('visibility', arg_type=get_enum_type(['Custom', 'Public']), help='Gets or sets the visibility of '
                   'the configuration')
        c.argument('maintenance_window_start_date_time', type=str, help='Effective start date of the maintenance '
                   'window in YYYY-MM-DD hh:mm format. The start date can be set to either the current date or future '
                   'date. The window will be created in the time zone provided and adjusted to daylight savings '
                   'according to that time zone.')
        c.argument('maintenance_window_expiration_date_time', type=str, help='Effective expiration date of the '
                   'maintenance window in YYYY-MM-DD hh:mm format. The window will be created in the time zone '
                   'provided and adjusted to daylight savings according to that time zone. Expiration date must be set '
                   'to a future date. If not provided, it will be set to the maximum datetime 9999-12-31 23:59:59.')
        c.argument('maintenance_window_duration', type=str, help='Duration of the maintenance window in HH:mm format. '
                   'If not provided, default value will be used based on maintenance scope provided. Example: 05:00.')
        c.argument('maintenance_window_time_zone', type=str, help='Name of the timezone. List of timezones can be '
                   'obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific '
                   'Standard Time, UTC, W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.')
        c.argument('maintenance_window_recur_every', type=str, help='Rate at which a Maintenance window is expected to '
                   'recur. The rate can be expressed as daily, weekly, or monthly schedules. Daily schedule are '
                   'formatted as recurEvery: [Frequency as integer][\'Day(s)\']. If no frequency is provided, the '
                   'default frequency is 1. Daily schedule examples are recurEvery: Day, recurEvery: 3Days.  Weekly '
                   'schedule are formatted as recurEvery: [Frequency as integer][\'Week(s)\'] [Optional comma '
                   'separated list of weekdays Monday-Sunday]. Weekly schedule examples are recurEvery: 3Weeks, '
                   'recurEvery: Week Saturday,Sunday. Monthly schedules are formatted as [Frequency as '
                   'integer][\'Month(s)\'] [Comma separated list of month days] or [Frequency as '
                   'integer][\'Month(s)\'] [Week of Month (First, Second, Third, Fourth, Last)] [Weekday '
                   'Monday-Sunday]. Monthly schedule examples are recurEvery: Month, recurEvery: 2Months, recurEvery: '
                   'Month day23,day24, recurEvery: Month Last Sunday, recurEvery: Month Fourth Monday.')

    with self.argument_context('maintenance maintenance-configuration delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='Resource Identifier')

    with self.argument_context('maintenance update list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')

    with self.argument_context('maintenance update list-parent') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Resource provider name')
        c.argument('resource_parent_type', type=str, help='Resource parent type')
        c.argument('resource_parent_name', type=str, help='Resource parent identifier')
        c.argument('resource_type', type=str, help='Resource type')
        c.argument('resource_name', type=str, help='Resource identifier')
