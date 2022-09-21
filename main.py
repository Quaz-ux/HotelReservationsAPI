from app import create_app

reservationsapi = create_app()


if __name__ == "__main__":
    reservationsapi.run(debug=True)
