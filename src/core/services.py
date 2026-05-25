from core.models import ServiceRequestBodyExample


def core_service_call(requestBody: ServiceRequestBodyExample) -> str:
    greeting = "Greetings, "
    title = requestBody.title
    name = requestBody.name

    if requestBody.is_doctor and not title:
        title = "Dr."
    if not name:
        name = title.lower().rstrip(".") if title else "friend"
    if title:
        greeting += f"{title} "
    greeting += f"{name}!"
    return "\n".join([greeting] * requestBody.count)
