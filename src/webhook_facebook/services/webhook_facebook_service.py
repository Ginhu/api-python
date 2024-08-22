class WebhookFacebook():
    def __init__(self, data):
        self.data = data

    def check_data(self):
        if "test_id" not in self.data.keys():
            return {'content': 'Fail', 'status_code': 400}
        return {'content': 'ok', 'status_code': 200}

    def process_data(self):
        ...
