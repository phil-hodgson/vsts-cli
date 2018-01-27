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
from vsts.cli.common.services import (get_feed_client,
                                      resolve_instance)
from vsts.cli.common.uri import uri_quote


def get_feeds(team_instance=None, detect=None):
    """Get a list of feeds.
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: When 'On' unsupplied arg values will be detected from the current working
                   directory's repo.
    :type detect: str
    :rtype: list of :class:`<Feed> <feed.v4_1.models.Feed>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        feed_client = get_feed_client(team_instance)

        feed_list = feed_client.get_feeds()

        return feed_list
    except Exception as ex:
        handle_command_exception(ex)
