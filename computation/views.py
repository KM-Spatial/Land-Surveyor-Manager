from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from computation.forms import PolarForm, JoinForm
from computation.utils import calculate_polar, calculate_join
from .models import Join, Polar, Traverse, LevelingProject, LevelingReading

# default python 
import math 
import json 
from decimal import Decimal 

def calculate_traverse_southern_hemisphere(start_latitude, start_longitude, distances, angles):
    # TODO: FIX THIS FORMULA SO THAT IT CALCULATES SOMETHING 
    # Constants for earth's radius and degrees to radians conversion
    EARTH_RADIUS = 6371.01
    DEG_TO_RAD = math.pi / 180

    # Converting initial latitude and longitude to radians
    lat1 = start_latitude * DEG_TO_RAD
    lon1 = start_longitude * DEG_TO_RAD

    # Lists to store intermediate latitude and longitude values
    latitude = [start_latitude]
    longitude = [start_longitude]

    # Loop through the distances and angles
    for distance, angle in zip(distances, angles):
        # Converting angle to radians
        angle_rad = angle * DEG_TO_RAD

        # Calculating end latitude and longitude
        lat2 = math.asin(math.sin(lat1) * math.cos(distance/EARTH_RADIUS) +
                         math.cos(lat1) * math.sin(distance/EARTH_RADIUS) * math.cos(angle_rad))
        lon2 = lon1 + math.atan2(math.sin(angle_rad) * math.sin(distance/EARTH_RADIUS) * math.cos(lat1),
                                 math.cos(distance/EARTH_RADIUS) - math.sin(lat1) * math.sin(lat2))

        # Adding end latitude and longitude to lists
        latitude.append(lat2 * 180 / DEG_TO_RAD)
        longitude.append(lon2 * 180 / DEG_TO_RAD)

        # Updating lat1 and lon1 with end latitude and longitude
        lat1 = lat2
        lon1 = lon2

    return latitude, longitude



class ComputationHome(TemplateView):
    template_name = 'computation/computation_home.html'


class IntersectionResectionHome(TemplateView):
    template_name = 'computation/intersection_resection_home.html'

def resection_three_points_2(request):
    return render(request, 'computation/resection_three_point_p2.html')


class CogoIntroduction(LoginRequiredMixin, TemplateView):
    template_name = 'computation/cogo_landing.html'

class Cogo(LoginRequiredMixin, TemplateView):
    template_name = 'computation/cogo.html'


def join_computation(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            return calculate_join(request, form)
    else:
        form = JoinForm

    context = {
        'form': form,
    }

    return render(request, 'computation/join.html', context)


def polar_computation(request):
    if request.method == 'POST':
        form = PolarForm(request.POST)
        if form.is_valid():
            return calculate_polar(request, form)
    else:
        form = PolarForm()

    context = {
        'form': form,
    }

    return render(request, 'computation/polar.html', context)


class ComputationsDataHome(TemplateView):
    template_name = 'computation/computation_data_home.html'


class JoinDataList(LoginRequiredMixin, ListView):
    model = Join
    context_object_name = 'join_data'
    template_name = 'computation/join_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Join.objects.filter(user=current_user)


class PolarDataList(LoginRequiredMixin, ListView):
    model = Join
    context_object_name = 'polar_data'
    template_name = 'computation/polar_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Polar.objects.filter(user=current_user)


def traverse(request):
    if request.method == 'POST':
        traverse_name = request.POST.get('traverse_name')
        start_latitude = float(request.POST.get('start_latitude'))
        start_longitude = float(request.POST.get('start_longitude'))
        distances = request.POST.getlist('distance')
        angles = request.POST.getlist('angle')

        # Calculate the traverse for the Southern Hemisphere
        end_lat, end_lon = calculate_traverse_southern_hemisphere(start_latitude, start_longitude, distances, angles)
        
        average_end_lat = sum(end_lat)/len(end_lat)
        average_end_lon = sum(end_lon)/len(end_lon)

        # Store the results in the model
        traverse = Traverse.objects.create(
            traverse_name=traverse_name,
            start_latitude=start_latitude,
            start_longitude=start_longitude,
            distance=','.join(distances),
            angle=','.join(angles),
            end_lat=average_end_lat,
            end_lon=average_end_lon
        )
        context = {
            'end_lat': end_lat,
            'end_lon': end_lon,
        }


        return render(request, 'computation/traverse_computation.html', context)
    else:
        return render(request, 'computation/traverse_computation.html')
    
    

@login_required  
def leveling(request):
    projects = LevelingProject.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'computation/leveling.html', {
        'projects': projects
        })

@login_required
@require_http_methods(['POST'])
def save_leveling(request):
    # TODO: A lot of stuff needs fixing here ==> Cannot save the records to the DB 
    try:
        data = json.loads(request.body)
        project_name = data.get('project_name')
        readings = data.get('readings', [])
        initial_rl = data.get('initial_rl')
        final_rl = data.get('final_rl')

        if not project_name or not readings:
            return JsonResponse({
                'success': False,
                'error': 'Missing required data'
            }, status=400)

        # Create new project
        project = LevelingProject.objects.create(
            user=request.user,
            project_name=project_name,
            initial_rl=Decimal(str(initial_rl)),
            final_rl=Decimal(str(final_rl))
        )

        # Save readings in bulk
        bulk_readings = []
        for index, reading in enumerate(readings):
            bulk_readings.append(
                LevelingReading(
                    project=project,
                    station=reading['station'][:50],  # Limit string length
                    bs=Decimal(str(reading['bs'])) if reading.get('bs') else None,
                    is_sight=Decimal(str(reading['is'])) if reading.get('is') else None,
                    fs=Decimal(str(reading['fs'])) if reading.get('fs') else None,
                    rise=Decimal(str(reading['rise'])) if reading.get('rise') else None,
                    fall=Decimal(str(reading['fall'])) if reading.get('fall') else None,
                    rl=Decimal(str(reading['rl'])),
                    remarks=reading.get('remarks', '')[:200],  # Limit string length
                    reading_order=index
                )
            )

        LevelingReading.objects.bulk_create(bulk_readings)
        
        return JsonResponse({
            'success': True,
            'project_id': project.id
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

@login_required
def load_leveling(request, project_id):
    project = get_object_or_404(LevelingProject, id=project_id, user=request.user)
    readings = project.readings.all().values()
    return JsonResponse({
        'project_name': project.project_name,
        'initial_rl': str(project.initial_rl),
        'final_rl': str(project.final_rl),
        'readings': list(readings)
        })