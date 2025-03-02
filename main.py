from flask_backend import app;
from AI import AI_startup;
if __name__ == "__main__":
    
    try:
        AI_startup()
        app.run()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    
    