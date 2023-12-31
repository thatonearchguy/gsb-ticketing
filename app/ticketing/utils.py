import random
import re
from functools import wraps
from urllib.parse import urlparse

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, resolve_url

from .models import AllowedUser, UserKind


def login_required(
    view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='raven_login'
):
    @wraps(view_func)
    def _wrapper_view(request, *args, **kwargs):

        if request.user.is_authenticated:
            # ensure user has entered sign up details before proceeding
            if not request.user.has_signed_up and 'signup' not in request.path:
                # prevent infinite redirect loop
                return redirect('signup')
            return view_func(request, *args, **kwargs)

        # logic for guessing next redirect
        path = request.build_absolute_uri()
        resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
        # If the login url is the same scheme and net location then just
        # use the path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = request.get_full_path()
        from django.contrib.auth.views import redirect_to_login

        print(path, resolved_login_url, redirect_field_name)

        return redirect_to_login(path, resolved_login_url, redirect_field_name)

    return _wrapper_view


def match_identity(user, resp):
    # first match against our list of allowed users
    allowed_user = AllowedUser.objects.filter(username=user.username)
    if allowed_user.exists():
        return UserKind.objects.get(enum=allowed_user.first().userkind_enum)
    else:
        canceled = user.profile.raven_for_life
        # first, check R4L against jdCollege attribute
        if canceled and resp.get('college') == 'GIRTON':
            return UserKind.objects.get(enum="GIRTON_ALUM")
        groups = resp.get('groups', [])
        # match group, if any
        for group in groups:
            if group['groupid'] == '002866':
                return UserKind.objects.get(enum="GIRTON_UGRAD")
            elif group['groupid'] == '002880':
                return UserKind.objects.get(enum="GIRTON_PGRAD")
            elif group['groupid'] == '002836':
                return UserKind.objects.get(enum="GIRTON_STAFF")

        # if no match found, return other
        return UserKind.objects.get(enum="UCAM_OTHER")


def validate_ticket_ref(ref):
    return re.match(r"^GSB[A-Z1-9]{8}$", ref)
