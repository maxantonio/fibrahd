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


# Nosotros
@gzip_page
def perfil(request):
    context = {
        'title': _("Perfil"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'perfil',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/perfil.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def historia(request):
    context = {
        'title': _("Historia"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'historia',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/historia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estrategia(request):
    context = {
        'title': _("Estrategia"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'estrategia',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/estrategia.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def equipo_directivo(request):
    context = {
        'title': _("Equipo directivo"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'equipo-directivo',
        'section': _('Nosotros')
    }
    return render(request, '{0}/frontend/nosotros/equipo_directivo.html'.format(request.LANGUAGE_CODE), context)


# Propiedades
@gzip_page
def propiedades(request):
    context = {
        'title': _("Propiedades"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'propiedades',
        'section': _('Propiedades')
    }
    return render(request, '{0}/frontend/propiedades.html'.format(request.LANGUAGE_CODE), context)


# Inversionistas
@gzip_page
def inversionistas(request):
    context = {
        'title': _("Inversionistas"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'inversionistas',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/inversionistas.html'.format(request.LANGUAGE_CODE), context)


# Financiera
@gzip_page
def resultados_trimestrales(request):
    context = {
        'title': _("Resultados trimestrales"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'resultados-trimestrales',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/resultados_trimestrales.html'.format(request.LANGUAGE_CODE),
                  context)


@gzip_page
def resultados_anuales(request):
    context = {
        'title': _("Resultados anuales"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'resultados-anuales',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/resultados_anuales.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def preguntas_frecuentes(request):
    context = {
        'title': _("Preguntas frecuentes"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'preguntas-frecuentes',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/preguntas_frecuentes.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def glosario(request):
    context = {
        'title': _("Glosario"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'glosario',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/glosario.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def glosario(request):
    context = {
        'title': _("Glosario"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'glosario',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/glosario.html'.format(request.LANGUAGE_CODE),
                  context)


@gzip_page
def sala_prensa(request):
    context = {
        'title': _("Sala de prensa"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'sala-prensa',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/sala_prensa.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def documentos_relevantes(request):
    context = {
        'title': _("Documentos relevantes"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'documentos-relevantes',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/financiera/documentos_relevantes.html'.format(request.LANGUAGE_CODE), context)


# Gobierno
@gzip_page
def comite_tecnico(request):
    context = {
        'title': _("Comité técnico"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'comite-tecnico',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/comite_tecnico.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def otros_comites(request):
    context = {
        'title': _("Otros comités"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'otros-comites',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/otros_comites.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def principales_tenedores(request):
    context = {
        'title': _("Principales tenedores"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'principales-tenedores',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/principales_tenedores.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def estructura_corporativa(request):
    context = {
        'title': _("Estructura corporativa"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'principales-tenedores',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/estructura_corporativa.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def auditor_externo(request):
    context = {
        'title': _("Auditor externo"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'auditor-externo',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/gobierno/auditor_externo.html'.format(request.LANGUAGE_CODE), context)


# Bursátil
@gzip_page
def cotizacion(request):
    context = {
        'title': _("Cotización"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'cotizacion',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/cotizacion.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def distribuciones_efectivo(request):
    context = {
        'title': _("Distribuciones de efectivo"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'distribuciones-efectivo',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/distribuciones_efectivo.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def cobertura_analistas(request):
    context = {
        'title': _("Cobertura de analistas"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'cobertura-analistas',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/cobertura_analistas.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def deuda(request):
    context = {
        'title': _("Deuda"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'deuda',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/deuda.html'.format(request.LANGUAGE_CODE), context)


@gzip_page
def prospectos(request):
    context = {
        'title': _("Prospectos"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'prospectos',
        'section': _('Inversionistas')
    }
    return render(request, '{0}/frontend/bursatil/prospectos.html'.format(request.LANGUAGE_CODE), context)


# Sustentabilidad
def sustentabilidad(request):
    context = {
        'title': _("Sustentabilidad"),
        'imagen': staticfiles_storage.url('images/header-preview2.png'),
        'page': 'sustentabilidad',
        'section': _('Sustentabilidad')
    }
    return render(request, '{0}/frontend/sustentabilidad/sustentabilidad.html'.format(request.LANGUAGE_CODE), context)


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
        [theme, 'it@irstrat.com', 'jsaucedag@elementia.com'],  # ['info@murano.com.mx',],
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
