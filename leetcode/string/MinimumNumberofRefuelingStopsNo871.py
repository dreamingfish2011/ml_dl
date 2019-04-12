import heapq
class Solution:
    def minRefuelStops(self, target, start_fuel, stations):
        stations.append([target, 0])
        pq_passed_stations = []
        tank = start_fuel
        ret = 0
##先不走，先把所有能找到的站点入堆。然后在从中判断找到能到达的最远公里数
##heapq 最小顶堆
        for mile, gas in stations:
            while pq_passed_stations and tank < mile:
                tank += -heapq.heappop(pq_passed_stations)
                ret += 1

            if tank < mile:
                return -1

            heapq.heappush(pq_passed_stations, -gas)

        return ret
target = 100
start_fuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
t =Solution()
ret = t.minRefuelStops(target, start_fuel, stations)
print(ret)
