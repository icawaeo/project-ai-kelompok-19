from app import create_app
from apscheduler.schedulers.background import BackgroundScheduler
from app.routes import check_reminder

if __name__ == "__main__":
    app, db = create_app()
    
    with app.app_context():
        db.create_all()
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=check_reminder, trigger="interval", days=1)
    scheduler.start()
    
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
