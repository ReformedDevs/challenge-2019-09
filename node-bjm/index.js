// Problem
// Find the largest prime number in the Fibonacci sequence under
// 9,000,000,000,000,000,000 who's square, as hexidecimal, ends on 0x9.
// Output
// Use a .sh file to output: Author, Language, Result, Time, Notes
// Author should be your Github account name. Result should be an integer (no .0)
// Time should be in milliseconds. Notes do not need to be filled in, that's up to you.
// Usually people include things like single/multi thread or the algorithm used.

const MAX_PRIME = 9000000000000000000
const TEST_A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
const HEX_TEST = '9'
// console.log('MAX_PRIME', MAX_PRIME)

const START = Date.now()

const fibs = (max, list = []) => {
  if (!list.length) {
    // console.log('starting sequence')
    list = [{num: 0}, {num: 1}]
  }
  const l = list.length
  const next = list[l - 1].num + list[l - 2].num
  if (next >= max) { return list }
  const bn = BigInt(next)
  list.push({
    num: next,
    sqh: (bn * bn).toString(16)
  })
  return fibs(max, list)
}

function isPrime1(n) {
  if (isNaN(n) || !isFinite(n) || n % 1 || n < 2) return false;
  if (n % 2 === 0) return false
  if (n % 3 === 0) return false
  const m = Math.sqrt(n)
  let i = 5
  for (i; i <= m; i += 6) {
    if (n % i == 0) return false
    if (n % (i + 2) == 0) return false
  }
  return true
}

const fiblist = fibs(MAX_PRIME)
let answer
// const primelist = fiblist.filter(f => {
let x = fiblist.length - 1
for (x; x >= 0; x--) {
  const f = fiblist[x]
  if (f.num < 3) { continue }
  if (f.sqh[f.sqh.length - 1] !== HEX_TEST) { continue }
  if (f.num % 2 === 0) { continue }
  if (isPrime1(f.num)) {
    answer = f.num
    break
  }
}
// })

const TOTAL_TIME = Date.now() - START

// github_username, Python, 1597, 30, any notes about the implementation used

// console.log(primelist)
// console.log(fiblist.length, primelist.length)
console.log(`zombeej, Node, ${answer}, ${TOTAL_TIME}, blarg`)
// console.log('execution time in ms:', TOTAL_TIME)
