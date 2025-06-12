class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)

        cooldown_queue = deque()
        time = 0
        while max_heap or cooldown_queue:
            time += 1
            if max_heap:
                current_count = heappop(max_heap) + 1
                if current_count != 0:
                    cooldown_queue.append((time + n, current_count))
            if cooldown_queue and cooldown_queue[0][0] == time:
                _, cooled_task_count = cooldown_queue.popleft()
                heappush(max_heap, cooled_task_count)
        return time
