



class Sort:
    def __init__(self,target):
        self.target = target
    def bubble(self):
        for i in range(len(self.target)-1):
            for j in range(len(self.target)-1, i, -1):
                if self.target[j] < self.target[j - 1]:
                    self.target[j],self.target[j-1] = self.target[j-1],self.target[j]

    def select(self):
        for i in range(len(self.target)-1):
            min = i
            for j in range(i+1,len(self.target)):
                if self.target[j] < self.target[min]:
                    min = j
            if i != min:
                self.target[min],self.target[i] = self.target[i],self.target[min]

    def insert(self):
        for i in range(len(self.target)):
            x = self.target[i]
            j = i
            while j > 0 and self.target[j-1] > x:
                self.target[j] = self.target[j-1]
                j -= 1
            self.target[j] = x

    def quick(self,low,hi):
        if low < hi:
            p = self.__partition(low, hi)
            self.quick(low,p-1)
            self.quick(p+1,hi)

    def __partition(self, low, hi):
        pivot = self.target[hi]
        i = low-1
        for j in range(low,hi) :
            if self.target[j] < pivot:
                i += 1
                self.target[i],self.target[j] = self.target[j],self.target[i]
        self.target[hi],self.target[i+1] = self.target[i+1],self.target[hi]
        return i+1





if __name__ == "__main__":
    list01 = [4,3,6,8,9,2,1,5]
    st = Sort(list01)
    st.quick(0,7)
    print(st.target)



