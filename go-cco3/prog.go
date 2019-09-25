package main

import (
  "fmt"
  "math/big"
  "time"
)

const max = int64(9000000000000000000)
var cycles = []int{1, 2, 1, 8}

func main() {
  start := time.Now()
  fibs := [32]int64{}
  i := 0

  vals := []int64{2, 3}
  x := 1
  c := 0
  mainloop:
  for vals[x] < max {
    for i := 0; i < cycles[c]; i++ {
      x ^= 1
      vals[x] = vals[0] + vals[1]

      // Detect integer overflow.
      if vals[x] < 0 {
        break mainloop
      }
    }
    fibs[i] = vals[x]
    i += 1
    c = (c + 1) & 0x3
  }

  for i > 0 {
    i -= 1
    // Miller-Rabin is accurate beyond the specified max.
    if big.NewInt(fibs[i]).ProbablyPrime(0) {
      break
    }
  }

  fmt.Printf("cco3, Go, %v, %f,\n", fibs[i], time.Since(start).Seconds() * 1000)
}
