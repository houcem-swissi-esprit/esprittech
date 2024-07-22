from rest_framework import serializers
from rdiapp.models import models
from django.apps import apps



def generate_serializers():
    app_models = apps.get_app_config('rdiapp').get_models()
    serializers_dict = {}

    for model in app_models:
        serializer_name = f"{model.__name__}Serializer"
        serializer_class = type(serializer_name, (serializers.ModelSerializer,), {
            "Meta": type("Meta", (), {
                "model": model,
                "fields": "__all__"
            })
        })
        serializers_dict[serializer_name] = serializer_class

    return serializers_dict

# Generate the serializers
generated_serializers = generate_serializers()

# Add the generated serializers to the global namespace
globals().update(generated_serializers)