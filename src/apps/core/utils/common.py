import json
import logging
import os

from django.conf import settings

logger = logging.getLogger(__name__)


def get_message(origin):
    result = None
    try:
        _file = "src/apps/core/static/languages/messages_es.json"
        url = os.path.join(settings.PROJECT_ROOT, _file)

        with open(url) as data_file:
            data = json.load(data_file)
            result = data.get(origin, None)
            if result is not None:
                return result
    except Exception as e:
        logger.error("Error in get_message", str(e))
    return result
