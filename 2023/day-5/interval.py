class Interval:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __lt__(self, other: 'Interval'):
        if self.first < other.first:
            if self.last < other.first:
                return True
        return False
    
    def __eq__(self, other: 'Interval'):
        return True if self.first == other.first and self.last == other.last else False

    def __repr__(self) -> str:
        return f"({self.first}, {self.last})"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class IntervalList:
    def __init__(self, intervals: list[Interval] = None):
        self._list: list[Interval] = []
        if intervals:
            for interval in intervals[::-1]:
                self.insert(interval)

    def insert(self, interval: Interval):
        if not self._list:
            self._list.append(interval)
        elif interval < self._list[0]:
            if interval.last + 1 == self._list[0].first:
                self._list[0].first = interval.first
            else:
                self._list.insert(0, interval)
        else:
            inserted = False
            for index in range(1, len(self._list)):
                if interval < self._list[index]:
                    linked_back = (interval.first == self._list[index - 1].last + 1)
                    linked_after = (interval.last + 1 == self._list[index].first)
                    if interval > self._list[index - 1]:
                        if linked_back:
                            if linked_after:
                                self._list[index - 1].last = self._list[index].last
                                del(self._list[index])
                            else:
                                self._list[index - 1].last = interval.last
                        else:
                            if linked_after:
                                self._list[index].first = interval.first
                            else:
                                self._list.insert(index, interval)
                        inserted = True
                        break
                    else:
                        raise ValueError(f'The interval is not compatible with this interval list because intervals {interval} and {self._list[index - 1]} overlap!')
            if not inserted:
                if interval > self._list[-1]:
                    if interval.first == self._list[-1].last + 1:
                        self._list[-1].last = interval.last
                    else:
                        self._list.append(interval)
                else:
                    raise ValueError(f'The interval is not compatible with this interval list because intervals {interval} and {self._list[-1]} overlap!')
            
    def min(self):
        return self._list[0].first

    def __getitem__(self, index: int):
        return self._list[index]
    
    def __eq__(self, other: 'IntervalList'):
        return self._list == other._list
        
    def __repr__(self):
        return str(self._list)
    
    def __str__(self):
        return self.__repr__()     