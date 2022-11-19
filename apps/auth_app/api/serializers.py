from rest_framework import serializers

from django.contrib.auth import get_user_model


USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:

        model = USER
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()
    picture_thumb = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_picture_thumb(self, obj):
        try:
            return obj.picture_thumb.url
        except:
            return None

    class Meta:
        model = USER
        fields = ['picture_thumb', 'date_joined', 'email',
                  'is_active',  'full_name', 'last_login']