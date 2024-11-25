from django.db import models
import re

class HEXColorField(models.CharField):
    """
    Custom Django model field to store HEX color values.
    """

    def __init__(self, *args, **kwargs):
        # Limit the field to a valid HEX color code length (#RRGGBB or #RGB)
        kwargs['max_length'] = 7  # e.g., "#FFFFFF"
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        """
        Validate that the value is a valid HEX color.
        """
        super().validate(value, model_instance)
        hex_pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'  # Matches #RGB or #RRGGBB
        if not re.match(hex_pattern, value):
            raise ValueError(f"Invalid HEX color value: {value}")