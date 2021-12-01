package main

import (
    "bufio"
    "fmt"
    "io"
    "strconv"
    "os"
)

// Read day1 input
func ReadInts(r io.Reader) ([]int, error) {
    // read file descriptor
    scanner := bufio.NewScanner(r)
    scanner.Split(bufio.ScanWords)

    var result []int
    for scanner.Scan() {
        // str2int
        x, err := strconv.Atoi(scanner.Text())
        if err != nil { return result, err }

        // add to array
        result = append(result, x)
    }
    return result, scanner.Err()
}

func inc(ints []int) (int) {
    var count int = 0
    for i := 0; i < len(ints)-1; i++ {
        if ints[i] < ints[i+1] {
            count++
        }
    }
    return count
}

func main() {
    fd, _ := os.Open("day1")
    ints, _ := ReadInts(fd)

    // Part 1
    fmt.Println(inc(ints))
    
    var win_sum []int
    var sum = 0
    // Part 2
    const win = 3;
    for i := 0; i < len(ints)-win+1; i++ {

        sum = 0
        for j := 0; j < win; j++ {
            sum += ints[i+j]
        }
        win_sum = append(win_sum, sum)
    }
    fmt.Println(inc(win_sum))
}
