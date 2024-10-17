from flask_restful import Resource
from flask import request, jsonify
from models import db, Episode, Guest, Appearance

class EpisodeResource(Resource):
    def get(self, id=None):
        if id is None:
            episodes = Episode.query.all()
            return jsonify([episode.to_dict() for episode in episodes])
        else:
            episode = Episode.query.get(id)
            if not episode:
                return {"error": "Episode not found"}, 404
            return jsonify(episode.to_dict())

class GuestResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

class AppearanceResource(Resource):
    def post(self):
        data = request.json
        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()
            return jsonify(appearance.to_dict()), 201
        except Exception as e:
            return {"errors": [str(e)]}, 400
