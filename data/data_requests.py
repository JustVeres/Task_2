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

    @staticmethod
    def changing_user_data_payload():
        return {
            "email": "",
            "name": ""
        }

    @staticmethod
    def create_order_payload():
        return {
            "ingredients": []
        }
