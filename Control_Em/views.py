from Control_G.models import Ganado
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import serializers, status
from django.utils.decorators import method_decorator


from Control_Em.serializer import Tacto_Serializers , Empadre_Serializers
from Control_Em.models import Control_Empadre , Tacto


#------------ VIEWS PARA EMPADRE ------------------
#TRAE TODOS LOS EMPADRES
class Empadre_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Control_Empadre.objects.all().order_by("id")
            serializer = Empadre_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(status = status.HTTP_400_BAD_REQUEST)


#TRAE EMPADRE POR ID
class Empadre_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Control_Empadre.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = Empadre_Serializers(queryset , many=True)
                    return Response(data= serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO EMPADRE
class Empadre_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        id_t = request.data["id_toro"] 
        id_v = request.data["vaca_id"]
        print("datos: " , request.data)
        try:
            topic_t = Ganado.objects.get(id=id_t)
            topic_v = Ganado.objects.get(id=id_v)
        except:
            print("fallo el topic")
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        cow_data = request.data
        cow_data["id_toro"] = topic_t
        cow_data["vaca_id"] = topic_v

        new_cow = Control_Empadre.objects.create(
            dia_servicio = cow_data["dia_servicio"],
            mes_servicio = cow_data["mes_servicio"],
            anio_servicio = cow_data["anio_servicio"],
            tipo_servicio = cow_data["tipo_servicio"],
            dia_gestacion = cow_data["dia_gestacion"],
            mes_gestacion = cow_data["mes_gestacion"],
            anio_gestacion = cow_data["anio_gestacion"],
            estado_servicio = cow_data["estado_servicio"],
            dia_prob_parto = cow_data["dia_prob_parto"],
            mes_prob_parto=  cow_data["mes_prob_parto"],
            anio_prob_parto = cow_data["anio_prob_parto"],
            id_toro = cow_data["id_toro"],
            vaca_id = cow_data["vaca_id"]
            )

        new_cow.save()
        serializer = Empadre_Serializers(new_cow)

        return Response(serializer.data , status= status.HTTP_201_CREATED)
    

#ACTUALIZA UN EMPADRE
class Empadre_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Control_Empadre.objects.get(id = id)
            serializer = Empadre_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN EMPADRE 
class Empadre_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Control_Empadre.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)




#----------------VIEWS PARA TACTO ----------------------
#TRAE TODOS LOS TACTOS
class Tacto_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Tacto.objects.all().order_by("id")
            serializer = Tacto_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE TACTO POR ID
class Tacto_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Tacto.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = Tacto_Serializers(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO TACTO
class Tacto_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        print("datos: " , request.data)

        id_t = request.data["id_empadre"] 
        try:
            topic_t = Control_Empadre.objects.get(id=id_t)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        cow_data = request.data
        cow_data["id_empadre"] = topic_t

        new_cow = Tacto.objects.create(
            detalle = cow_data["detalle"],
            hallazgo = cow_data["hallazgo"],
            id_empadre = cow_data["id_empadre"]
        )

        new_cow.save()
        serializer = Tacto_Serializers(new_cow)
        return Response(serializer.data , status= status.HTTP_201_CREATED)


#ACTUALIZA UN TACTO
class Tacto_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Tacto.objects.get(id = id)
            serializer = Tacto_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN GANADO 
class Tacto_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Tacto.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)