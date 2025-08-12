from flask import Blueprint, render_template, request, redirect, url_for
from models.job import Job
from time import strftime
import json
import uuid
from utilities import file_helper
jobs_bp = Blueprint('jobs', __name__, url_prefix="/jobs")


@jobs_bp.route('/')
def list_jobs():
    jobs = Job.load_data()
    return render_template('jobs.html', jobs=jobs)

@jobs_bp.route('/apply/<job_id>', methods = ['GET' , 'POST'])
def apply_job(job_id):
    # first we get the job by id
    job = Job.find_by_id(job_id)

    #then we it is not found
    if not job:
        return "Job not found", 404
    
    if request.method == 'POST':
        applicant_name = request.form.get('full_name')
        applicant_email = request.form.get('email')
        cover_letter = request.form.get('cover_letter')
        cv_link = request.form.get('cv_link')

        application = {
                "id": str(uuid.uuid4()),
                "job_id": job_id,
                "job_title": job.id,
                "applicant_name": applicant_name,
                "applicant_email": applicant_email,
                "cover_letter": cover_letter,
                "company_name" : job.id,
                "cv_link" : cv_link,
                "date_applied": strftime('%Y-%m-%d')
            }
        
        Job.save_to_json("data/application.json", application)

        return redirect(url_for('jobs.list_jobs'))

    return render_template('apply_job.html', job=job)