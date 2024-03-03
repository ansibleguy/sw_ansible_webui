class FilterModule(object):

    def filters(self):
        return {
            "ensure_list": self.ensure_list,
        }

    @staticmethod
    def ensure_list(data: (str, list)) -> list:
        # if user supplied a string instead of a list => convert it to match our expectations
        if isinstance(data, list):
            return data

        if isinstance(data, str) and data.find(',') != -1:
            return data.split(',')

        return [data]
