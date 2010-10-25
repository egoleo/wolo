from django.core.urlresolvers import reverse
from django.template.defaulfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Htt404, HttpResponseForbidden,HttpResponseServerError, HttpResponseRedirect

from contacts.models import Person, Group
from contacts.views import small_render_to_response
from contacts.forms import PersonCreateForm, PersonUpdateForm

def add(request, template_name='contacts/person/add.html'):
    user = request.user
    if not user.has_perm('add_person'):
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = PersonAddForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.slug = slugify("%s %s" % (p.first_name,p.last_name))
            p.save()
            return HttpResponseRedirect(p.get_absolute_url())

        else:
            return HttpResponseServerError

    context = {
        'form':PersonAddForm(request.POST)
    }

    return small_render_to_response(request, template_name, context)

