const START = process.hrtime()
const MAX = BigInt(9000000000000000000)

const list = [0, 1]
const primeList = []
let prev = 0
let curr = 1


function genPrimeFib(max) {
    for (i = 0; i < max; i++) {
        const next = prev + curr
        if (next > max) break
        prev = curr
        curr = next
        list.push(next)
        if (isPrime(next)) primeList.push(next)
    }
    return primeList
}

// 6k+1 optimization method
function isPrime(num) {
    if (num % 2 == 0 || num % 3 == 0) return false

    for (i = 5; (i * i) < num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false
    }
    return true
}


const fibList = genPrimeFib(MAX)
const solution = primeList.reverse()
    .map(num => (BigInt(num) * BigInt(num)).toString(16))
    .filter(num => num[num.length - 1] === '9')
    .filter((val, index) => index === 0)
    .map(num => Math.sqrt(parseInt(num, 16)))
    .join('')




console.log(`ashok, Node, ${solution}, ${process.hrtime(START) / 1000}, Scooby Power`)