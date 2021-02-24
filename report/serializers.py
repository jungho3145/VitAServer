from rest_framework import serializers

from report.models import reportLog


class reportLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = reportLog
        fields = "__all__"