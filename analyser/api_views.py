from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ResumeSerializer
from .services.resume_parser import (
    extract_text,
    extract_email,
    extract_phone,
    extract_skills,
    calculate_score,
    extract_education,
    get_resume_status
)


class ResumeUploadAPIView(APIView):
    # def get(self, request):
    #     return Response({
    #         "status": "API Working"
    #     })
    #
    # def post(self, request):
    #     # existing code
    #     pass

    def post(self, request):
        serializer = ResumeSerializer(
            data=request.data
        )

        if serializer.is_valid():
            resume = serializer.save()

            text = extract_text(
                resume.resume_file.path
            )

            skills=extract_skills(text)
            score=calculate_score(skills)

            return Response({

                "email": extract_email(text),

                "phone": extract_phone(text),

                "education": extract_education(text),

                "skills": skills,

                "score":score,

                "status": get_resume_status(score)

            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )