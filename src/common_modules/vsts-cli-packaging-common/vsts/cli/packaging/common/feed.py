# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.feed.v4_1.models.feed import Feed
from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.services import (get_feed_client,
                                      resolve_instance)

def get_feeds(team_instance=None, detect=None):
    """Get a list of feeds.
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
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


def show_feed(name, team_instance=None, detect=None):
    """Show a feed.
    :param name: The name of the feed.
    :type name: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
    :type detect: str
    :rtype: :class:`Feed <feed.v4_1.models.Feed>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        feed_client = get_feed_client(team_instance)
        feed = feed_client.get_feed(name)
        return feed
    except Exception as ex:
        handle_command_exception(ex)


def delete_feed(name, team_instance=None, detect=None):
    """Delete a feed.
    :param name: The name of the feed.
    :type name: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
    :type detect: str
    :rtype: list of :class:`<Feed> <feed.v4_1.models.Feed>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        feed_client = get_feed_client(team_instance)
        feed_client.delete_feed(name)
        print('The feed \'' + name + '\' was successfully deleted.')
    except Exception as ex:
        handle_command_exception(ex)

def update_feed(name, description=None, team_instance=None, detect=None):
    """Update a feed.
    :param name: The name of the feed.
    :type name: str
    :param description: New description for the feed.
    :type description: str
    :param team_instance: The URI for the VSTS account (https://<account>.visualstudio.com) or your TFS project
                          collection.
    :type team_instance: str
    :param detect: Automatically detect instance. Default is "on".
    :type detect: str
    :rtype: :class:`Feed <feed.v4_1.models.Feed>`
    """
    try:
        team_instance = resolve_instance(detect=detect, team_instance=team_instance)
        feed_client = get_feed_client(team_instance)
        feed = feed_client.get_feed(name)

        if description is not None:
            feed.description = description

        updated_feed = feed_client.update_feed(feed, name)
        return updated_feed
    except Exception as ex:
        handle_command_exception(ex)