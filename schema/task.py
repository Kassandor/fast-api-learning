from pydantic import BaseModel, Field, field_validator, model_validator


class Task(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(...)

    @field_validator('name', 'category_id')
    def validate_name_category_id(cls, v):
        # print(v)
        return v

    @model_validator(mode='after')
    def validate_after_name_category_id(self):
        # print(self.name, self.category_id)
        return self
