
import os
import logging

def registerCallbacks(reg):
    script_name = "task_change"
    api_key = "6)odhFwnkzwxfottlaisykqgt"
    eventFilter = None
    reg.registerCallback(
        script_name,
        api_key,
        logArgs,
        eventFilter,
        None,
    )
    reg.logger.setLevel(logging.DEBUG)

def logArgs(sg, logger, event, args):

    task_id = event.get('meta').get('entity_id')
    logger.info("Tis is the task_id %s", event)
    # change the task status to be hold
    # sg.find_one('Task',[['id','is',task_id]],['sg_status_list'])
    if task_id !=None:
        if sg.find_one('Task',[['id','is',task_id]]):
            sg.update('Task',task_id,{'sg_status_list':'hld'})

            logger.info("Creating a new Modified Notes")
            note_data = {
            'project': {'type': 'Project', 'id': 125 },
            'sg_note_type':'Client',
            'subject':'Notes created task for the bob task',
            'content': "this is for bob project testing ",
            }
            sg.create('Note', note_data)
