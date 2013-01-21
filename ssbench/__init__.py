DEFAULT_TUBE = 'default'
STATS_TUBE = 'stats'
WORK_TUBE = 'work'

# NB: lower number --> higher priority (0 is highest, 2**32 - 1 is lowest)
# And 2**31 is the default
PRIORITY_SETUP = 5000
PRIORITY_WORK = 10000
PRIORITY_CLEANUP = 20000

CREATE_OBJECT = 'upload_object' # includes obj name
READ_OBJECT = 'get_object'       # does NOT include obj name to get
UPDATE_OBJECT = 'update_object' # does NOT include obj name to update
DELETE_OBJECT = 'delete_object' # may or may not include obj name to delete
