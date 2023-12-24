from interval import Interval, IntervalList

import re


re_source = re.compile(r'(\w+)-to-(\w+) map')
re_numbers = re.compile(r'\d+')

# -----------------------------

class SingleMap:
    def __init__(self, destination_start:int, source_start:int, range_length:int):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length

    def into_source(self, number: int) -> bool:
        return True if self.source_start <= number < self.source_start + self.range_length else False
    
    def convert(self, number: int) -> int:
        return self.destination_start + (number - self.source_start)
        
    def convert_interval(self, interval:Interval) -> Interval:
        first = max([self.source_start, interval.first])
        last = min([self.source_start + self.range_length - 1, interval.last])
        # converted interval
        if first <= last:
            converted_interval = Interval(
                first = self.convert(first), 
                last = self.convert(last)
            )
            return converted_interval
    
    def __repr__(self) -> str:
        return f"{self.destination_start} {self.source_start} {self.range_length}"
    
    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other: 'SingleMap') -> bool:
        if (
            self.destination_start == other.destination_start and 
            self.source_start == other.source_start and 
            self.range_length == other.range_length
        ):
            return True
        return False
        

class IntervalMap:
    def __init__(self, block:str = None):
        self.source = None
        self.destination = None
        self._list: list[SingleMap] = []
        if block:
            self.get_map(block)

    def convert(self, number: int):
        for single_map in self._list:
            if single_map.into_source(number):
                return single_map.convert(number)
        return number
            
    def convert_interval(self, interval:Interval) -> IntervalList:
        interval_list = IntervalList()        
        for single_map in self._list:
            converted_interval = single_map.convert_interval(interval)
            if converted_interval:
                interval_list.insert(converted_interval)
        return interval_list
    
    def convert_interval_list(self, interval_list:IntervalList) -> IntervalList:
        converted_interval_list = IntervalList()
        for interval in interval_list[::-1]:
            new_list = self.convert_interval(interval)
            for converted_interval in new_list[::-1]:
                converted_interval_list.insert(converted_interval)
        return converted_interval_list

    def get_map(self, block: str):
        self.source, self.destination = self._get_source_destination(block)
        self._list = self._get_map_block(block)
    
    def _get_source_destination(self, block: str):
        source, destination = re_source.match(block).groups()
        return source, destination
    
    def _get_map_block(self, block: str):
        _map = []

        lines = block.split('\n')
        for index in range(1, len(lines)):
            line = lines[index]
            map_line_str = re_numbers.findall(line)
            map_line = [int(number) for number in map_line_str]
            if map_line:
                _map.append(SingleMap(*map_line))
        # sort _map list
        sorted_map: list[SingleMap] = sorted(_map, key=lambda single_map: single_map.source_start)
        # take the first single map
        sorted_map.insert(0, SingleMap(0, 0, sorted_map[0].source_start))
        # take the last single map
        sorted_map.append(SingleMap(
            destination_start = sorted_map[-1].source_start + sorted_map[-1].range_length,
            source_start = sorted_map[-1].source_start + sorted_map[-1].range_length,
            range_length = float('Inf')
        ))

        return sorted_map
    
    def __repr__(self) -> str:
        body:str = '\n'.join([str(single_map) for single_map in self._list])
        body = f'{self.source}-to-{self.destination} map:\n' + body + '\n'
        return body
    
    def __str__(self) -> str:
        return self.__repr__()


class ListMap:
    def __init__(self, almanac:str = None):
        self._list: list[IntervalMap] = []
        if almanac:
            self.get_maps(almanac)

    def get_maps(self, almanac:str):
        blocks = almanac.split('\n\n')

        for index in range(1, len(blocks)):
            block = blocks[index]
            interval_map = IntervalMap(block)
            self._list.append(interval_map)
    
    def convert(self, number:int) -> int:
        converted_number = number
        for interval_map in self._list:
            converted_number = interval_map.convert(converted_number)
        return converted_number

    def convert_interval_list(self, interval_list:IntervalList) -> IntervalList:
        converted_interval_list = interval_list
        for interval_map in self._list:
            converted_interval_list = interval_map.convert_interval_list(converted_interval_list)
        return converted_interval_list
    
    def __repr__(self) -> str:
        return '\n'.join([str(interval_map) for interval_map in self._list])
    
    def __str__(self) -> str:
        return self.__repr__()