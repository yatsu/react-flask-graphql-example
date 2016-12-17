from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import Schema


def create_app(**kwargs):
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=Schema, **kwargs)
    )
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    CORS(app, resources={r'/graphql': {'origins': '*'}})
    app.run()
