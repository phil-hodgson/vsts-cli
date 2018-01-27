# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_feeds_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_feed_row(item))
    return table_output

def transform_feed_table_output(result):
    table_output = [_transform_feed_row(result)]
    return table_output


def _transform_feed_row(row):
    table_row = OrderedDict()
    table_row['Name'] = row['name']
    table_row['Description'] = row['description']

    if row['hideDeletedPackageVersions']:
        table_row['Hide Deleted Package Versions'] = 'True'
    else:
        table_row['Hide Deleted Package Versions'] = 'False'

    return table_row
