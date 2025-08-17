"""
jobs/routes.py

This module defines all the routes related to job listings, applications, 
drafts, and saved jobs in the Flask application.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.job import Job
from models.application import Application
from time import strftime
import uuid
from utilities import file_helper

jobs_bp = Blueprint('jobs', __name__, url_prefix="/jobs")


@jobs_bp.route('/')
def list_jobs():
    """
    Display all available job listings.

    Returns:
        Response: Rendered template with job listings.
    """
    jobs = Job.load_data()
    return render_template('jobs.html', jobs=jobs)


@jobs_bp.route('/apply/<job_id>', methods=['GET', 'POST'])
def apply_job(job_id):
    """
    Handle the job application process (apply or save as draft).

    Args:
        job_id (str): The ID of the job being applied to.

    Returns:
        Response: Redirects to job list or re-renders the application form.
    """
    job = Job.find_by_id(job_id)
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

        action = request.form.get('action')
        if action == "apply":
            applications = Application.load_data() or []
            if file_helper.has_applied(applications, job_id, applicant_email):
                flash("You have already applied for this job.", "warning")
            else:
                Application.save_to_json(application)
                flash("Applied successfully", "success")

        elif action == "draft":
            drafts_list = Application.load_drafts()
            if file_helper.has_draft(drafts_list, job_id, applicant_email):
                flash("You already have a draft for this job.", "warning")
            else:
                Application.save_draft(application, "data/drafts.json")
                flash("Draft saved successfully", "success")

        return redirect(url_for('jobs.list_jobs'))

    return render_template('apply_job.html', job=job)


@jobs_bp.route('/applied_jobs/', methods=['GET'])
def get_applied_jobs():
    """
    Show the list of all jobs the user has applied for.

    Returns:
        Response: Rendered template with applied jobs.
    """
    applied_jobs_data = Application.load_data()
    return render_template('applied_jobs.html', applied_jobs=applied_jobs_data)


@jobs_bp.route("/save/<job_id>", methods=['POST'])
def save_job(job_id):
    """
    Save a job to the user's saved jobs list.

    Args:
        job_id (str): The ID of the job to save.

    Returns:
        Response: Redirect to saved jobs page.
    """
    job = Job.find_by_id(job_id)
    if not job:
        return "Job not found", 404

    saved_jobs = file_helper.read_file("data/saved_jobs.json")
    for saved_job in saved_jobs:
        if saved_job["id"] == job.id:
            flash("You have already saved this job.", "warning")
            return redirect(url_for('jobs.saved_jobs'))

    Job.save_to_json(job, "data/saved_jobs.json")
    flash("Saved successfully", "success")
    return redirect(url_for('jobs.saved_jobs'))


@jobs_bp.route('/saved')
def saved_jobs():
    """
    Display all saved jobs.

    Returns:
        Response: Rendered template with saved jobs.
    """
    saved_jobs = Job.load_saved_jobs()
    return render_template('saved_jobs.html', saved_jobs=saved_jobs)


@jobs_bp.route("/remove/<job_id>", methods=['POST'])
def remove_saved_job(job_id):
    """
    Remove a saved job by its ID.

    Args:
        job_id (str): The ID of the job to remove.

    Returns:
        Response: Redirect to saved jobs page with success message.
    """
    job_data = file_helper.read_file("data/saved_jobs.json")
    new_jobs = [job for job in job_data if job["id"] != job_id]
    file_helper.write_file("data/saved_jobs.json", new_jobs)

    flash("Job removed successfully!", "success")
    return redirect(url_for('jobs.saved_jobs'))


@jobs_bp.route('/search')
def search_jobs():
    """
    Search for jobs by title keyword.

    Query Params:
        query (str): The search term entered by the user.

    Returns:
        Response: Rendered template with filtered jobs.
    """
    query = request.args.get('query', '').strip().lower()
    jobs_list = Job.load_data()
    searched_jobs = [job for job in jobs_list if query in job.title.lower()]
    return render_template('jobs.html', jobs=searched_jobs)


@jobs_bp.route('/job_details/<job_id>', methods=['GET'])
def get_job_details(job_id):
    """
    Display details of a specific job.

    Args:
        job_id (str): The ID of the job.

    Returns:
        Response: Rendered template with job details or 404 if not found.
    """
    job = Job.find_by_id(job_id)
    if not job:
        return "Job not found", 404
    return render_template('job_details.html', job=job)


@jobs_bp.route('/drafts')
def drafts():
    """
    Display all saved draft applications.

    Returns:
        Response: Rendered template with draft applications.
    """
    drafts_list = Application.load_drafts()
    return render_template('drafts.html', drafts=drafts_list)


@jobs_bp.route('/drafts/edit/<draft_id>', methods=['GET'])
def edit_draft(draft_id):
    """
    Load a draft application for editing.

    Args:
        draft_id (str): The ID of the draft.

    Returns:
        Response: Rendered edit draft template or 404 if not found.
    """
    drafts_list = Application.load_drafts()
    draft = next((d for d in drafts_list if d['id'] == draft_id), None)

    if not draft:
        return "Draft not found", 404

    return render_template('edit_draft.html', draft=draft)


@jobs_bp.route('/drafts/update/<draft_id>', methods=['POST'])
def update_draft(draft_id):
    """
    Update an existing draft or submit it as an application.

    Args:
        draft_id (str): The ID of the draft.

    Returns:
        Response: Redirect to jobs or drafts page depending on action.
    """
    drafts_list = Application.load_drafts()
    draft = next((d for d in drafts_list if d['id'] == draft_id), None)

    if not draft:
        return "Draft not found", 404

    # Update draft fields
    draft['applicant_name'] = request.form.get('full_name')
    draft['applicant_email'] = request.form.get('email')
    draft['cv_link'] = request.form.get('cv_link')
    draft['cover_letter'] = request.form.get('cover_letter')
    draft['date_applied'] = strftime('%Y-%m-%d')

    action = request.form.get('action')
    if action == "apply":
        applications = Application.load_data()
        if file_helper.has_applied(applications, draft['job_id'], draft['applicant_email']):
            flash("You have already applied for this job.", "warning")
            return redirect(url_for('jobs.drafts'))

        Application.save_to_json(Application(**draft))
        drafts_list = [d for d in drafts_list if d['id'] != draft_id]
        file_helper.write_file("data/drafts.json", drafts_list)
        flash("Submitted successfully", "success")
        return redirect(url_for('jobs.list_jobs'))

    elif action == "draft":
        file_helper.write_file("data/drafts.json", drafts_list)
        flash("Updated successfully", "success")
        return redirect(url_for('jobs.drafts'))
