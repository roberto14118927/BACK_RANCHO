from django.test import TestCase
from apps.Ganado.Control_Ganado.models import Raza, Ganado

#create raza
class RazaTestCase(TestCase):
    def setUp(self):
        Raza.objects.create(raza='Raza 1')
        
    def test_raza_create(self):
        raza = Raza.objects.get(raza='Raza 1')
        self.assertEqual(raza.raza, 'Raza 1')


#create ganado
class GanadoTestCase(TestCase):
    def setUp(self):
        Raza.objects.create(raza='Raza 1')
        ganado_uno = Ganado.objects.create(
            nombre='Ganado 1',
            sexo='M', 
            id_raza=Raza.objects.get(raza='Raza 1'),
            padre=None,
            madre=None,
            fecha_entrada_hato='05',
            estado='Saludable',
            condicion_estadia='Renta',
            comentarios=None,
            num_economico='1',
            num_registro='1',
            num_siniga='1',
            fecha_nacimiento='05',
            #test jsonfield
            info_ganado_externo={'madre': {'nombre': 'princesa',
                                            'raza': 'Suizo'},
                                 'padre': {'nombre': 'Nombre',
                                            'raza': 'Suizo'}}
            )
        ganado_dos = Ganado.objects.create(
            nombre='Ganado 2',
            sexo='H',
            id_raza=Raza.objects.get(raza='Raza 1'),
            padre=None,
            madre=None,
            fecha_entrada_hato='05',
            estado='Saludable',
            condicion_estadia='Renta',
            comentarios=None,
            num_economico='2',
            num_registro='2',
            num_siniga='2',
            fecha_nacimiento='05'
            )
        ganado_tres = Ganado.objects.create(
            nombre='Ganado 3',
            sexo='M',
            id_raza=Raza.objects.get(raza='Raza 1'),
            padre=Ganado.objects.get(nombre='Ganado 1'),
            madre=Ganado.objects.get(nombre='Ganado 2'),
            fecha_entrada_hato='05',
            estado='Saludable',
            condicion_estadia='Renta',
            comentarios=None,
            num_economico='3',
            num_registro='3',
            num_siniga='3',
            fecha_nacimiento='05'
            )
        ganado_uno.save()
        ganado_dos.save()
        ganado_tres.save()

        print(ganado_uno)
    
    def test_ganado_madre_padre(self):
        ganado = Ganado.objects.get(nombre='Ganado 3')
        self.assertEqual(ganado.padre.nombre, 'Ganado 1')
        self.assertEqual(ganado.madre.nombre, 'Ganado 2')
