
import json
import uuid
from time import strftime
from utilities import file_helper

class Application:
    path = 'data/application.json'

    def __init__(self, id, job_id, job_title, applicant_name, applicant_email, cover_letter, company_name, cv_link, date_applied):
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
    def load_data(cls):
        applications_list = file_helper.read_file(cls.path)
        return [cls(**app) for app in applications_list]

    