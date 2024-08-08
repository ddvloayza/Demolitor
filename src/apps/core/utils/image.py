from os import path
from uuid import uuid4

from django.utils.text import slugify

IMAGE_TYPES_ALLOWED = [".png", ".jpg", ".jpeg"]
IMAGE_PREFIX_TEST = "finniu/images"
IMAGE_PREFIX = "images" if not IMAGE_PREFIX_TEST else IMAGE_PREFIX_TEST


def get_uuid(max_length=32):
    return str(uuid4()).replace("-", "")[:max_length]


def get_filename(obj, source, filename=None, auto_filename=False):
    if not auto_filename and filename:
        return slugify(path.splitext(filename)[0])

    if source:
        name = getattr(obj, source, get_uuid(8))
        return slugify(name)

    return get_uuid(8)


def get_ext(filename):
    return path.splitext(filename)[1]


def upload_to(identifier, source="slug", prefix=IMAGE_PREFIX):
    upload_path = "%s/%s/%s" % (prefix, identifier, get_uuid(8))
    return lambda obj, filename: "%s/%s%s" % (
        upload_path,
        get_filename(obj, source),
        get_ext(filename),
    )


def property_media_upload_to(obj, filename):
    upload = upload_to("property/images")
    return upload(obj, filename)


def report_file_upload_to(obj, filename):
    upload = upload_to("report/excel", prefix="report")
    return upload(obj, filename)
