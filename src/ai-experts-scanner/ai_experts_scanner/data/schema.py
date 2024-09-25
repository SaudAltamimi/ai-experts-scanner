from typing import List, Optional
from pydantic import BaseModel, Field

# Define the schema for extracting information
class Person(BaseModel):
    """Information about a key person in a company."""
    name: str = Field(description="Full name of the person")
    role: str = Field(description="Current role or position in the company")
    background: Optional[str] = Field(description="Brief background or previous experience")
    importance: Optional[str] = Field(description="Importance to the company and potential impact on investment decisions")

class CompanyData(BaseModel):
    """Extracted data about key people in a company."""
    company_name: str = Field(description="Name of the company")
    key_people: List[Person] = Field(description="List of key people in the company")