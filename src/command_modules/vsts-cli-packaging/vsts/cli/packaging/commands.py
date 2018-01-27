# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_feed_table_output,transform_feeds_table_output

def load_packaging_commands(cli_command_loader):
    cli_command_loader.command_table['feed list'] = \
        cli_command_loader.create_command(module_name='packaging', name='feed list',
                                          operation='vsts.cli.packaging.common.feed#get_feeds',
                                          table_transformer=transform_feeds_table_output)
