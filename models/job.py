import json
import uuid
from time import strftime
from utilities import file_helper
class Job : 
    path = 'data/jobs.json'

    def __init__(self ,title, company_name, location, salary, job_type, description,
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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company_name": self.company_name,
            "location": self.location,
            "salary": self.salary,
            "job_type": self.job_type,
            "description": self.description,
            "requirements": self.requirements,
            "contact_email": self.contact_email,
            "date_posted": self.date_posted
        }

    @classmethod
    def load_data(cls):
        job_lists  = file_helper.read_file(cls.path)
        return [cls(**job) for job in job_lists]
       
    
    @classmethod
    def find_by_id(cls ,id):
        jobs = cls.load_data()
        for job in jobs : 
            if job.id == id:
                return job
        return None 
    
    @classmethod
    def save_to_json(cls, filepath , data):
        data_db = file_helper.read_file(filepath)
        data_db.append(data.to_dict())
        file_helper.write_file(filepath , data_db)

    @classmethod
    def delete(cls, id):
        jobs = cls.load_data()
        jobs = [job for job in jobs if job.id != id]
        file_helper.write_file(cls.path,jobs)

    @classmethod
    def load_saved_jobs(cls):
        saved_jobs = file_helper.read_file("data/saved_jobs.json")
        return saved_jobs