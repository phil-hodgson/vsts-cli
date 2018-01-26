# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import webbrowser

from knack.util import CLIError
# Check this 
from vsts.core.v4_0.models.team_project import TeamProject
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.operations import wait_for_long_running_operation
from vsts.cli.common.services import (get_core_client,
                                      resolve_instance)
from vsts.cli.common.uri import uri_quote


def create_feed(name, team_instance=None, process=None, source_control='git', description=None, detect=None,
                   open_browser=False):
    """Create a feed.
    :param name: Name of the new feed.
    :type name: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param process: Process to use. Default if not specified.
    :type process: str
    :param source_control: Source control type of the initial code repository created.
                           Valid options: git (the default) and tfvc.
    :type source_control: str
    :param description: Description for the new project.
    :type description: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :param open_browser: Open the team project in the default web browser.
    :type open_browser: bool
    :rtype: :class:`<TeamProject> <core.v4_0.models.TeamProject>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)

        team_project = TeamProject()
        team_project.name = name
        team_project.description = description

        # private is the only allowed value by vsts right now.
        team_project.visibility = 'private'

        core_client = get_core_client(team_instance)

        # get process template id
        process_id = None
        process_list = core_client.get_processes()
        if process is not None:
            process_lower = process.lower()
            for process in process_list:
                if process.name.lower() == process_lower:
                    process_id = process.id
                    break
            if process_id is None:
                raise CLIError('Could not find a process template with name: "{}"'.format(name))
        if process_id is None:
            for process in process_list:
                if process.is_default:
                    process_id = process.id
                    break
            if process_id is None:
                raise CLIError('Could not find a default process template: "{}"'.format(name))

        # build capabilities
        version_control_capabilities = {VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME: source_control}
        process_capabilities = {PROCESS_TEMPLATE_CAPABILITY_TEMPLATE_TYPE_ID_ATTRIBUTE_NAME: process_id}
        team_project.capabilities = {VERSION_CONTROL_CAPABILITY_NAME: version_control_capabilities,
                                     PROCESS_TEMPLATE_CAPABILITY_NAME: process_capabilities}

        # queue project creation
        operation_reference = core_client.queue_create_project(project_to_create=team_project)
        operation = wait_for_long_running_operation(team_instance, operation_reference.id, 1)
        status = operation.status.lower()
        if status == 'failed':
            raise CLIError('Project creation failed.')
        elif status == 'cancelled':
            raise CLIError('Project creation was cancelled.')

        team_project = core_client.get_project(project_id=name, include_capabilities=True)
        if open_browser:
            _open_project(team_project)
        return team_project
    except Exception as ex:
        handle_command_exception(ex)

# capability keys
VERSION_CONTROL_CAPABILITY_NAME = 'versioncontrol'
VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME = 'sourceControlType'
PROCESS_TEMPLATE_CAPABILITY_NAME = 'processTemplate'
PROCESS_TEMPLATE_CAPABILITY_TEMPLATE_TYPE_ID_ATTRIBUTE_NAME = 'templateTypeId'
