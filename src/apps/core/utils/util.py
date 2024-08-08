import logging

import graphene

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def get_errors(e):
    """Get list of errors from dict.

    Args:
        e (dict): errors.

    Returns:
        List[str]: list of errors.

    """
    errors = []
    try:
        fields = e.message_dict.keys()
        messages = ["; ".join(m) for m in e.message_dict.values()]
        errors = [i for pair in zip(fields, messages) for i in pair]
        return errors
    except Exception as e:  # pylint: disable=broad-except,invalid-name
        errors.append(e.message)
        return errors


class MessageNode(graphene.ObjectType):
    """Message

    Attributes:
        field (str): field name.
        message (str): text of message.
        error_code (str): error code.

    """

    field = graphene.String()
    message = graphene.String()
    error_code = graphene.String()
