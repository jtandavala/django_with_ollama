from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ollama import chat
from ollama import ChatResponse


from predict.serializers import PredictionSerializer


class PredictView(APIView):
    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_text = serializer.validated_data['input']

        response: ChatResponse = chat(
            model="phi3",
            messages=[
                {
                    "role": "user",
                    "content": input_text,
                },
            ],
            
        )
        print(response["message"]["content"])
        # or access fields directly from the response object
        print(response.message.content)

        # 

        # prediction = ollama_model.predict(input_text)

        return Response(
            {"prediction": response.message.content},
            status=status.HTTP_200_OK,
        )
