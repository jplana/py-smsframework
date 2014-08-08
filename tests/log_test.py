import unittest

from smsframework import Gateway
from smsframework.providers import LogProvider
from smsframework import OutgoingMessage

from testfixtures import log_capture

class LoopbackProviderTest(unittest.TestCase):
    """ Test LoopbackProvider """

    def setUp(self):
        self.gw = Gateway()
        # Providers
        self.gw.add_provider('main', LogProvider)


    @log_capture()
    def test_basic_send(self, l):
        msg = self.gw.send(OutgoingMessage('+1234', 'body'))
        l.check(
            ('smsframework.providers.log', 'INFO', 'Sent SMS to 1234: body'),
        )
