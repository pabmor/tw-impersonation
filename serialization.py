import pickle

class Serializer:
	def save(self, data):
		try:
			output = open('data.pk1', 'wb')
			pickle.dump(obj=a, file=output, protocol=2)
			output.close()
		except IOError as err:
			print("Couldn't persist data: ", err.args)

	def load(self):
		try:
			pkl_file = open('data.pk1', 'rb')
			data = pickle.load(pkl_file)
			return data;
		except IOError as err:
			print("Couldn't load data: ", err.args)