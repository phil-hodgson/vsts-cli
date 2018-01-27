# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list, ArgumentsContext

_ON_OFF_SWITCH_VALUES = ['on', 'off']

def load_packaging_arguments(cli_command_loader):
    with ArgumentsContext(cli_command_loader, 'packaging') as ac:
        ac.argument('team_instance', options_list=('--instance', '-i'))
        ac.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        
