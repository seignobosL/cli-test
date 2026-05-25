import typer
from typing_extensions import Annotated
from core.services import core_service_call
from core.models import ServiceRequestBodyExample


app = typer.Typer()


@app.command()
def greet(
    name: Annotated[
        str,
        typer.Argument(
            help="The (last, if --title is given) name of the person to greet")
    ] = "",
    title: Annotated[
        str,
        typer.Option(help="The preferred title of the person to greet")
    ] = "",
    doctor: Annotated[
        bool,
        typer.Option(help="Whether the person is a doctor (MD or PhD)")
    ] = False,
    count: Annotated[
        int,
        typer.Option(help="Number of times to greet the person")
    ] = 1,
):
    requestBody = ServiceRequestBodyExample(
        name=name,
        title=title,
        is_doctor=doctor,
        count=count,
    )
    message = core_service_call(requestBody)
    print(message)


if __name__ == "__main__":
    app()
