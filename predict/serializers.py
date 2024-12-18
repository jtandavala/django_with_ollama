from rest_framework import serializers


class PredictionSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=10000)

    def validate_input(self, value):
        return value.strip()
