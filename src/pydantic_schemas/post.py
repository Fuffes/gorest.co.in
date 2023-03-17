from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int
    title: str

    # id: int = Field(le=3)
    # name: str = Field(alias='_name') ///if we have some key like _name

    # @validator('id')
    # def check_id_less_2(cls, v):
    #     if v > 2:
    #         raise ValueError('id less than 2')
    #     else:
    #         raise v
