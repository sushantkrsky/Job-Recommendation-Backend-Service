from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile, JobPosting
from .serializers import UserProfileSerializer, JobPostingSerializer
from .utils import recommend_jobs

@api_view(['POST'])
def get_recommended_jobs(request):
    # Parse user profile data from the request
    user_profile_data = request.data
    user_profile_serializer = UserProfileSerializer(data=user_profile_data)

    if user_profile_serializer.is_valid():
        user_profile = user_profile_serializer.validated_data
        
        # Ensure the preferences are correctly structured
        preferences = user_profile.pop('preferences')  # This removes 'preferences' from user_profile
        user_profile['desired_roles'] = preferences['desired_roles']
        user_profile['locations'] = preferences['locations']
        user_profile['job_type'] = preferences['job_type']

        job_postings = JobPosting.objects.all()

        # Use the recommendation logic to get matching jobs
        recommended_jobs = recommend_jobs(user_profile, job_postings)

        # Serialize the recommended job postings
        recommended_jobs_serialized = JobPostingSerializer(recommended_jobs, many=True)
        return Response(recommended_jobs_serialized.data)

    return Response(user_profile_serializer.errors)
