from pydantic import BaseModel, ConfigDict, Field, conint, constr

class StrictModelTemplate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    str_max_5: constr(min_length=0, max_length=5) = ""
    int_max_5: conint(ge=1, le=5) = 1
    boolean: bool = False
    pattern_match: str = Field(default="", pattern=r"^(A\.|B\.|C\.|)$")

class CLIStarterTemplate(BaseModel):
    name: constr(min_length=0, max_length=50) = ""
    count: conint(ge=1, le=10) = 1
    is_doctor: bool = False
    title: str = Field(default="", pattern=r"^(Dr\.|M\.|Mme|)$")

