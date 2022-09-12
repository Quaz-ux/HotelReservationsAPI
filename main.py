from app import create_app, Room
from app.models.room import db

reservationsapi = create_app()


if __name__ == "__main__":
    reservationsapi.run(debug=True)
