import os
import ConfigParser


class AWSCredentials:

    def __init__(self):
        self.filename = "credentials"
        self.directory = "~/.aws"
        self.full_path = ""
        self.creds_found = []

    def run(self):
        self.check_shared_creds_location()
        keys_from_env = self.check_env_vars()
        if keys_from_env:
            self.creds_found.append(keys_from_env)

        if os.path.exists(self.full_path) and os.path.getsize(self.full_path) > 0:
            profiles = self.check_creds_file()
            if profiles:
                for profile in profiles:
                    self.creds_found.append(profile)

    def check_shared_creds_location(self):
        if os.getenv('AWS_SHARED_CREDENTIALS_FILE'):
            self.full_path = os.path.expanduser(os.getenv('AWS_SHARED_CREDENTIALS_FILE'))
        else:
            self.full_path = os.path.expanduser(os.path.join(self.directory, self.filename))

    def check_env_vars(self):
        if os.getenv('AWS_ACCESS_KEY_ID') and os.getenv('AWS_SECRET_ACCESS_KEY'):
            values = {}
            values['profile_name'] = ""
            values['location'] = "Found in shell environment"
            values['aws_access_key_id'] = os.getenv('AWS_ACCESS_KEY_ID')
            values['aws_secret_access_key'] = os.getenv('AWS_SECRET_ACCESS_KEY')
            return values
        else:
            return None

    def check_creds_file(self):
        config = ConfigParser.RawConfigParser()
        config.read(self.full_path)
        profiles = []
        for section in config.sections():
            values = {}
            values['profile_name'] = section
            values['location'] = "Found in crentials file ({full_path})".format(full_path=self.full_path)
            values['aws_access_key_id'] = config.get(section, "aws_access_key_id")
            values['aws_secret_access_key'] = config.get(section, "aws_secret_access_key")
            profiles.append(values)
        return profiles

