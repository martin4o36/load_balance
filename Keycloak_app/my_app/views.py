from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import addEvent, removeEvent, addPerson, removePerson, getAllEvents

@csrf_exempt
def add_person(request):
    if request.method == 'POST':
        data = request.POST
        person = addPerson(
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password'),
            role=data.get('role')
        )
        return JsonResponse({"id": person.person_id}, status=201)
    

@csrf_exempt
def remove_person(request):
    if request.method == 'POST':
        data = request.POST
        removePerson(
            person_id=data.get('person_id'),
            username=data.get('username'),
            password=data.get('password')
        )
        return JsonResponse({"status": "Person removed"}, status=200)
    

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = request.POST
        event = addEvent(
            event_name=data.get('event_name'),
            event_date=data.get('event_date'),
            username=data.get('username'),
            password=data.get('password')
        )
        return JsonResponse({"id": event.event_id}, status=201)
    

@csrf_exempt
def remove_event(request):
    if request.method == 'POST':
        data = request.POST
        removeEvent(
            event_id=data.get('event_id'),
            username=data.get('username'),
            password=data.get('password')
        )
        return JsonResponse({"status": "Event removed"}, status=200)
    

@csrf_exempt
def get_all_events(request):
    if request.method == 'GET':
        try:
            events = getAllEvents()
            events_list = [{"id": event.event_id, "name": event.event_name, "date": event.date} for event in events]
            return JsonResponse({"events": events_list}, status=200)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)