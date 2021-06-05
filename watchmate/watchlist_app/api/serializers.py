from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review



class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"  


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True) 
    class Meta:
        model = WatchList
        fields = "__all__"



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
      



# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     descriptions = serializers.CharField()
#     active = serializers.BooleanField()

#     class Meta:
#         model = WatchList
#         fields = ['id','name','descriptions','active']

# def create(self, validated_data):
#     return Movie.objects.create(**validated_data) 

# def update(self, instance, validated_data):
#     instance.name = validated_data.get('name',instance.name)
#     instance.descriptions = validated_data.get('descriptions',instance.descriptions)
#     instance.active =validated_data.get('active',instance.active)
#     instance.save()
#     return instance    

#     # def validate_name(self,value):
#     #     if len(value) < 2:

#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value    
   
#     def validate(self,data):
#         if data['name'] == data['descriptions']:
#             raise serializer.ValidationError('Name not found')
#         else:
#             return data    
        
    
