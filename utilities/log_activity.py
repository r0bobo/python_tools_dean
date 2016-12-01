#!/usr/bin/env python3

import datetime
from python_tools_dean import conf_reader


class Log:
    """."""

    config_reader = []
    log_file = []
    html_file = []

    def __init__(self, log_file=None):
        """."""
        self.config_reader = conf_reader.ConfigReader()

        if log_file:
            self.log_file = log_file
        else:
            self.log_file = self.config_reader.get('activity_log')

    def write_log(self, script_name, successful):
        if successful:
            status = 'successfully finished'
        else:
            status = 'failed'

        message = '%s    %s: %s\n' % (datetime.datetime.now().strftime('%Y %b %d %H:%M:%S'), script_name, status)

        with open(self.log_file, 'a+') as f:
            f.write(message)

    def successful(self, script_name):
        self.write_log(script_name, True)

    def failed(self, script_name):
        self.write_log(script_name, False)

    def write_html(self, output_file=None):
        if output_file:
            self.html_file = output_file
        else:
            self.html_file = self.config_reader.get('html_log')
        convert_to_html(self.log_file, self.html_file) 

def convert_to_html(input_file, output_file):
    with open(output_file, 'w+') as outfile:
        outfile.write('<!DOCTYPE html>\n')
        outfile.write('<html>\n\n')
        outfile.write('<head>\n')
        outfile.write('    <title>Python Logs</title>\n\n')
        outfile.write('    <style>\n')
        outfile.write('        pre {\n')
        outfile.write('            color:gray\n')
        outfile.write('        }\n')
        outfile.write('    </style>\n')
        outfile.write('</head>\n\n')
        outfile.write('<body>\n')
        outfile.write('    <h1>Python Logs</h1>\n\n')
        outfile.write('    <hr>\n\n')
        outfile.write('    <pre>\n')
        outfile.write('        <samp>\n')

        with open(input_file, 'r') as input_file:
            for line in input_file:
                outfile.write('%s\n' % line.rstrip())

            outfile.write('        </samp>\n')
            outfile.write('    </pre>\n')
            outfile.write('</body>\n\n')
            outfile.write('</html>\n')
