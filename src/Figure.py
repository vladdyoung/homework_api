class Figure:
    def add_figure(self, name):
        if isinstance(name, Figure):
            return self.area + name.area
        else:
            try:
                raise ValueError
            except ValueError:
                return
