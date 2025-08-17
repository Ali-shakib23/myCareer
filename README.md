
# MY FINAL PROJECT

This project is a **Job Application Management System** built with Flask, where users can apply for jobs, save draft applications, and manage their applications efficiently.

---

## What does it do?

- Employees can view available jobs and apply.  
- Employees can save drafts of applications and edit them before submitting.  
- Employees can view saved jobs and remove them if needed.  
- Employees can search for jobs based on their title.

---

## What is the "new feature" which you have implemented that we haven't seen before?

- Used **form validation with JavaScript** to ensure correct user input.  
- Integrated **localStorage** to persist form data even when the page is refreshed.  
- Implemented **flash messages** for notifications of different processes (apply, save draft, etc.).  
- Applied **CSS and HTML** for styling the app.  
- Applied **inheritance** by developing a **BaseModel** class that serves as a parent for `Job` and `Application` classes.  
- Used **uuid** for unique identifiers.

---

## Prerequisites

To run this project, you need:

```bash
pip install flask
flask run
````

---

## Project Checklist

* [x] It is available on GitHub.
* [x] It uses the Flask web framework.
* [x] It uses at least one module from the Python Standard Library other than `random`.

  * Module name: `json`, `uuid`, `strftime`
* [x] It contains at least one class written by you that has both properties and methods.

  * File name for the class definition: `models/job.py`
  * Line number(s) for the class definition: 7-35
  * Name of two properties: `id`, `title`
  * Name of two methods: `find_by_id(cls, id)`, `load_saved_jobs(cls)`
  * File name and line numbers where the methods are used: `job/routes.py` (lines 131 and 182)
* [x] It makes use of JavaScript in the front end and uses the `localStorage` of the web browser.
* [x] It uses modern JavaScript (e.g., `let` and `const` instead of `var`).
* [x] It makes use of reading and writing to the same file feature (`JSON` files).
* [x] It contains conditional statements.

  * File name: `jobs/routes.py`
  * Line number(s):41, 64, 109
* [x] It contains loops.

  * File name: `jobs/routes.py`
  * Line number(s): 113
* [x] It lets the user enter a value in a text box, which is processed by your back-end Python code.
* [x] It doesn't generate any error message even if the user enters wrong input.
* [x] It is styled using your own CSS.
* [x] The code follows the style conventions introduced in the course, is fully documented using comments, and doesn't contain unused or experimental code.
* [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.

```
