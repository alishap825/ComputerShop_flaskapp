from computer_shop import create_app, db, admin


if __name__ == "__main__":
    # create app
    app = create_app()

    # create tables for the model classes
    # creates new tables if they do not exist
    # does not update existing tables
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    # admin.create_data(db)

    # run app on port 5000
    app.run(port=5000)
