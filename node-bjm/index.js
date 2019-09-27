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

const START = process.hrtime.bigint()

// const fibs = (max, list = []) => {
//   if (!list.length) {
//     // console.log('starting sequence')
//     list = [{num: 0}, {num: 1}]
//   }
//   const l = list.length
//   const next = list[l - 1].num + list[l - 2].num
//   if (next >= max) { return list }
//   const bn = BigInt(next)
//   list.push({
//     num: next,
//     sqh: (bn * bn).toString(16)
//   })
//   return fibs(max, list)
// }

function fibs (max) {
  let current = 0, p1 = 0, p2 = 1, bc
  const list = []
  while (current < max) {
    current = p1 + p2
    bn = BigInt(current)
    p1 = p2
    p2 = current
    if (current % 2 &&
      current % 3 &&
      current % 5 &&
      current % 7 &&
      current % 11 &&
      current % 13 &&
      current % 17 &&
      current % 19 &&
      current % 23 &&
      current % 29 &&
      current % 31 &&
      current % 37) {
        const sqh = (bn * bn).toString(16)
        if (sqh[sqh.length - 1] === '9') {
          list.push(current)
        }
    }
  }
  return list
}

function isPrime1(n) {
  // if (isNaN(n) || !isFinite(n) || n % 1 || n < 2) return false;
  const m = Math.sqrt(n)
  let i = 5
  for (i; i <= m; i += 6) {
    if (n % i == 0) return false
    if (n % (i + 2) == 0) return false
  }
  return true
}

function isPrime2(n) {
  var k;
  var limit = Math.sqrt(n);
  for (k = 2; k <= limit; k += 1) {
    if (n % k === 0) {
      return false
    }
  }
  return true
}

function isPrime3(n) {
  return !(Array(n + 1).join(1).match(/^1?$|^(11+?)\1+$/))
}

const fiblist = fibs(MAX_PRIME)
// const FIBGEN = process.hrtime.bigint() - START
let answer
let x = fiblist.length - 1
for (x; x >= 0; x--) {
  const f = fiblist[x]
  if (isPrime1(f)) {
    answer = f
    break
  }
}

const TOTAL_TIME = (process.hrtime.bigint() - START).toString()

const TIME_STRING = parseInt(TOTAL_TIME) / 1000000

// github_username, Python, 1597, 30, any notes about the implementation used

// console.log(primelist)
// console.log(fiblist.length, primelist.length)
// console.log('FIBGEN', parseInt(FIBGEN.toString()) / 1000000)
// console.log(fiblist)
console.log(`zombeej, Node, ${answer}, ${TIME_STRING}, blarg`)
// console.log('execution time in ms:', TOTAL_TIME)
