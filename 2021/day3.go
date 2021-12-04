package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
)
func ReadDay3(r io.Reader) ([]string) {

    scanner := bufio.NewScanner(r)
    
    var s string
    var str []string

    for scanner.Scan() {
        fmt.Sscanf(scanner.Text(), "%s", &s)

        str = append(str, s)
    }

    return str
}

func zero(a []int) ([]int) {
    for i:=0;i<len(a);i++{
        a[i]=0
    }
    return a
}

func main() {
    fd, _ := os.Open("day3")

    str := ReadDay3(fd)

    bits := len(str[0])
    samp := len(str)

    var bitmask uint = 0
    var count int
    var mask uint = 0
    var count_arr []int

    // Go thru each bit
    for j:=0; j<bits; j++ {
        count = 0

        // Go thru each line on the bit
        for i:=0; i<samp; i++ {
            if string(str[i][j]) == "1" {
                count++;
            }
        }
        count_arr = append(count_arr, count)
        
        // Majority? Add the bit
        if count > samp/2 {
            bitmask |= 1 << (bits-j-1)
            fmt.Println(bitmask,bits-j)
        }

    // inverter for bitmask
    mask |= 1 << j
    }

    fmt.Println(bitmask * (mask^bitmask))

    // Part 2 //
    


}





























