from .models import Person, Role, Event
from .keycloak_services import verify_role, create_user_in_keycloak, authenticate_user, keycloak_admin


# Creates a user in keycloak too
def addPerson(username, email, first_name, last_name, password, role):
    if role != Role.ADMIN.value:
        raise ValueError("Incorrect person role.")
    
    roles = [role]
    user_id = create_user_in_keycloak(username, email, first_name, last_name, password, roles)
    person = Person.objects.create(
        person_id=user_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        role=role
    )

    return person


def getAllEvents():
    try:
        events = Event.objects.all()
        return events
    except Exception as e:
        raise ValueError(f"Error retrieving events: {str(e)}")


def removePerson(person_id, username, password):
    try:
        token = authenticate_user(username, password)
        if not verify_role(token, Role.ADMIN.value):
            raise PermissionError("User does not have permission to remove persons.")
        
        person = Person.objects.get(pk=person_id)
        keycloak_user_id = person.person_id
        person.delete()
        keycloak_admin.delete_user(keycloak_user_id)
    except Person.DoesNotExist:
        raise ValueError("Person not found.")
    except Exception as e:
        raise ValueError(f"Error removing person: {str(e)}")


# Authorize first in keycloak who does that
def addEvent(event_name, event_date, username, password):
    try:
        token = authenticate_user(username, password)
        if not verify_role(token, Role.ADMIN.value):
            raise PermissionError("User does not have permission to add events.")

        event = Event.objects.create(
            name = event_name,
            date = event_date
        )

        return event
    except Exception as e:
        raise ValueError(f"Error adding event: {str(e)}")
    

# Authorize first in keycloak who does that
def removeEvent(event_id, username, password):
    try:
        token = authenticate_user(username, password)
        if not verify_role(token, Role.ADMIN.value):
            raise PermissionError("User does not have permission to remove events.")
        
        event = Event.objects.get(pk=event_id)
        event.delete()
    except Event.DoesNotExist:
        raise ValueError("Event not found.")
    except Exception as e:
        raise ValueError(f"Error removing event: {str(e)}")