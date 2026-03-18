from GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor

class MonteCarloOptionProcessor:
    
    def __init__(self, geom_bm_processor : GeometricBrownianMotionProcessor, K):
        self.geom_bm_processor = geom_bm_processor
        self.K = K

        