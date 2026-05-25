from core.models import CLIStarterTemplate

def build_greeting(request: CLIStarterTemplate) -> str:
    greeting = "Greetings, "
    title = request.title
    name = request.name

    if request.is_doctor and not title:
        title = "Dr."
    if not name:
        name = title.lower().rstrip(".") if title else "friend"
    if title:
        greeting += f"{title} "
    greeting += f"{name}!"
    return "\n".join([greeting] * request.count)