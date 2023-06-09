import uuid

import pydantic


class TeacherBase(pydantic.BaseModel):
    full_name: str


class TeacherRead(TeacherBase):
    id: uuid.UUID
