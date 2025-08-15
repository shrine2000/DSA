from collections import Counter
from typing import List


class BruteForce:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        last_exec_time = {task: -n - 1 for task in task_counts}
        time = 0
        remaining = sum(task_counts.values())
        while remaining > 0:
            available_tasks = [
                task
                for task in task_counts
                if task_counts[task] > 0 and time - last_exec_time[task] > n
            ]
            if available_tasks:
                task_to_run = max(available_tasks, key=lambda t: task_counts[t])
                task_counts[task_to_run] -= 1
                last_exec_time[task_to_run] = time
                remaining -= 1
            time += 1
        return time
