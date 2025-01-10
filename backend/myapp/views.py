from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Login
from .serializers import RegisterSerializer, LoginSerializer,ProfileSerializer
from .models import Rating, Profile
from django.db.models import Avg
import os
from rest_framework import generics



class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Save the new user
        return Response({"message": "Registration successful", "data": serializer.data}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        try:
            user = Login.objects.get(username=username)
            if check_password(password, user.password):
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Login.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateRatingView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('worker_username')
        try:
            # Calculate the average rating for the worker
            average_rating = Rating.objects.filter(worker_username=username).aggregate(Avg('ratings'))['ratings__avg']
            if average_rating:
                # Update the Profile model with the average rating
                profile = Profile.objects.get(user__username=username)
                profile.rating = average_rating
                profile.save()

                return Response({"message": "Rating updated successfully", "average_rating": average_rating}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No ratings found for this worker"}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({"message": "Profile not found for this worker"}, status=status.HTTP_404_NOT_FOUND)

class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)

        profile_image = request.FILES.get('profile_image', None)

        # Handle profile image upload
        if profile_image:
            if instance.profile.profile_image:
                try:
                    os.remove(instance.profile.profile_image.path)
                except FileNotFoundError:
                    pass
            instance.profile.profile_image = profile_image

        # Update other fields
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response({"message": "Validation failed", "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)

        return Response({
            "message": "Profile updated successfully!",
            "user": {
                "username": instance.username,
                "name": instance.profile.name,
                "phone_number": instance.profile.phone_number,
                "age": instance.profile.age,
                "gender": instance.profile.gender,
                "address": instance.profile.address,
                "jobs_done": instance.profile.jobs_done,
                "reviews": instance.profile.reviews,
                "profile_image": build_image_url(instance.profile.profile_image),
            }
        }, status=status.HTTP_200_OK)
        
class ProfileFilterView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        worker_type = self.request.query_params.get('worker_type', None)
        if worker_type is not None:
            return Profile.objects.filter(worker_type=worker_type)
        return Profile.objects.all()