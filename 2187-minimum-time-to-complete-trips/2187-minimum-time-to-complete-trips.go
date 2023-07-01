func minimumTime(time []int, totalTrips int) int64 {
    left := min(time)
	right := left * totalTrips

	for left < right {
		mid := left + (right-left)/2
		if isPossible(mid, time, totalTrips) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return int64(left)
}

func isPossible(mid int, time []int, totalTrips int) bool {
	total := 0
	for _, t := range time {
		total += mid / t
	}

	return total >= totalTrips
}

func min(time []int) int {
	minVal := time[0]
	for _, t := range time {
		if t < minVal {
			minVal = t
		}
	}
	return minVal
}
