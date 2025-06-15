import (
	"container/heap"
	"sort"
)

type IntervalHeap [][]int

func (h IntervalHeap) Len() int { return len(h) }
func (h IntervalHeap) Less(i, j int) bool {
	return h[i][0] < h[j][0]
}
func (h IntervalHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *IntervalHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}
func (h *IntervalHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minInterval(intervals [][]int, queries []int) []int {
	type Query struct {
		val, idx int
	}
	q := make([]Query, len(queries))
	for i, v := range queries {
		q[i] = Query{v, i}
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	sort.Slice(q, func(i, j int) bool {
		return q[i].val < q[j].val
	})
	res := make([]int, len(queries))
	h := &IntervalHeap{}
	heap.Init(h)
	i := 0
	for _, query := range q {
		for i < len(intervals) && intervals[i][0] <= query.val {
			start, end := intervals[i][0], intervals[i][1]
			if end >= query.val {
				heap.Push(h, []int{end - start + 1, end})
			}
			i++
		}
		for h.Len() > 0 && (*h)[0][1] < query.val {
			heap.Pop(h)
		}
		if h.Len() == 0 {
			res[query.idx] = -1
		} else {
			res[query.idx] = (*h)[0][0]
		}
	}
	return res
}
