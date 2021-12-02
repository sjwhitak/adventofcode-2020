package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
)
func ReadDay2(r io.Reader) ([]string, []int) {

    scanner := bufio.NewScanner(r)
    
    var s string
    var d int
    var str []string
    var dis []int

    for scanner.Scan() {
        fmt.Sscanf(scanner.Text(), "%s %d", &s, &d)

        str = append(str, s)
        dis = append(dis, d)
    }

    return str, dis
}

func main() {
    fd, _ := os.Open("day2")

    str, dis := ReadDay2(fd)


    var x_pos int = 0
    var y_pos int = 0

    for i := 0; i < len(str); i++ {
        if str[i] == "forward" {
            x_pos += dis[i]
        } else if str[i] == "down" {
            y_pos += dis[i]
        } else if str[i] == "up" {
            y_pos -= dis[i]
        }
    }
    fmt.Println(x_pos*y_pos)

    // Part 2
    var aim int = 0
    x_pos = 0
    y_pos = 0

    for i := 0; i < len(str); i++ {
        if str[i] == "forward" {
            x_pos += dis[i]
            y_pos += dis[i]*aim
        } else if str[i] == "down" {
            aim += dis[i]
        } else if str[i] == "up" {
            aim -= dis[i]
        }
    }
    fmt.Println(x_pos*y_pos)
}
