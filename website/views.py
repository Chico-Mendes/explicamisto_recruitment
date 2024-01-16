from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Testemunho, Person
from .serializers import TestemunhoSerializer, PersonSerializer


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        testemunho_instances = Testemunho.objects.all()
        testemunho_serializer = TestemunhoSerializer(testemunho_instances, many=True)

        occupations = Testemunho.OCCUPATIONS

        return render(
            request,
            self.template_name,
            {"listTestemunhos": testemunho_serializer.data, "occupations": occupations},
        )


@method_decorator(csrf_exempt, name="dispatch")
class TestemunhoListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Testemunho.objects.all()
        serializer = TestemunhoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)

        # Serialize and validate the Testemunho data
        serializer = TestemunhoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
