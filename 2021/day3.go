package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
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

func f_count_arr(s []string, bit int) (int){
// Return the count of the string array, `s` at the position `bit`

    var count int = 0

    for i:=0; i<len(s); i++ {
        if string(s[i][bit]) == "1" {
            count++
        }
    }
    return count 
}

func main() {
    fd, _ := os.Open("day3")

    str := ReadDay3(fd)

    bits := len(str[0])
    samp := len(str)

    var bitmask uint = 0
    var mask uint = 0
    var count_arr []int

    // Go thru each bit
    for j:=0; j<bits; j++ {

        // Go thru each line on the bit
        count := f_count_arr(str, j)
        
        count_arr = append(count_arr, count)
        
        // Majority? Add the bit
        if count*2 > samp {
            bitmask |= 1 << (bits-j-1)
        }

    // inverter for bitmask
    mask |= 1 << j
    }
    fmt.Println(bitmask * (mask^bitmask))

    // Part 2 //
    
    // Find majority of bits
    // "If 0 and 1 are equally common, keep values with 1"

    // go thru each bit
    for j:=0; j<bits; j++ {
        var new_str []string;
        count := f_count_arr(str, j)
        majority := count*2 >= samp
    
        // Update array
        for i:=0; i<samp; i++ {
            if majority {
                if string(str[i][j]) == "1" {
                    new_str = append(new_str, string(str[i]))
                }
            } else {
                if string(str[i][j]) == "0" {
                    new_str = append(new_str, string(str[i]))
                }
            }
        }
        samp = len(new_str)

        // check new array for majority
        str = new_str

        // End early
        if samp == 1 {
            break
        }
    }
    oxygen,_ := strconv.ParseUint(str[0], 2, bits)

    // Refresh string
    fd, _ = os.Open("day3")
    str = ReadDay3(fd)
    samp = len(str)

    for j:=0; j<bits; j++ {
        var new_str []string;
        count := f_count_arr(str, j)
        minority := count*2 < samp
    
        // Update array
        for i:=0; i<samp; i++ {
            if minority {
                if string(str[i][j]) == "1" {
                    new_str = append(new_str, string(str[i]))
                }
            } else {
                if string(str[i][j]) == "0" {
                    new_str = append(new_str, string(str[i]))
                }
            }
        }
        samp = len(new_str)

    
        // check new array for majority
        str = new_str


        // End early
        if samp == 1 {
            break
        }
    }
    c02,_ := strconv.ParseUint(str[0], 2, bits)

    fmt.Println(oxygen*c02)
}
