from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import pytz

def get_duration(visit):
    if (visit.leaved_at is not None):
        return visit.leaved_at - visit.entered_at
    return localtime() - visit.entered_at


def format_duration(duration):
    return str(duration).split(".")[0]


def create_non_closed_visit(visit):
    return {
        'who_entered': visit.passcard.owner_name,
        'entered_at': visit.entered_at,
        'duration': format_duration(get_duration(visit))
    }


def storage_information_view(request):
    non_closed_visits = [create_non_closed_visit(visit) for visit in Visit.objects.filter(leaved_at__isnull=True)]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
