class Ponto2D:
    def __init__(self, x = 0.0, y = 0.0) :
        self.x = x
        self.y = y
        
class Retangulo:
    def __init__(self, esq_sup, dir_inf) :
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
        self.width = abs(self.__dir_inf.x - self.__esq_sup.x)
        self.height = abs(self.__esq_sup.y - self.__dir_inf.y)
    
    @property
    def esq_sup(self) :
        return self.__esq_sup

    @property
    def dir_inf(self) :
        return self.__dir_inf

    @esq_sup.setter
    def esq_sup (self, value_esq) :
        self.__esq_sup = value_esq

    @dir_inf.setter
    def dir_inf (self, value_dir) :
        self.__dir_inf = value_dir

    def calcularArea(self) :
        return (self.width)*(self.height)
        
    def calcularIntersecao(self, ret) :
        if (self.__esq_sup.x < ret.__esq_sup.x + ret.width
             and self.__esq_sup.x + self.width > ret.__esq_sup.x
             and self.__esq_sup.y < ret.__esq_sup.y + ret.width
             and self.__esq_sup.y + self.width > ret.__esq_sup.y) :  
            x_ = (max(ret.__esq_sup.x, self.__esq_sup.x)-
            min(ret.__dir_inf.x, self.__dir_inf.x))
            y_ = (min(ret.__esq_sup.y, self.__esq_sup.y)-
            max(ret.__dir_inf.y, self.__dir_inf.y))
            return abs(x_*y_)
        else:
            return None
