# serializers.py

from rest_framework import serializers
from rest_framework.fields import empty
from .models import Person, Testemunho


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name"]


class TestemunhoSerializer(serializers.ModelSerializer):
    user = PersonSerializer()

    class Meta:
        model = Testemunho
        fields = ["id", "text", "year", "occupation", "user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["username"] = instance.user.name if instance.user else None
        del representation["user"]
        return representation

    def create(self, validated_data):
        user_data = validated_data.pop("user", None)
        person, _ = Person.objects.get_or_create(name=user_data.get("name"))

        # Create the Testemunho instance
        testemunho_instance = Testemunho.objects.create(user=person, **validated_data)

        return testemunho_instance
