from app import db
from datetime import datetime

class Urls(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fake_url = db.Column(db.String(), nullable=False)
	real_url = db.Column(db.String(), nullable=False)
	date_minified = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"{self.id}, {self.fake_url}, {self.real_url}"