
from rest_framework import serializers
import app.models as m

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = m.Restaurant
		fields =['name','description','cuisine','address','city','state','phoneNumber','startTime','endTime','monday','tuesday','wednesday','thursday','friday','saturday','sunday','delivers']
		