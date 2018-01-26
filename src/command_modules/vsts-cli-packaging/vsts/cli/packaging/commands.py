# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_feed_table_output

def load_packaging_commands(cli_command_loader):
    cli_command_loader.command_table['feed create'] = \
        cli_command_loader.create_command(module_name='packaging', name='feed create',
                                          operation='vsts.cli.packaging.common.feed#create_feed',
                                          table_transformer=transform_feed_table_output)
