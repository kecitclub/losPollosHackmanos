from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .models import Login, Profile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = Login.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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