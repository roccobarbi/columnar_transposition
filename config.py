class Config:
    def __init__(self, width=None):
        self.width = width
        self.force_complete = False
        self.iterations = 1
        self.keywords = []
        self.rearrange = False

    def set_width(self, width):
        self.width = width

    def set_force_complete(self, force_complete):
        self.force_complete = force_complete

    def set_iterations(self, iterations):
        self.iterations = iterations

    def set_keywords(self, keywords):
        self.keywords = keywords

    def set_rearrange(self, rearrange):
        self.rearrange = rearrange

    def append_keyword(self, keyword):
        self.keywords.append(keyword)
