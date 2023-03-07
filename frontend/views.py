import json
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_POST
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import gettext as _


@gzip_page
# @cache_page(60 * 15)
def index(request):
    context = {
        'title': _("Inicio"),
        'page': 'index',
    }
    return render(request, '{0}/frontend/index.html'.format(request.LANGUAGE_CODE), context)


# Nosotros
@gzip_page
def perfil(request):
    context = {
        'title': _("Perfil"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header_perfil.jpg'),
        'page': 'perfil',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/perfil.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def historia(request):
    context = {
        'title': _("Historia"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-estrategia.jpg'),
        'page': 'historia',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/historia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estrategia(request):
    context = {
        'title': _("Estrategia"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-estrategia.jpg'),
        'page': 'estrategia',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/estrategia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def equipo_directivo(request):
    context = {
        'title': _("Equipo directivo"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-equipodirectivo.jpg'),
        'page': 'equipo-directivo',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/equipo_directivo.html'.format(request.LANGUAGE_CODE), context)


# Propiedades
@gzip_page
def propiedades(request):
    context = {
        'title': _("Propiedades"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-propiedades.jpg'),
        'page': 'propiedades',
        'section': _('Propiedades')
    }
    return render(request, '{0}/frontend/propiedades/propiedades.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def descripcion(request, id):
    propiedades = {
        "1": {
            "titulo": "NAVE INDUSTRIAL VILLAHERMOSA",
            "descripcion": "Nave Industrial que tiene de inquilino a Grupo Elektra. Empresa de Grupo Salinas que brinda servicios financieros y de comercio especializado líder en Latinoamérica y el mayor proveedor de préstamos no bancarios de corto plazo en Estado Unidos.",
            "abr": "17,895",
            "pabr": "2.82",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/NaveIndustrial-Villahermosa-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/NaveIndustrial-Villahermosa-02.jpg',
                'images/fibrahd/propiedades/descripcion/NaveIndustrial-Villahermosa-05.jpg',
                'images/fibrahd/propiedades/descripcion/NaveIndustrial-Villahermosa-07.jpg']
        },
        "2": {
            "titulo": "NAVE INDUSTRIAL HEINEKEN",
            "descripcion": "",
            "abr": "5,942",
            "pabr": "0.94",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Heineken-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Heineken-02.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Heineken-03.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Heineken-04.jpg']
        },
        "3": {
            "titulo": "NAVE INDUSTRIAL VERITIV",
            "descripcion": "Nave destinada a la logística para la distribución de empaques, cartón y papel.",
            "abr": "4,645",
            "pabr": "0.73",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Veritv-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Veritv-03.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Veritv-05.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Veritv-04.jpg']
        },
        "4": {
            "titulo": "ENSAMBLES HYSON",
            "descripcion": "Nave Industrial destinada a ensambles de partes para equipo de riego.",
            "abr": "6,733",
            "pabr": "1.06",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ensambles-Hyson-05.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ensambles-Hyson-08.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ensambles-Hyson-06.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ensambles-Hyson-09.jpg']
        },
        "5": {
            "titulo": "SQM",
            "descripcion": "Aplicaciones a través de sus cinco líneas de negocio: Nutrición Vegetal de Especialidad, Yodo y derivados, Litio y derivados, Químicos Industriales y Potasio.",
            "abr": "11,255",
            "pabr": "1.77",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-SQM-Manzanillo-05.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-SQM-Manzanillo-06.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-SQM-Manzanillo-01.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-SQM-Manzanillo-03.jpg']
        },
        "6": {
            "titulo": "AEROESPACIAL DAHER",
            "descripcion": "Nave industrial destinada a la manufactura de partes de Aeronaves.",
            "abr": "6,141",
            "pabr": "0.97",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Aeroespacial-Daher-05.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Aeroespacial-Daher-03.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Aeroespacial-Daher-02.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Aeroespacial-Daher-07.jpg']
        },
        "7": {
            "titulo": "INDUSTRIAL ESQUIMAL",
            "descripcion": "Nave industrial destinada a la manufactura de colchas y edredones.",
            "abr": "12,786",
            "pabr": "2.01",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Esquimal-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Esquimal-05.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Esquimal-02.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Esquimal-03.jpg']
        },
        "8": {
            "titulo": "NAVE INDUSTRIAL TERNIUM",
            "descripcion": "",
            "abr": "7,395",
            "pabr": "1.16",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ternium-02.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ternium-01.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ternium-03.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Ternium-05.jpg']
        },
        "9": {
            "titulo": "YAZAKI",
            "descripcion": "Empresa que se dedica a la producción de cables en el sector automotriz. Tienen presencia en 46 países alrededor del mundo con un total de 258,300 empleados. Tecnología auto eléctrica de Durango produce piezas de plástico con y sin reforzamiento para el sector automotriz.",
            "abr": "21,709",
            "pabr": "3.42",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Durango-05.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Durango-07.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Durango-02.jpg',
                'images/fibrahd/propiedades/descripcion/Nave-Industrial-Durango-06.jpg']
        },
        "10": {
            "titulo": "PLAZA CARMEN CENTER",
            "descripcion": "Uno de los principales Centros Comerciales por su ubicación en Ciudad del Carmen. Entre sus principales inquilinos se encuentran: Sanborns, HSBC, Office Max, Santander y Big Bola.",
            "abr": "15,091",
            "pabr": "2.38",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-carmen-center-03.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-carmen-center-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-carmen-center-07.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-carmen-center-01.jpg']
        },
        "11": {
            "titulo": "PLAZA LOMAS VERDES",
            "descripcion": "Ubicado en una de las zonas de mayor dinamismo en Lomas Verdes muy bien comunicado y con facilidad de accesos y cómodo estacionamiento. Entre sus principales inquilinos se encuentran: Camarón Guasaveño, Barezzito y la Vid Argentina.",
            "abr": "5,863",
            "pabr": "0.92",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-lomas-verdes-07.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-lomas-verdes-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-lomas-verdes-05.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-lomas-verdes-11.jpg']
        },
        "12": {
            "titulo": "PLAZA PUNTO CHAPULTEPEC",
            "descripcion": "Parte de un importante desarrollo de usos mixtos en una zona corporativa de gran plusvalía de Guadalajara. Entre sus principales inquilinos se encuentran: CoLabora y Smart Fit.",
            "abr": "5,380",
            "pabr": "0.85",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-chapultepec-07.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-chapultepec-05.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-chapultepec-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-chapultepec-09.jpg']
        },
        "13": {
            "titulo": "PLAZA CATAVIÑA",
            "descripcion": "Ubicada en una de las principales intersecciones comerciales de la ciudad. Entre sus principales inquilinos se encuentran: DAX, Burger King, Farmacia Benavides.",
            "abr": "8,100",
            "pabr": "1.28",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-catavina-03.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-catavina-05.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-catavina-04.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-catavina-01.jpg']
        },
        "14": {
            "titulo": "PLAZA CASA GRANDE",
            "descripcion": "Ubicada en el corredor comercial más destacado de la ciudad de Saltillo. Entre sus principales inquilinos se encuentran: AT&T y Broxton.",
            "abr": "4,435",
            "pabr": "0.70",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-casa-grande-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-casa-grande-03.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-casa-grande-04.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-casa-grande-05.jpg']
        },
        "15": {
            "titulo": "PLAZA PUNTO MOCHIS",
            "descripcion": "Plaza ubicada en el epicentro de la actividad comercial de Los Mochis. Entre sus principales inquilinos se encuentran: Walmart, Starbucks, Carls Jr, Cinepolis y Parisina.",
            "abr": "22,753",
            "pabr": "3.58",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-monchis-08.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-monchis-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-monchis-09.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-punto-monchis-06.jpg']
        },
        "16": {
            "titulo": "PLAZA LA ROCA",
            "descripcion": "Ubicada en una de las zonas residenciales con mayor poder adquisitivo. Entre sus principales inquilinos se encuentran: Cinemex, Krispy Kreme, Santander, Scotiabank y CoLabora.",
            "abr": "7,011",
            "pabr": "1.10",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-la-roca-11.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-la-roca-12.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-la-roca-10.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-la-roca-05.jpg']
        },
        "17": {
            "titulo": "PLAZA LOS CORALES",
            "descripcion": "Ubicada en una avenida de alto flujo y a tan solo 3km de la zona portuaria de Veracruz. Entre sus principales inquilinos se encuentran: Parisina, Carl´s Jr, Office Depot e Interceramic.",
            "abr": "6,028",
            "pabr": "0.95",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-corales-03.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-corales-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-corales-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-corales-04.jpg']
        },
        "18": {
            "titulo": "PLAZA SAN ANTONIO",
            "descripcion": "Plaza de barrio ubicada alrededor de un gran sector residencial, característica que promete un potencial de plusvalía para el inmueble. Entre sus principales inquilinos se encuentran: 7eleven, Multifarmacias.",
            "abr": "1,902",
            "pabr": "0.30",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-parque-san-antonio-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-parque-san-antonio-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-parque-san-antonio-03.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-parque-san-antonio-04.jpg']
        },
        "19": {
            "titulo": "PORTAFOLIO STAND ALONE DE BURGER KING",
            "descripcion": "Portafolio de 4 propiedades stand alone. Ubicadas en las principales zonas comerciales de Tijuana, San Luis Río Colorado, Guaymas y Guasave.",
            "abr": "2,055",
            "pabr": "0.32",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-burger-king-09.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-burger-king-09.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-burger-king-07.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-burger-king-05.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-burger-king-04.jpg']
        },
        "20": {
            "titulo": "BARRIO REFORMA",
            "descripcion": "El inmueble se encuentra ubicado a unos metros de la zona financiera de Paseo de la Reforma en la Ciudad de México. Entre sus principales inquilinos se encuentran: Office Depot, Harmon Hall.",
            "abr": "2,130",
            "pabr": "0.34",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-barrio-reforma-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-barrio-reforma-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-barrio-reforma-03.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-barrio-reforma-04.jpg']
        },
        "21": {
            "titulo": "PLAZA CHIMALHUACÁN",
            "descripcion": "Uno de los principales Centros Comerciales en Chimalhuacán y de las zonas con mayor densidad en el Estado de México. Entre sus principales inquilinos se encuentran: Sears, Cinepolis, Famsa, Elektra, Recórcholis, Boss GYM y Coppel.",
            "abr": "31,204",
            "pabr": "4.92",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-chimalhuacan-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-chimalhuacan-05.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-chimalhuacan-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-chimalhuacan-07.jpg']
        },
        "22": {
            "titulo": "PLAZA PENINSULA",
            "descripcion": "Plaza Península está situado en San José del Cabo, Baja California Sur en un lugar privilegiado y estratégicamente ubicado. Su arquitectura y diseño abierto concuerda con el magnífico paisaje que le rodea. Entre sus principales inquilinos se encuentran: BBVA, Actinver, Office Max, Starbucks.",
            "abr": "7,183",
            "pabr": "1.13",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-peninsula-02.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-peninsula-04.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-peninsula-07.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-peninsula-05.jpg']
        },
        "23": {
            "titulo": "PLAZA VÍA SAN JUAN",
            "descripcion": "Una de las principales plazas en Iztapalapa y de las zonas con mayor densidad de la ciudad. Entre sus principales inquilinos se encuentran: Soriana, Bisquets de Obregon, Honda, Toyota, Cinemex y Dominos.",
            "abr": "14,363",
            "pabr": "2.26",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-via-san-juan-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-via-san-juan-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-via-san-juan-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-via-san-juan-05.jpg']
        },
        "24": {
            "titulo": "AGENCIA SUZUKI",
            "descripcion": "",
            "abr": "1,248",
            "pabr": "0.20",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-zuzuki-02.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-zuzuki-02.jpg']
        },
        "25": {
            "titulo": "PLAZA LA PILITA",
            "descripcion": "Centro Comercial ubicado a 5 minutos del centro de Metepec. Anclado por Soriana y Cinemex. Cuenta con gran variedad de servicios y un amplio estacionamiento para más de 330 autos. Entre sus principales clientes se encuentran: Coppel, Cinemex, Cash America y Calzado Andrea.",
            "abr": "6,450",
            "pabr": "1.02",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-plaza-pilita-04.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-plaza-pilita-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-pilita-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-plaza-pilita-03.jpg']
        },
        "26": {
            "titulo": "PORTAFOLIO OLAB",
            "descripcion": "",
            "abr": "3,519",
            "pabr": "0.55",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-olabs-03.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-olabs-01.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-olabs-02.jpg']
        },
        "27": {
            "titulo": "PORTAFOLIO BODEGA AURERA EXPRESS",
            "descripcion": "",
            "abr": "4,250",
            "pabr": "0.67",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-bodega-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-bodega-02.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-bodega-03.jpg',
                'images/fibrahd/propiedades/descripcion/comercial-portafolio-bodega-04.jpg']
        },
        "28": {
            "titulo": "UVM CAMPUS NOGALES",
            "descripcion": "",
            "abr": "3,995",
            "pabr": "0.63",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-uvm-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-uvm-05.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-uvm-06.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-uvm-02.jpg']
        },
        "29": {
            "titulo": "COLEGIO CELTA INTERNACIONAL",
            "descripcion": "Ubicada en uno de los nuevos polos de crecimiento del segmento de clase media alta de la zona metropolitana de Querétaro. Instalaciones de primer nivel.",
            "abr": "13,168",
            "pabr": "2.07",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-celta-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-celta-02.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-celta-04.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-celta-05.jpg']
        },
        "30": {
            "titulo": "COLEGIO MÉXICO NUEVO CAMPUS LA CALMA",
            "descripcion": "Institución educativa de alta calidad. Operada por un grupo de alto prestigio la cual ofrece atención desde prescolar hasta preparatoria.",
            "abr": "10,280",
            "pabr": "1.62",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-calma-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-calma-02.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-calma-06.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-calma-07.jpg']
        },
        "31": {
            "titulo": "IPETH",
            "descripcion": "Institución líder en la formación de fisioterapeutas a nivel nacional y más de 3 mil estudiantes.",
            "abr": "3,890",
            "pabr": "0.61",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-ipeth-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-ipeth-05.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-ipeth-06.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-ipeth-04.jpg']
        },
        "32": {
            "titulo": "COLEGIO TÉCNICO QUERÉTARO",
            "descripcion": "Inmueble de reciente construcción, ubicado en una zona de gran crecimiento comercial y de negocios. El inquilino del inmueble es la preparatoria Celta y carreras técnicas.",
            "abr": "4,076",
            "pabr": "0.64",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-queretaro-02.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-queretaro-08.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-queretaro-08.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-queretaro-08.jpg']
        },
        "33": {
            "titulo": "COLEGIO MÉXICO NUEVO CAMPUS QUERÉTARO",
            "descripcion": "Institución educativa de alta calidad. Operada por un grupo de alto prestigio la cual ofrece atención desde prescolar hasta preparatoria.",
            "abr": "3,706",
            "pabr": "0.58",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/educativo-campus-queretaro-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/educativo-campus-queretaro-02.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-campus-queretaro-03.jpg',
                'images/fibrahd/propiedades/descripcion/educativo-campus-queretaro-04.jpg']
        },
        "34": {
            "titulo": "CORPORATIVO GARZA SADA",
            "descripcion": "Ubicada en una de las zonas residenciales que albergan a los ejecutivos de las empresas más importantes de la región, así como comunicada con parques industriales, zonas de servicios financieros y administración pública.",
            "abr": "1,836",
            "pabr": "0.29",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-garza-sada-02.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-garza-sada-04.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-garza-sada-01.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-garza-sada-07.jpg']
        },
        "35": {
            "titulo": "SKY CUMBRES",
            "descripcion": "",
            "abr": "1,658",
            "pabr": "0.26",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-sky-cumbres-03.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-sky-cumbres-01.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-sky-cumbres-02.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-sky-cumbres-04.jpg']
        },
        "36": {
            "titulo": "CORPORATIVO BOSQUE REAL",
            "descripcion": "Inmueble destinado para el uso corporativo de un grupo desarrollador de naves industriales y vivienda en renta. Importante potencial de plusvalía a corto plazo por el crecimiento de la zona.",
            "abr": "1,530",
            "pabr": "0.24",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-real-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-real-02.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-real-03.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-real-04.jpg']
        },
        "37": {
            "titulo": "CORPORATIVO BOSQUES DE LAS LOMAS",
            "descripcion": "Inmueble destinado para el uso corporativo. Importante potencial de plusvalía dada su ubicación y la demanda de la zona.",
            "abr": "3,623",
            "pabr": "0.57",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-lomas-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-lomas-02.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-lomas-03.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-bosque-lomas-04.jpg']
        },
        "38": {
            "titulo": "CORPORATIVO PERIFÉRICO SUR",
            "descripcion": "Inmueble destinado para el uso corporativo de distintos grupos.",
            "abr": "3,938",
            "pabr": "0.62",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-sur-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-sur-02.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-sur-03.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-sur-04.jpg']
        },
        "39": {
            "titulo": "CORPORATIVO PERIFÉRICO NORTE",
            "descripcion": "Edificio de oficinas, con 4 niveles, ubicado sobre la lateral de periférico.",
            "abr": "2,941",
            "pabr": "0.46",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-norte-01.jpg'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-norte-02.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-norte-03.jpg',
                'images/fibrahd/propiedades/descripcion/oficinas-periferico-norte-04.jpg']
        },
        "40": {
            "titulo": "PLAZA LA CANTERA",
            "descripcion": "",
            "abr": "6,799",
            "pabr": "1.07",
            "fecha": "oct-2021",
            "header": staticfiles_storage.url(
                'images/fibrahd/propiedades/descripcion/fhd-plaza-la-cantera-05.png'),
            "imagenes": [
                'images/fibrahd/propiedades/descripcion/fhd-plaza-la-cantera-02.png',
                'images/fibrahd/propiedades/descripcion/fhd-plaza-la-cantera-03.png',
                'images/fibrahd/propiedades/descripcion/fhd-plaza-la-cantera-04.png']
        }
    }
    propiedad = propiedades[id]
    context = {
        'title': propiedad["titulo"],
        'imagen': propiedad["header"],
        'page': 'descripcion',
        'section': _('Propiedades'),
        'propiedad': propiedad
    }
    return render(request, '{0}/frontend/propiedades/descripcion.html'.format(request.LANGUAGE_CODE), context)


# Inversionistas
@gzip_page
def inversionistas(request):
    context = {
        'title': _("Inversionistas"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'inversionistas',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/inversionistas.html'.format(request.LANGUAGE_CODE), context)


# Financiera
@gzip_page
def resultados_trimestrales(request):
    context = {
        'title': _("Resultados trimestrales"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'resultados-trimestrales',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/resultados_trimestrales.html'.format(request.LANGUAGE_CODE),
                  context)


@gzip_page
def resultados_anuales(request):
    context = {
        'title': _("Resultados anuales"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'resultados-anuales',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/resultados_anuales.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def preguntas_frecuentes(request):
    context = {
        'title': _("Preguntas frecuentes"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'preguntas-frecuentes',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/preguntas_frecuentes.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def glosario(request):
    context = {
        'title': _("Glosario"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'glosario',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/glosario.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def sala_prensa(request):
    eventos = settings.BASE_DIR + '/frontend/static/datos/sala_prensa.json'
    eventos_json_data = open(eventos)
    eventos = json.load(eventos_json_data)

    context = {
        'title': _("Sala de prensa"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'sala-prensa',
        'section': _('Inversionistas'),
        'eventos': eventos
    }
    return render(request, '{0}/frontend/financiera/sala_prensa.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def documentos_relevantes(request):
    context = {
        'title': _("Documentos relevantes"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-financiera.jpg'),
        'page': 'documentos-relevantes',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/documentos_relevantes.html'.format(request.LANGUAGE_CODE), context)


# Gobierno
@gzip_page
def comite_tecnico(request):
    context = {
        'title': _("Comité técnico"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-gobierno-corporativo.jpg'),
        'page': 'comite-tecnico',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/comite_tecnico.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def otros_comites(request):
    context = {
        'title': _("Otros comités"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-gobierno-corporativo.jpg'),
        'page': 'otros-comites',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/otros_comites.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def principales_tenedores(request):
    context = {
        'title': _("Principales tenedores"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-gobierno-corporativo.jpg'),
        'page': 'principales-tenedores',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/principales_tenedores.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estructura_corporativa(request):
    context = {
        'title': _("Estructura corporativa"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-gobierno-corporativo.jpg'),
        'page': 'principales-tenedores',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/estructura_corporativa.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def auditor_externo(request):
    context = {
        'title': _("Auditor externo"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-gobierno-corporativo.jpg'),
        'page': 'auditor-externo',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/auditor_externo.html'.format(request.LANGUAGE_CODE), context)


# Bursátil
@gzip_page
def cotizacion(request):
    context = {
        'title': _("Cotización"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'cotizacion',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/cotizacion.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def distribuciones_efectivo(request):
    context = {
        'title': _("Distribuciones de efectivo"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'distribuciones-efectivo',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/distribuciones_efectivo.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def cobertura_analistas(request):
    context = {
        'title': _("Cobertura de analistas"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'cobertura-analistas',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/cobertura_analistas.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def deuda(request):
    context = {
        'title': _("Deuda"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'deuda',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/deuda.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def prospectos(request):
    context = {
        'title': _("Prospectos"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-informacion-bursatil.jpg'),
        'page': 'prospectos',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/prospectos.html'.format(request.LANGUAGE_CODE), context)


# Sustentabilidad
def sustentabilidad(request):
    context = {
        'title': _("Sustentabilidad"),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-sustentabilidad.jpg'),
        'page': 'sustentabilidad',
        'section': _('Sustentabilidad')
    }
    return render(request, '{0}/frontend/sustentabilidad/sustentabilidad.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def contacto(request):
    context = {
        'title': _("Contacto"),
        'section': _('Contacto'),
        'imagen': staticfiles_storage.url('images/fibrahd/headers/header-contacto.jpg'),
    }
    return render(request, '{0}/frontend/contacto.html'.format(request.LANGUAGE_CODE), context)


@require_POST
def send_mail_contact(request):
    context = {'title': 'Inicio'}
    name = request.POST['form_name']
    company = request.POST['form_company']
    email = request.POST['form_email']
    phone = request.POST['form_phone']
    country = request.POST['form_country']
    state = request.POST['form_state']
    theme = request.POST['form_theme']
    message = request.POST['form_message']

    html_message = loader.render_to_string(
        '{0}/frontend/emails/send_mail_contact.html'.format(request.LANGUAGE_CODE),
        {
            'name': name,
            'company': company,
            'email': email,
            'phone': phone,
            'country': country,
            'state': state,
            'theme': theme,
            'message': message
        }
    )

    send_mail(
        'Usuario anónimo desea contactar con admin del sitio Fibra HD',
        '',
        'it@investorcloud.net',
        ['it@irstrat.com', 'contacto@fibrahd.mx'],
        html_message=html_message
    )
    return JsonResponse({"success": "true"}, safe=False)


def denuncia(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/canal-denuncias.png')
    else:
        imagen = staticfiles_storage.url('images/whistleblower-channel.png')

    context = {
        'title': _("Canal de Denuncias"),
        'imagen': imagen,
        'page': 'denuncia'
    }
    return render(request, '{0}/frontend/denuncia.html'.format(request.LANGUAGE_CODE), context)


@require_POST
def send_denuncia(request):
    context = {'title': 'Inicio'}
    name = request.POST['form_name']
    company = request.POST['form_company']
    email = request.POST['form_email']
    phone = request.POST['form_phone']
    country = request.POST['form_country']
    state = request.POST['form_state']
    theme = request.POST['form_theme']
    message = request.POST['form_message']

    html_message = loader.render_to_string(
        '{0}/frontend/emails/send_mail_contact.html'.format(request.LANGUAGE_CODE),
        {
            'name': name,
            'company': company,
            'email': email,
            'phone': phone,
            'country': country,
            'state': state,
            'theme': theme,
            'message': message
        }
    )

    send_mail(
        'Usuario anónimo desea contactar con admin del sitio Fortaleza',
        '',
        'it@investorcloud.net',
        ['it@irstrat.com', ],  # ['info@murano.com.mx',],
        html_message=html_message
    )
    return JsonResponse({"success": "true"}, safe=False)


@require_POST
def send_subscription(request):
    context = {'title': 'Inicio'}
    email = request.POST['subscription']
    send_mail(
        'Usuario ' + email + ' desea subscribirse al  sitio Murano',
        'Usuario con email ' + email + " desea subscribirse",
        'it@irstrat.com',
        ['it@irstrat.com'],  # ['info@murano.com.mx','it@irstrat.com'],
    )
    return JsonResponse({"success": "true"}, safe=False)


@gzip_page
def resultados(request):
    context = {
        'title': _("Resultados"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/resultados.html'.format(request.LANGUAGE_CODE),
                  context)


@require_POST
def send_subscription(request):
    context = {'title': 'Inicio'}
    email = request.POST['subscription']
    send_mail(
        'Usuario ' + email + ' desea subscribirse al  sitio Murano',
        'Usuario con email ' + email + " desea subscribirse",
        'it@irstrat.com',
        ['it@irstrat.com'],  # ['info@murano.com.mx','it@irstrat.com'],
    )
    return JsonResponse({"success": "true"}, safe=False)
