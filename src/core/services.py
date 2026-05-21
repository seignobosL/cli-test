def build_greeting(
    name: str = "",
    title: str = "",
    doctor: bool = False,
    count: int = 1,
) -> str:
    greeting = "Greetings, "
    if doctor and not title:
        title = "Dr."
    if not name:
        name = title.lower().rstrip(".") if title else "friend"
    if title:
        greeting += f"{title} "
    greeting += f"{name}!"
    return "\n".join([greeting] * count)