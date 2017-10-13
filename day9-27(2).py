import math

def 면적(*반):
    for 반지름 in 반:
        합 = 반지름 * 반지름 * math.pi
        return 합

면적(1,2,3,4,5)