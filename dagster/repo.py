from dagster import job, op, repository, ScheduleDefinition

@op
def welcome_op():
    return "Willkommen auf dem Mothership!"

@job
def welcome_job():
    welcome_op()

@repository
def mothership_repo():
    return [
        welcome_job,
        ScheduleDefinition(job=welcome_job, cron_schedule="0 9 * * *"),
    ]