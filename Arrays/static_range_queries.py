get_prefix_sum = lambda arr: [0] + [sum(arr[: i + 1]) for i in range(len(arr))]

range_sum_query = (
    lambda prefix_sum, a, b: prefix_sum[b] - prefix_sum[a - 1]
    if a > 0
    else prefix_sum[b]
)


def process_queries(arr, queries):
    prefix_sum = get_prefix_sum(arr)
    res = []
    for a, b in queries:
        res.append((range_sum_query(prefix_sum, a, b)))
    return res


if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = process_queries(arr, queries)
    for result in results:
        print(result)
