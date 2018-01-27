# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import transform_feed_table_output,transform_feeds_table_output


def load_packaging_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'packaging', 'vsts.cli.packaging.common.{}') as g:
        # basic feed commands
        # g.command('feed create', 'feed#create_feed',
        #           table_transformer=transform_feed_table_output)
        # g.command('feed update', 'feed#update_feed',
        #           table_transformer=transform_feed_table_output)
        g.command('feed show', 'feed#show_feed',
                  table_transformer=transform_feed_table_output)
        g.command('feed list', 'feed#get_feeds',
                  table_transformer=transform_feeds_table_output)
