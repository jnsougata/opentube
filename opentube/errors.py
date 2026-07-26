class TooManyRequests(Exception):
    """
    When too many requests are made to the YouTube API in a short period of time.
    """

    def __init__(self, message):
        self.message = message


class InvalidURL(Exception):
    """
    When invalid URL is provided.
    """

    def __init__(self, message):
        self.message = message


class RequestError(Exception):
    """
    When an error occurs while making a request.
    """

    def __init__(self, message):
        self.message = message
