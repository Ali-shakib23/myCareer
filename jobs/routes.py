from flask import Blueprint, render_template, request, redirect, url_for
from models.job import Job
from models.application import Application
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

        application = Application(
        id=str(uuid.uuid4()),
        job_id=job_id,
        job_title=job.title,
        applicant_name=applicant_name,
        applicant_email=applicant_email,
        cover_letter=cover_letter,
        company_name=job.company_name,
        cv_link=cv_link,
        date_applied=strftime('%Y-%m-%d')
        )
        
        Application.save_to_json(application)

        return redirect(url_for('jobs.list_jobs'))

    return render_template('apply_job.html', job=job)


@jobs_bp.route('/applied_jobs/', methods=['GET'])
def get_applied_jobs():
    applied_jobs_data= Application.load_data()
    return render_template('applied_jobs.html', applied_jobs=applied_jobs_data)

@jobs_bp.route("/save/<job_id>", methods=['POST'])
def save_job(job_id):
    job = Job.find_by_id(job_id)
    if not job:
        return "Job not found", 404
    job.save_to_json(job, "data/saved_jobs.json")
    return redirect(url_for('jobs.saved_jobs'))

@jobs_bp.route('/saved')
def saved_jobs():
    saved_jobs = Job.load_saved_jobs()
    return render_template('saved_jobs.html', saved_jobs=saved_jobs)

@jobs_bp.route("/remove/<job_id>", methods=['POST'])
def remove_saved_job(job_id):
    job_data = file_helper.read_file("data/saved_jobs.json")

    new_jobs = []
    for job in job_data:
        if job["id"] != job_id:
            new_jobs.append(job)

    file_helper.write_file("data/saved_jobs.json" , new_jobs)
    return redirect(url_for('jobs.saved_jobs'))