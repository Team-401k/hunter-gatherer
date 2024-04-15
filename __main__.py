#!/usr/bin/env python3
import uvicorn

def main():
    """Entrypoint of the application"""
    uvicorn.run(
        "app.app:get_app",
        reload=True,
        factory=True,
        timeout_keep_alive=60,
    )

if __name__ == "__main__":
    main()