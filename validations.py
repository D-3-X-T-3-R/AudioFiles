class Validations:
    def get_schema(self):
        schema_type = self["audio_type"]
        if schema_type == "Song":
            schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "properties": {
                    "audio_type": {"type": "string"},
                    "records": {
                        "type": "array",
                        "items": {"$ref": "#/$records/rec"},
                    },
                },
                "additionalProperties": False,
                "$records": {
                    "rec": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string", "maxLength": 100},
                            "duration": {"type": "number", "minimum": 0},
                            "upload_time": {"type": "string"},
                        },
                        "additionalProperties": False,
                        "required": [
                            "id",
                            "name",
                            "duration",
                            "upload_time",
                        ],
                    }
                },
            }
        elif schema_type == "AudioBook":
            schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "properties": {
                    "audio_type": {"type": "string"},
                    "records": {"type": "array", "items": {"$ref": "#/$records/rec"}},
                },
                "additionalProperties": False,
                "$records": {
                    "rec": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string", "maxLength": 100},
                            "author": {"type": "string", "maxLength": 100},
                            "narrator": {"type": "string", "maxLength": 100},
                            "duration": {"type": "number", "minimum": 0},
                            "upload_time": {"type": "string"},
                        },
                        "additionalProperties": False,
                        "required": [
                            "id",
                            "title",
                            "author",
                            "narrator",
                            "duration",
                            "upload_time",
                        ],
                    }
                },
            }
        elif schema_type == "Podcast":
            schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "properties": {
                    "audio_type": {"type": "string"},
                    "records": {"type": "array", "items": {"$ref": "#/$records/rec"}},
                },
                "additionalProperties": False,
                "$records": {
                    "rec": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string", "maxLength": 100},
                            "duration": {"type": "number", "minimum": 0},
                            "upload_time": {"type": "string"},
                            "hosts": {"type": "string", "maxLength": 100},
                            "participants": {
                                "type": "array",
                                "items": {"type": "string", "maxLength": 100},
                                "maxItems": 10,
                                "uniqueItems": True,
                            },
                        },
                        "additionalProperties": False,
                        "required": ["id", "name", "duration", "upload_time", "hosts"],
                    }
                },
            }
        return schema
