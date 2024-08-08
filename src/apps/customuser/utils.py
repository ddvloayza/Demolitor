from apps.core.utils.image import upload_to


def custom_user_upload_to(obj, filename):
    upload = upload_to("customuser")
    return upload(obj, filename)



