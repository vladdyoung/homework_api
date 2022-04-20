class Figure:
    def add_figure(self, name):
        if not isinstance(name, Figure):
            raise ValueError
        return self.area + name.area
