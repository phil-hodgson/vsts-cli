# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict

def transform_feed_table_output(result):
    table_output = [_transform_feed_row(result)]
    return table_output


def _transform_feed_row(row):
    from vsts.cli.packaging.common.feed import (PROCESS_TEMPLATE_CAPABILITY_NAME,
                                              VERSION_CONTROL_CAPABILITY_NAME,
                                              VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME)
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['State'] = row['state']

    if 'capabilities' in row:
        capabilities = row['capabilities']
        if PROCESS_TEMPLATE_CAPABILITY_NAME in capabilities:
            process_capabilities = capabilities[PROCESS_TEMPLATE_CAPABILITY_NAME]
            if 'templateName' in process_capabilities:
                table_row['Process'] = process_capabilities['templateName']
        if VERSION_CONTROL_CAPABILITY_NAME in capabilities:
            version_capabilities = capabilities[VERSION_CONTROL_CAPABILITY_NAME]
            if VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME in version_capabilities:
                table_row['Source Control'] = version_capabilities[VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME]

    return table_row
