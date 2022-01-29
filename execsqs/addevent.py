from execsqs.models import TraceEvent


def add_event(event, context):
    event_string = {
        "event": event,
        "context": context
    }
    event_string = str(event_string)
    print(event_string)
    TraceEvent.objects.create(eventstring=event_string)

    return
