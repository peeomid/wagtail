from __future__ import absolute_import, unicode_literals

import json

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.widgets import AdminChooser
from wagtail.wagtailimages.models import get_image_model


class AdminImageChooser(AdminChooser):
    choose_one_text = _('Choose an image')
    choose_another_text = _('Choose another image')
    clear_choice_text = _('Clear image')

    def __init__(self, **kwargs):
        super(AdminImageChooser, self).__init__(**kwargs)
        self.image_model = get_image_model()

    def render_html(self, name, value, attrs):
        original_field_html = super(AdminImageChooser, self).render_html(name, value, attrs)

        instance = self.get_instance(self.image_model, value)

        return render_to_string("wagtailimages/widgets/image_chooser.html", {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': value,
            'image': instance,
        })

    def render_js_init(self, id_, name, value):
        return "createImageChooser({0});".format(json.dumps(id_))
