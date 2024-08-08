from apps.core.utils.image import upload_to


def custom_company_upload_to(obj, filename):
    upload = upload_to("company")
    return upload(obj, filename)

