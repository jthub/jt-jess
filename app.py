#!/usr/bin/env python3
import connexion
import datetime
import logging
import jt_jess
from jt_jess.exceptions import OwnerNameNotFound, AMSNotAvailable, WorklowNotFound, WRSNotAvailable
from connexion import NoContent


def get_jobs(owner_name):
    pass


def get_job(owner_name):
    pass


def enqueue_job(owner_name):
    pass


def get_workers(owner_name, job_queue_id):
    pass


def get_worker(owner_name, job_queue_id, worker_id):
    pass


def register_worker(owner_name, job_queue_id):
    pass


def next_task(owner_name, job_queue_id, worker):
    pass


def next_task_from_job(owner_name, job_queue_id, job_id, worker):
    pass


def complete_task(owner_name, job_queue_id, task_name):
    pass


def fail_task(owner_name, job_queue_id, task_name):
    pass


def get_job_queues(owner_name, workflow_name=None, workflow_version=None):
    if workflow_name and '.' in workflow_name:
        if len(workflow_name.split('.')) > 2:
            return 'Value for workflow name parameter can not have more than two dots (.)', 400
        else:
            workflow_owner_name, workflow_name = workflow_name.split('.')
    else:
        workflow_owner_name = owner_name

    try:
        workflows = jt_jess.get_job_queues(owner_name, workflow_name, workflow_version, workflow_owner_name)
    except OwnerNameNotFound as err:
        return str(err), 404
    except AMSNotAvailable as err:
        return str(err), 500
    except WorklowNotFound as err:
        return str(err), 404
    except WRSNotAvailable as err:
        return str(err), 500

    return workflows or ('No workflow job queue found', 404)


def get_job_queues1(owner_name):
    try:
        workflows = get_job_queues(owner_name)
    except OwnerNameNotFound as err:
        return str(err), 404
    except AMSNotAvailable as err:
        return str(err), 500
    except WorklowNotFound as err:
        return str(err), 404
    except WRSNotAvailable as err:
        return str(err), 500

    return workflows or ('No workflow job queue found', 404)


def get_job_queues2(owner_name, workflow_name):
    try:
        workflows = get_job_queues(owner_name, workflow_name)
    except OwnerNameNotFound as err:
        return str(err), 404
    except AMSNotAvailable as err:
        return str(err), 500
    except WorklowNotFound as err:
        return str(err), 404
    except WRSNotAvailable as err:
        return str(err), 500

    return workflows or ('No workflow job queue found', 404)


def get_job_summary(owner_name, job_queue_id):
    pass


def job_action(owner_name):
    pass


def job_queue_action(owner_name):
    pass


def worker_action(owner_name, job_queue_id, worker_id):
    return


def register_job_queue(owner_name, owner_type='org'):
    exists = jt_jess.get_owner(owner_name)
    if exists:
        return NoContent, 409
    else:
        return jt_jess.create_owner(owner_name, owner_type)


def register_job_queue1():
    pass


def get_tasks(owner_name):
    pass


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml', base_path='/api/jt-jess/v0.1')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=1208, server='gevent')
