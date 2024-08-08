from apps.core.utils.image import upload_to


def custom_product_upload_to(obj, filename):
    upload = upload_to("product")
    return upload(obj, filename)

def custom_category_upload_to(obj, filename):
    upload = upload_to("category")
    return upload(obj, filename)
