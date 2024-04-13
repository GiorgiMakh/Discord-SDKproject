import time
import discordsdk as dsdk
import os

app = dsdk.Discord("Your_Discord_APP_ID", dsdk.CreateFlags.default)

activity_manager = app.get_activity_manager()

activity = dsdk.Activity()
activity.state = "Testing Game SDK"
activity.party.id = "my_super_party_id"
activity.party.size.current_size = 4
activity.party.size.max_size = 8
activity.secrets.join = "my_super_secret"


def callback(result):
    if result == dsdk.Result.ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)


activity_manager.update_activity(activity, callback)

while 1:
    time.sleep(1/10)
    app.run_callbacks()