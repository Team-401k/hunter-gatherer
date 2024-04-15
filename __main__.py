#!/usr/bin/env python3
import uvicorn
import threading
import sys

def exit_application():
    sys.exit(0)

def main():

    timeout = 50
    
    # Start the timer
    timer = threading.Timer(timeout, exit_application)
    timer.start()

    """Entrypoint of the application"""
    uvicorn.run(
        "app.app:get_app",
        reload=True,
        factory=True,
        timeout_keep_alive=60,
    )
    exit()

if __name__ == "__main__":
    main()