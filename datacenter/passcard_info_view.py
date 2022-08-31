from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import date
from .storage_information_view import get_duration, format_duration
from django.utils.timezone import timedelta
from django.shortcuts import get_object_or_404, get_list_or_404


def is_visit_long(visit, minutes=60):
    return (get_duration(visit).total_seconds() / 60) > minutes


def create_this_passcard_visit(visit):
    return {
        'entered_at': visit.entered_at,
        'duration': format_duration(get_duration(visit)),
        'is_strange': is_visit_long(visit)
    }


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = [create_this_passcard_visit(visit) for visit in visits]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
