#!/usr/bin/python3

import uuid
import json
import os
import datetime

from models.base_model import BaseModel

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def __init__():
		pass

	def all(self):
		return self.__objects

	def new(self, obj):
		# add new id:obj in __objects
		obj_id = '{}'.format(obj.id)
		__objects[obj_id] = obj

	def save(self):
		# serializes objects in __objects
		for obj in __objects:
			obj.dump(self.__file_path)

	def reload(self):
		# calls load --ONLY USE IF NECESSARY--
		pass

	def load(self):
		# deserializes json file to __objects 
		pass
