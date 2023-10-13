#!/usr/bin/python3

import uuid

import datetime

from __init__ import storage

class BaseModel:
	id = 0
	created_at = 0
	updated_at = datetime.datetime.now()
	print("//////\nupdated_at (on instancing): {}\n//////".format(updated_at))
	def __init__(self, *args, **kwargs):
		if kwargs is not None and len(kwargs) > 0:
			self.from_dict(kwargs)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.datetime.now()
	
	def __str__(self):
		return "{} ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = datetime.datetime.now()
		storage.save()

	def to_dict(self):
		self.created_at = self.created_at.isoformat()
		self.updated_at = datetime.datetime.now()
		print("//////\nupdated_at (at conversion to dict): {}\n//////".format(self.updated_at))
		self.updated_at = self.updated_at.isoformat()
		self.__dict__['__class__'] = self.__class__.__name__
		return self.__dict__

	def from_dict(self, kwargs):
		print("///\nkwargs: {}\n///".format(kwargs))
		self.id = kwargs["id"]
		self.created_at = datetime.datetime.strptime(kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
		self.updated_at = datetime.datetime.strptime(kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")
