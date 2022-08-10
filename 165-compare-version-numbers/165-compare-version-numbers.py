class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = list(map(int, version1.split('.')))
        vers2 = list(map(int, version2.split('.')))
        if len(vers1) > len(vers2):
            vers2 += [0] * (len(vers1) - len(vers2))
        elif len(vers1) < len(vers2):
            vers1 += [0] * (len(vers2) - len(vers1))
        for i in range(len(vers1)):
            if vers1[i] > vers2[i]:
                return 1
            elif vers1[i] < vers2[i]:
                return -1
        return 0