class Payloads:

    @staticmethod
    def request_create_user_payload():
        return {
            "email": "",
            "password": "",
            "name": ""
        }

    @staticmethod
    def request_login_payload():
        return {
                "email": "",
                "password": ""
        }
