from .exceptions import BadUserDataException, BadUserConfigurationException
from sparkmagic.utils.constants import AUTHS_SUPPORTED


class Endpoint(object):
    def __init__(self, url, auth, username="", password="", kerberos_principal="", implicitly_added=False):
        if not url:
            raise BadUserDataException(u"URL must not be empty")
        if auth not in AUTHS_SUPPORTED:
            raise BadUserConfigurationException(u"Auth '{}' not supported".format(auth))
        
        self.url = url.rstrip(u"/")
        self.username = username
        self.password = password
        self.kerberos_principal = kerberos_principal
        self.auth = auth
        # implicitly_added is set to True only if the endpoint wasn't configured manually by the user through
        # a widget, but was instead implicitly defined as an endpoint to a wrapper kernel in the configuration
        # JSON file.
        self.implicitly_added = implicitly_added

    def __eq__(self, other):
        if type(other) is not Endpoint:
            return False
        return self.url == other.url and self.username == other.username and self.password == other.password and self.auth == other.auth and self.kerberos_principal == other.kerberos_principal

    def __hash__(self):
        return hash((self.url, self.username, self.password, self.auth, self.kerberos_principal))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return u"Endpoint({})".format(self.url)
