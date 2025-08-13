import json
import uuid
from time import strftime
from models.base_model import BaseModel
from utilities import file_helper

class Job(BaseModel): 
    path = 'data/jobs.json'

    def __init__(self, title, company_name, location, salary, job_type, description,
                 requirements, contact_email, date_posted, id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.company_name = company_name
        self.location = location
        self.salary = salary
        self.job_type = job_type
        self.description = description
        self.requirements = requirements
        self.contact_email = contact_email
        self.date_posted = date_posted

    @classmethod
    def find_by_id(cls, id):
        jobs = cls.load_data()
        for job in jobs:
            if job.id == id:
                return job
        return None


    @classmethod
    def load_saved_jobs(cls):
        return file_helper.read_file("data/saved_jobs.json")
