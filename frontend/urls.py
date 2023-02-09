from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('perfil', views.perfil, name='perfil'),
    path('historia', views.historia, name='historia'),
    path('estrategia', views.estrategia, name='estrategia'),
    path('equipo-directivo', views.equipo_directivo, name='equipo-directivo'),

    path('propiedades', views.propiedades, name='propiedades'),
    path('inversionistas', views.inversionistas, name='inversionistas'),

    path('resultados-trimestrales', views.resultados_trimestrales, name='resultados-trimestrales'),
    path('resultados-anuales', views.resultados_anuales, name='resultados-anuales'),
    path('preguntas-frecuentes', views.preguntas_frecuentes, name='preguntas-frecuentes'),
    path('glosario', views.glosario, name='glosario'),
    path('sala-prensa', views.sala_prensa, name='sala-prensa'),
    path('documentos-relevantes', views.documentos_relevantes, name='documentos-relevantes'),

    path('comite-tecnico', views.comite_tecnico, name='comite-tecnico'),
    path('otros-comites', views.otros_comites, name='otros-comites'),
    path('principales-tenedores', views.principales_tenedores, name='principales-tenedores'),
    path('estructura-corporativa', views.estructura_corporativa, name='estructura-corporativa'),
    path('auditor-externo', views.auditor_externo, name='auditor-externo'),

    path('cotizacion', views.cotizacion, name='cotizacion'),
    path('distribuciones-efectivo', views.distribuciones_efectivo, name='distribuciones-efectivo'),
    path('cobertura-analistas', views.cobertura_analistas, name='cobertura-analistas'),
    path('deuda', views.deuda, name='deuda'),
    path('prospectos', views.prospectos, name='prospectos'),

    path('sustentabilidad', views.sustentabilidad, name='sustentabilidad'),

    path('contacto', views.contacto, name='contacto'),
    path('denuncia', views.denuncia, name='denuncia'),
    path('send-denuncia', views.send_denuncia, name='send-denuncia'),
    path('send-mail-contact', views.send_mail_contact, name='send-mail-contact'),
    path('resultados', views.resultados, name='resultados'),
    path('send-subscription', views.send_subscription, name='send-subscription'),
]
