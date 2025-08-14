from utilities import file_helper
import uuid

class BaseModel:
    path = None

    def to_dict(self):
        return self.__dict__

    @classmethod
    def load_data(cls):
        data_db = file_helper.read_file(cls.path)
        return [cls(**item) for item in data_db]

    @classmethod
    def save_to_json(cls, obj, filepath=None):
        path = filepath or cls.path
        data_db = file_helper.read_file(path)

        updated = False

    # Update existing object if found
        for i in range(len(data_db)):
            if data_db[i].get('id') == obj.id:
                data_db[i] = obj.to_dict()
                updated = True
                break

    # If not updated (object doesn't exist), append it
        if not updated:
            data_db.append(obj.to_dict())

        file_helper.write_file(path, data_db)

    @classmethod
    def delete(cls, id):
        data_db = cls.load_data()
        data = [item.to_dict() for item in data_db if item.id != id]
        file_helper.write_file(cls.path, data)

    