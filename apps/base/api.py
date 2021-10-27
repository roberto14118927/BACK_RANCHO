from rest_framework import generics

class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all().filter(state = True).order_by("id")