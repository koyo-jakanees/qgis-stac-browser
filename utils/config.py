class Config:
    STAC_APIS = ['https://sat-api.developmentseed.org']

    def __init__(self):
        pass

    def get_api_list(self):
        return self.STAC_APIS
