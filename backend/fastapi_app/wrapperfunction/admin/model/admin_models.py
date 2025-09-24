from pydantic import BaseModel, Field
from typing import Optional, Union
import uuid
class UserQuery(BaseModel):
    admin_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)# 
    query: Optional[str]
