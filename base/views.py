from base.utils import fetch_response
from base.serializers import StaffRecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import StaffRecords



# Create your views here.
class StaffReocrdAPIView(APIView):
    url_one = 'https://management-main.vercel.app/'
    url_two = 'https://servicemanagement.vercel.app/'
    """
        For Getting All Requests
    """
    def get(self, request, format=None):
        # Call the function 
        response = fetch_response(self.url_one, self.url_two)
        for data in response:
            del data['gender']
            del data['is_confirmed']
            del data['date_confirmed']
            del data['id']
            del data['HMO_number']
            
            try:
                StaffRecords.objects.create(**data)
            except: 
                pass
        
        staff_records = StaffRecords.objects.all()
        serializer =StaffRecordSerializer(staff_records, many=True)
        return Response(serializer.data, 200)

