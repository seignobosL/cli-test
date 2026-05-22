from pydantic import BaseModel, Field, conint, constr

class StrictGreetRequest(BaseModel):
    name: constr(min_length=1, max_length=50)

    count: conint(ge=1, le=10) = 1

    is_doctor: bool = False

    title: str = Field(default="", pattern=r"^(Dr\.|M\.|Mme|)$")