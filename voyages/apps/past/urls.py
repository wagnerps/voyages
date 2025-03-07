from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView

import voyages.apps.past.views
import voyages.apps.static_content.views

urlpatterns = [
    url(r'^api/search',
        voyages.apps.past.views.search_enslaved, name='search'),
    url(r'^api/modern-countries',
        voyages.apps.past.views.get_modern_countries,
        name='modern-countries'),
    url(r'^api/language-groups',
        voyages.apps.past.views.get_language_groups,
        name='language-groups'),
    url(r'^database/(?P<dataset>[\w\-]+)',
        voyages.apps.past.views.enslaved_database,
        name='database'),
    url(r'^database',
        voyages.apps.past.views.enslaved_database,
        name='database'),
    url(r'^contribute/(?P<id>.*)',
        TemplateView.as_view(template_name='past/contribute.html'),
        name='contribute'),
    url(r'^enslaved_contribution',
        voyages.apps.past.views.enslaved_contribution),
    url(r'^store-audio/(?P<contrib_pk>[0-9]+)/'
        r'(?P<name_pk>[0-9]+)/(?P<token>.*)',
        voyages.apps.past.views.store_audio),
    url(r'enslaved-filtered-places',
        voyages.apps.past.views.get_enslaved_filtered_places,
        name='enslaved-filtered-places')
]
