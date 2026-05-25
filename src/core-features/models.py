from pydantic import BaseModel, ConfigDict, Field, conint, constr

class StrictModelTemplate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    str_max_5: constr(min_length=0, max_length=5) = ""
    int_max_5: conint(ge=1, le=5) = 1
    bool: bool = False
    pattern_match: str = Field(default="", pattern=r"^(Dr\.|M\.|Mme|)$")