from rest_framework import serializers
from rdiapp.models import *
from django.apps import apps



class TeacherSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Teacher
        fields = ['__all__','projects']


class StudentSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Application.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Application
        fields = ['__all__','Applications']        



def generate_serializers():
    app_models = apps.get_app_config('rdiapp').get_models()
    serializers_dict = {}

    for model in app_models:
        if ({model.__name__} not in ("Teacher","Student")):
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

