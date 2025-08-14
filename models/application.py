
import json
import uuid
from time import strftime
from utilities import file_helper
from models.base_model import BaseModel


class Application(BaseModel):
    path = 'data/application.json'

    def __init__(self, id, job_id, job_title, applicant_name, applicant_email,
                 cover_letter, company_name, cv_link, date_applied):
        self.id = id
        self.job_id = job_id
        self.job_title = job_title
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.cover_letter = cover_letter
        self.company_name = company_name
        self.cv_link = cv_link
        self.date_applied = date_applied

    @classmethod
    def find_by_job_id(cls, job_id):
        applications = cls.load_data()
        return [app for app in cls.load_data() if app.job_id == job_id]
    
    @classmethod
    def save_draft(cls, application , filepath):
        cls.save_to_json(application, filepath)

    @classmethod
    def load_drafts(cls):
        drafts = file_helper.read_file("data/drafts.json")
        
        drafts_list = []
        for draft in drafts:
            drafts_list.append(draft)
        return drafts_list
    