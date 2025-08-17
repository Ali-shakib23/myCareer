import json

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lists = json.load(f)
            return lists
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_file(filepath , data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


#saved_jobs = file_helper.read_file("data/saved_jobs.json")
    #for saved_job in saved_jobs:
        #if saved_job["id"] == job.id:
def is_exist(lists, id ,   filepath):
    for list in lists :
        if list["id"] == id:
            return True
    return False

def has_applied(applications, job_id, applicant_email):
    for app in applications:
       
        if app.job_id == job_id and app.applicant_email == applicant_email:
            return True
    return False

def has_draft(drafts, job_id, applicant_email):
    
    for draft in drafts:
        if draft["job_id"] == job_id and draft["applicant_email"] == applicant_email:
            return True
    return False
