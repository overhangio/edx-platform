from django.contrib.sessions.serializers import PickleSerializer


class PickleV2Serializer(PickleSerializer):
    """
    Lock the pickle serializer to version 2 of the protocol
    because we don't want python 2 to be able to read session
    data written by python3 while both are running at the same
    time in production.
    """

    protocol = 2
