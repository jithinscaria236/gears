#!/usr/bin/env python
##########################################################################
# Simple library to convert list of dictionaries into ASCII table
#-------------------------------------------------------------------------
# Dependencies:
#   - None
#-------------------------------------------------------------------------
# Author: Jayan <jayanatl@gmail.com>
#-------------------------------------------------------------------------
# Modifications:
#   12SEP2019:Jayan
#       +Examples
#-------------------------------------------------------------------------
# Copyright (c) 2019, Jayanatl@gmail.com.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################
import logging


class DictsToTable:
    def __init__(self, input={}):
        self.data = []
        self.header_width = {}
        self.output_fields = []
        if isinstance(input, dict):
            self.add_row(input)
        elif isinstance(input, list):
            [self.add_row(item) for item in input]
        else:
            raise ValueError(f"Invalid input")

    def set_output_fields(self, fields=[]):
        '''Use this method to set fields you want in your output and order in which they should be listed'''
        if not isinstance(fields, list):
            raise ValueError(f"Input to this function must be a list of fields")
        self.output_fields = fields

    def add_row(self, d):
        '''Function to add a row represented as a dictionary'''
        if not isinstance(d, dict):
            raise ValueError(f"This function excepts dictionary as input")

        # Ensure keys and values are always string
        d = {str(k): str(v) for k, v in d.items()}

        # Calculate width of each field
        for k, v in d.items():
            try:
                if self.header_width[k] < len(v):
                    self.header_width[k] = len(v)
            except KeyError as err:
                logging.debug(f"Looks like we found a new field: {err}")
                self.header_width[k] = len(k) if len(k) > len(v) else len(v)
        self.data.append(d)

    def __generate_output(self):
        fields = self.output_fields if self.output_fields else self.header_width.keys()
        list_of_list = []

        # Generating rows for output
        # Add '---' if value for a column is missing
        line = " | ".join([f"{field:{self.header_width.get(field, len(field))}s}" for field in fields])
        line = f"| {line} |"
        list_of_list.append(line)
        for row in self.data:
            line = " | ".join([f"{row.get(field, '-' * self.header_width.get(field, len(field))):{self.header_width.get(field, len(field))}s}" for field in fields])
            line = f"| {line} |"
            list_of_list.append(line)

        # Beautify
        separator = "-+-".join([f"{'-' * self.header_width.get(field, len(field))}" for field in fields])
        separator = f"+-{separator}-+"
        list_of_list.insert(0, separator)
        list_of_list.insert(2, separator)
        list_of_list.append(separator)

        return list_of_list

    def __str__(self):
        return "\n".join(self.__generate_output())

    __repr__ = __str__


if __name__ == "__main__":
    '''Few examples on how to use this'''
    table1 = DictsToTable()
    table1.add_row({"acc": "1", "own": "jay"})
    table1.add_row({"acc": "2", "own": "ann"})
    print(table1)
    table1.set_output_fields(['own', 'acc'])
    print(table1)
    table1.set_output_fields(['in', 'valid', 'fields'])
    print(table1)
    table1.set_output_fields(['own', 'choo', 'acc', 'eehaa'])
    table1.add_row({"name": "jay", "comp": "reancloud"})
    print(table1)
    table1.set_output_fields([])
    print(table1)

    print("\n".join([
        "",
        "Another object",
        f"{'-' * 40}"
    ]))
    data = [
        {"Name": "Jayan", "Project": "ABC"},
        {"Name": "Venu", "Project": "ABC"},
        {"Name": "Srikumar", "Project": "XYZ"}
    ]

    table2 = DictsToTable(data)
    print(table2)
