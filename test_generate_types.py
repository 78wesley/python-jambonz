from generate_types import generate_dataclasses

if __name__ == "__main__":
    schema = {
        "target": {
            "properties": {
                "type": {"type": "string", "enum": ["phone", "sip", "user", "teams"]},
                "confirmHook": "object|string",
                "method": {"type": "string", "enum": ["GET", "POST"]},
                "headers": "object",
                "from": "#dialFrom",
                "name": "string",
                "number": "string",
                "sipUri": "string",
                "auth": "#auth",
                "vmail": "boolean",
                "tenant": "string",
                "trunk": "string",
                "overrideTo": "string",
                "proxy": "string",
            },
            "required": ["type"],
        }
    }
    result = generate_dataclasses(schema)
    print(result)
