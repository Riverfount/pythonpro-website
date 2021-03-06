from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pythonpro.mailchimp.facade import tag_as
from pythonpro.modules.facade import get_all_modules, get_module_with_contents


@login_required
def detail(request, slug):
    module = get_module_with_contents(slug)
    return render(request, 'modules/module_detail.html', {'module': module})


def index(request):
    return render(request, 'modules/module_index.html', context={'modules': get_all_modules()})


@login_required
def enrol(request, slug):
    module = get_module_with_contents(slug)
    tag_as(request.user.email, slug)
    return render(request, 'modules/module_enrol.html', {'module': module})
