

class Layer(list):
    def __init__(self, args):
        super().__init__(args)

    def gen_next_layer(self):
        new_layer = Layer([1])
        for index in range(len(self)-1):
            new_layer.append(self[index]+self[index+1])
        new_layer.append(1)
        return new_layer

    def __str__(self):
        return " ".join([str(i) for i in self])


class Triangle(list):
    def __init__(self, layers:int):
        super().__init__([Layer([1])])
        self.layers = layers

        for i in range(layers):
            self.append(self[-1].gen_next_layer())

    def __str__(self):
        ret = ""
        for layer in self:
            ret += str(layer) + "\n"
        return ret



if __name__=="__main__":
    a = Triangle(3)
    print(a)