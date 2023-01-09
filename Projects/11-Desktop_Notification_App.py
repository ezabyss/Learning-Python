from plyer import notification
import time

while(True):
    notification.notify(
        title="Start Coding Now!",
        message="Be focused at the craft of doing.",
        app_icon="Projects/Assets/notificaiton.ico",
        timeout=5
    )
    time.sleep(10)
