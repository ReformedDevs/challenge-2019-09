package main

import (
  "fmt"
  "math/big"
  "time"
)

const max = int64(9000000000000000000)

func main() {
  start := time.Now()
  a := int64(3)
  b := int64(5)
  hold := int64(3)
  for true {
    next := a + b
    a = b
    b = next

    if b > max || b < a {
      break
    }

    switch b % 16 {
    case 3, 5, 11, 13:
    default:
      continue
    }

    // Miller-Rabin is accurate beyond the specified max.
    if !big.NewInt(b).ProbablyPrime(0) {
      continue
    }

    hold = b
  }

  fmt.Printf("cco3, Go, %v, %f,\n", hold, time.Since(start).Seconds())
}
