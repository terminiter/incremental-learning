import model.densenet as dn
import model.resnet32 as res
class modelFactory():
    def __init__(self):
        pass
    def getModel(self, modelType):
        if modelType=="densenet":
            return dn.DenseNet(growthRate=12, depth=40, reduction=0.5,
                        bottleneck=True, nClasses=100)
        elif modelType=="resnet32":
            return res.resnet32(100)