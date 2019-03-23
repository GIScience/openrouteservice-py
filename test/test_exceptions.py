from openrouteservice.exceptions import ValidationError, ApiError, \
    HTTPError, Timeout, _RetriableRequest, _OverQueryLimit

import test as _test

from pprint import pprint


class ExceptionTest(_test.TestCase):

    def test_ValidationError(self):
        exception = ValidationError('hamspam')

        pprint(exception.__dict__)
        self.assertIsInstance(exception, Exception)

    def test_ApIError(self):
        exception = ApiError(500, 'hamspam')

        pprint(exception.__dict__)

        self.assertEqual(exception.status, 500)
        self.assertEqual(exception.message, 'hamspam')

        self.assertEqual(str(exception), '500 (hamspam)')

        exception = ApiError(500)

        self.assertEqual(str(exception), '500')

    def test_HTTPError(self):
        exception = HTTPError(500)

        self.assertEqual(exception.status_code, 500)

        self.assertEqual(str(exception), 'HTTP Error: 500')

    def test_Timeout(self):
        exception = Timeout()

        self.assertIsInstance(exception, Exception)

    def test_RetriableRequest(self):
        exception = _RetriableRequest()

        self.assertIsInstance(exception, Exception)

    def test_OverQueryLimit(self):
        exception = _OverQueryLimit(500, 'hamspam')

        self.assertIsInstance(exception, Exception)
        self.assertIsInstance(exception, ApiError)
        self.assertIsInstance(exception, _RetriableRequest)

        self.assertEqual(str(exception), '500 (hamspam)')
