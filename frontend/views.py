from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_POST
from django.views.decorators.cache import cache_page
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import gettext as _
import requests


@gzip_page
# @cache_page(60 * 15)
def index(request):
    context = {
        'title': _("Inicio"),
        'page': 'index',
    }
    return render(request, '{0}/frontend/index.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def contacto(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/contacto-pic.png')
    else:
        imagen = staticfiles_storage.url('images/contact.png')

    context = {
        'title': _("Contacto"),
        'section': _('Contacto'),
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/contacto.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def responsabilidad(request):
    context = {
        'title': _("Responsabilidad_social"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/responsabilidad.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def acerca_de(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/header-nosotros.png')
    else:
        imagen = staticfiles_storage.url('images/about-us.png')

    context = {
        'title': _("Sobre nosotros"),
        'section': _('Perfil'),
        'page': "acerca-de",
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/nosotros/acerca_de.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def trayectoria(request):
    context = {
        'title': _("Nuestra trayectoria"),
        'section': _('Perfil'),
        'page': "trayectoria",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/trayectoria.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def cultura(request):
    context = {
        'title': _("Nuestra cultura"),
        'section': _('Perfil'),
        'page': "cultura",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/cultura.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def trabaja(request):
    context = {
        'title': _("Trabaja con Nosotros"),
        'section': _('Perfil'),
        'page': "cultura",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/trabaja.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def identidad(request):
    context = {
        'title': _("Nuestra identidad corporativa"),
        'section': _('Perfil'),
        'page': "identidad",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/identidad.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def negocios(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/header-nuestras-empresas-NEW.png')
    else:
        imagen = staticfiles_storage.url('images/our-companies.png')

    context = {
        'title': _("Nuestras Empresas"),
        'section': _('Perfil'),
        'page': "negocios",
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/nosotros/negocios.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def construsistemas(request):
    context = {
        'title': _("Construsistemas"),
        'section': _('Perfil'),
        'page': "construsistemas",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/construsistemas.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def proveedores(request):
    context = {
        'title': _("Proveedores"),
        'section': _('Proveedores'),
        'page': "proveedores",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/proveedores.html'.format(request.LANGUAGE_CODE), context)


def clientes(request):
    context = {
        'title': _("Clientes"),
        'section': _('Clientes'),
        'page': "clientes",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/clientes.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def funcionarios(request):
    context = {
        'title': _("Principales funcionarios"),
        'section': _('Perfil'),
        'page': "acerca-de",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/funcionarios.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def consejo_administracion(request):
    context = {
        'title': _("Consejo de administración"),
        'section': _('Perfil'),
        'page': "acerca-de",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/consejo_administracion.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def aspectos_destacados(request):
    context = {
        'title': _("Aspectos destacados"),
        'section': _('Perfil'),
        'page': "acerca-de",
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/aspectos_destacados.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def historia(request):
    context = {
        'title': _("Historia"),
        'section': _('Perfil'), 'sectionp': _('about'),
        'page': 'historia',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/historia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estrategia(request):
    context = {
        'title': _("Estrategia de negocio"),
        'section': _('Perfil'), 'sectionp': _('about'),
        'page': 'estrategia',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/estrategia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def alianzas(request):
    context = {
        'title': _("Alianzas estratégicas"),
        'section': _('Perfil'), 'sectionp': _('about'),
        'page': 'alianza',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/alianzas.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def panorama(request):
    context = {
        'title': _("Panorama"),
        'section': _('Perfil'), 'sectionp': _('about'),
        'page': 'panorama',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/nosotros/panorama.html'.format(request.LANGUAGE_CODE), context)


########### GOBIERNO COORPORATIVO ########
def directivos(request):
    context = {
        'title': _("Equipo directivo"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/directivos.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def compensacion(request):
    context = {
        'title': _("Plan de compensación"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/plan_compensacion.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def consejo(request):
    context = {
        'title': _("Consejo de administración"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/consejo.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def comites(request):
    context = {
        'title': _("Comites"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/comites.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estructura(request):
    context = {
        'title': _("Estructura_Corporativa"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/estructura.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def documentos(request):
    context = {
        'title': _("Documentos corporativos"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/documentos.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def esg(request):
    context = {
        'title': _("ESG"),
        'section': _('Gobierno_Corporativo'),
        'page': 'gobierno',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/gobierno/esg.html'.format(request.LANGUAGE_CODE), context)


########### informacion financiera ###########


def informacion(request):
    context = {
        'title': _("Informacion de la Deuda"),
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
            'message': message
        }
    )

    send_mail(
        'Usuario anónimo desea contactar con admin del sitio Elementia Materiales',
        '',
        'it@investorcloud.net',
        [theme,'it@irstrat.com','jsaucedag@elementia.com' ],  # ['info@murano.com.mx',],
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
        'page':'denuncia'
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


# @login_required
def cifras(request):
    context = {
        'title': _("Cifras_principales"),
        'section': 'infofinanciera',
        'page': 'cifras',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/cifras.html'.format(request.LANGUAGE_CODE), context)


def faq(request):
    context = {
        'title': _("Preguntas_frecuentes"),
        'section': 'infofinanciera',
        'page': 'faq',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/faq.html'.format(request.LANGUAGE_CODE), context)


def glosario(request):
    context = {
        'title': _("Glosario"),
        'section': 'infofinanciera',
        'page': 'glosario',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/glosario.html'.format(request.LANGUAGE_CODE), context)


def eventos(request):
    context = {
        'title': _("Documentos relevantes"),
        'section': 'infofinanciera',
        'page': 'eventos',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/eventos.html'.format(request.LANGUAGE_CODE), context)


def comunicados(request):
    if request.LANGUAGE_CODE == 'es':
        comunicados = requests.get(
            request._get_scheme() + '://' + request.get_host() + '/static/datos/comunicados.json').json()
    else:
        comunicados = requests.get(
            request._get_scheme() + '://' + request.get_host() + '/static/datos/comunicados_en.json').json()
    context = {
        'title': _("Eventos Relevantes"),
        'section': 'infofinanciera',
        'page': 'comunicados',
        'comunicados': comunicados,
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/comunicados.html'.format(request.LANGUAGE_CODE), context)


def proximos_eventos(request):
    context = {
        'title': _("Próximos eventos"),
        'section': 'infofinanciera',
        'page': 'proximos_eventos',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/proximos_eventos.html'.format(request.LANGUAGE_CODE), context)


def reportes(request):
    context = {
        'title': _("Reportes_de_resultados"),
        'section': 'infofinanciera',
        'page': 'reportes',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/reportes.html'.format(request.LANGUAGE_CODE), context)


def reportes_financieros(request):
    context = {
        'title': _("Reportes financieros"),
        'section': 'infofinanciera',
        'page': 'reportes_financieros',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/reportes_financieros.html'.format(request.LANGUAGE_CODE), context)


def conferencia(request):
    context = {
        'title': _("Conferencia Telefónica"),
        'section': 'infofinanciera',
        'page': 'conferencia',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/financiera/conferencia.html'.format(request.LANGUAGE_CODE), context)


#################informacion BURSATIL ##################
def asamblea(request):
    context = {
        'title': _("Asamblea de tenedores"),
        'section': 'infofinanciera',
        'page': 'reportes',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/asamblea.html'.format(request.LANGUAGE_CODE), context)


def accion(request):
    context = {
        'title': _("Información de la acción"),
        'section': 'Información para accionistas',
        'page': 'accion',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/accion.html'.format(request.LANGUAGE_CODE), context)


def historicos(request):
    context = {
        'title': _("Búsqueda de precios históricos"),
        'section': 'Información para accionistas',
        'page': 'historico',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/precios_historicos.html'.format(request.LANGUAGE_CODE), context)


def calculadora(request):
    context = {
        'title': _("Calculadora de rendimientos"),
        'section': 'Información para accionistas',
        'page': 'calculadora',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/calculadora.html'.format(request.LANGUAGE_CODE), context)


def cobertura(request):
    context = {
        'title': _("Cobertura de analistas"),
        'section': 'Información para accionistas',
        'page': 'cobertura',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/cobertura.html'.format(request.LANGUAGE_CODE), context)


def cerpis(request):
    context = {
        'title': _("Programa de CERPIs"),
        'section': 'infobursatil',
        'page': 'bursatil',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/cerpis.html'.format(request.LANGUAGE_CODE), context)


def administrador(request):
    context = {
        'title': _("administrador"),
        'section': 'infobursatil',
        'page': 'bursatil',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/administrador.html'.format(request.LANGUAGE_CODE), context)


def calificaciones(request):
    context = {
        'title': _("Colocaciones"),
        'section': 'infofinanciera',
        'page': 'reportes',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/calificaciones.html'.format(request.LANGUAGE_CODE), context)


def prospectos(request):
    context = {
        'title': _("Prospectos y documentos de emisión"),
        'section': 'infofinanciera',
        'page': 'reportes',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/bursatil/prospecto.html'.format(request.LANGUAGE_CODE), context)


def prensa(request):
    if request.LANGUAGE_CODE == 'es':
        comunicados = requests.get(
            request._get_scheme() + '://' + request.get_host() + '/static/datos/comunicados.json').json()
    else:
        comunicados = requests.get(
            request._get_scheme() + '://' + request.get_host() + '/static/datos/comunicados_en.json').json()
    context = {
        'title': _("SALA DE PRENSA"),
        'section': _("SALA DE PRENSA"),
        'page': 'prensa',
        'comunicados': comunicados,
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/prensa.html'.format(request.LANGUAGE_CODE), context)


##PORTAFOLIO
def concepto_plaza(request):
    context = {
        'title': _("Concepto Plaza Sendero"),
        'section': _("Portafolio"),
        'page': 'concepto plaza sendero',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/concepto_plaza.html'.format(request.LANGUAGE_CODE), context)


def resumen_operativo(request):
    context = {
        'title': _("Resumen operativo"),
        'section': _("Portafolio"),
        'page': 'Resumen operativo',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/resumen_operativo.html'.format(request.LANGUAGE_CODE), context)


def arrendatarios(request):
    context = {
        'title': _("Arrendatarios"),
        'section': _("Portafolio"),
        'page': 'Arrendatarios',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/arrendatarios.html'.format(request.LANGUAGE_CODE), context)


def propiedades(request):
    context = {
        'title': _("Portafolio_t"),
        'section': _("Portafolio"),
        'page': 'propiedades',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/propiedades.html'.format(request.LANGUAGE_CODE), context)


def anteriores(request):
    context = {
        'title': _("anteriores"),
        'section': _("Portafolio"),
        'page': 'propiedades',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/anteriores.html'.format(request.LANGUAGE_CODE), context)


def cancun(request):
    context = {
        'title': _("Grand Island Cancún I"),
        'section': _("Portafolio"),
        'page': 'cancun',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/cancun.html'.format(request.LANGUAGE_CODE), context)


def marina_vallarta(request):
    context = {
        'title': _("Marina Vallarta"),
        'section': _("Portafolio"),
        'page': 'marina-vallarta',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/marina-vallarta.html'.format(request.LANGUAGE_CODE), context)


def wyndham_condesa(request):
    context = {
        'title': _("Wyndham Grand Condesa"),
        'section': _("Portafolio"),
        'page': 'wyndham-condesa',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/wyndham-condesa.html'.format(request.LANGUAGE_CODE), context)


def cancun2(request):
    context = {
        'title': _("Grand Island Cancún II"),
        'section': _("Portafolio"),
        'page': 'cancun2',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/cancun2.html'.format(request.LANGUAGE_CODE), context)


def dreams(request):
    context = {
        'title': _("Dreams Chateau Baja"),
        'section': _("Portafolio"),
        'page': 'dreams',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/dreams.html'.format(request.LANGUAGE_CODE), context)


def parque(request):
    context = {
        'title': _("Baja Park"),
        'section': _("Portafolio"),
        'page': 'parque',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/portafolio/parque.html'.format(request.LANGUAGE_CODE), context)


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


def esg(request):
    context = {
        'title': _("ESG"),
        'section': _("ESG"),
        'page': 'esg',
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/esg.html'.format(request.LANGUAGE_CODE), context)


def sustentabilidad(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/header-sustentabilidad-NEW.png')
    else:
        imagen = staticfiles_storage.url('images/header-sustainability.png')

    context = {
        'title': _("Sustentabilidad"),
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/sustentabilidad/sustentabilidad.html'.format(request.LANGUAGE_CODE), context)


def que_es(request):
    context = {
        'title': _("¿Qué es?"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/sustentabilidad/que_es.html'.format(request.LANGUAGE_CODE), context)


def publicaciones(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/publicaciones-NEW.png')
    else:
        imagen = staticfiles_storage.url('images/releases.png')

    comunicados = [{
        "documento": "https://investorcloud.s3.amazonaws.com/corporativoelementia/ReportesAnuales/Informe-anual-2021.pdf",
        "titulo": "Informe Anual 2021",
        "titulo_en":"Annual Report 2021",
        "fecha": "05/05/2022",
    }]
    context = {
        'title': _("Publicaciones"),
        'comunicados': comunicados,
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/sustentabilidad/publicaciones.html'.format(request.LANGUAGE_CODE), context)


def grupos(request):
    context = {
        'title': _("Grupos de interes y materialidad"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/sustentabilidad/grupos.html'.format(request.LANGUAGE_CODE), context)


def desempeno_social(request):
    context = {
        'title': _("Desempeño Social"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/sustentabilidad/desempeno_social.html'.format(request.LANGUAGE_CODE), context)


def desempeno_ambiental(request):
    context = {
        'title': _("Desempeño Ambiental"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/sustentabilidad/desempeno_ambiental.html'.format(request.LANGUAGE_CODE),
                  context)

def resultados(request):
    context = {
        'title': _("Resultados"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
    }
    return render(request, '{0}/frontend/resultados.html'.format(request.LANGUAGE_CODE),
                  context)
def empleo(request):
    if request.LANGUAGE_CODE == 'es':
        imagen = staticfiles_storage.url('images/header-empleo-2.png')
    else:
        imagen = staticfiles_storage.url('images/careers.png')

    context = {
        'title': _("Empleo"),
        'imagen': imagen,
    }
    return render(request, '{0}/frontend/empleo.html'.format(request.LANGUAGE_CODE),
                  context)
