from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students # model ta niye asha. mane kun model er serialization korbo seta
        fields = '__all__'
    # কাস্টম ভ্যালিডেশন (Validation)
    def validate_age(self,value): # er moddhe integer field er value k condition diye check kora
        if value < 18:
            raise serializers.ValidationError
        return value