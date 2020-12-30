import crypto from 'crypto'
import fetch from 'node-fetch'

export function change(amount) {
  let result = [0, 0, 0, 0]
  if (amount < 0) {
    throw RangeError('Invalid Argument')
  }
  if (amount === 0) {
    return result
  }
  let coins = [25, 10, 5, 1]
  for (let x in coins) {
    let dividend = Math.floor(amount / coins[x])
    amount -= dividend * coins[x]
    result[x] = dividend
  }
  return result
}

export function stretched(input) {
  input = input.replace(/\s+/g, '')
  let result = ''
  for (let i = 0; i < input.length; i++) {
    result += input[i].repeat(i + 1)
  }
  return result
}

export function scramble(input) {
  let arr = input.split('').sort(function () {
    return 0.5 - Math.random()
  })
  input = arr.join('')
  return input
}

export function say(input) {
  let arr = []
  if (input) {
    arr.push(input)
    return function sayNext(nextInput) {
      if (nextInput) {
        arr.push(nextInput)
        return sayNext
      } else {
        return arr.join(' ')
      }
    }
  } else {
    return ''
  }
}

export function powers(base, limit, callback) {
  let value = 1
  while (value <= limit) {
    callback(value)
    value *= base
  }
}

export function interleave() {
  let arr = arguments[0]
  if (arguments.length === 1) {
    return arr
  }
  let index = 1
  for (let i = 1; i < arguments.length; i++) {
    if (arr.length >= index) {
      arr.splice(index, 0, arguments[i])
      index += 2
    } else {
      arr.push(arguments[i])
    }
  }
  return arr
}

//from https://cs.lmu.edu/~ray/notes/javascript/
export function* powersGenerator(base, limit) {
  let value = 1
  while (value <= limit) {
    yield value
    value *= base
  }
}

export function makeCryptoFunctions(key, algorithm, vector) {
  const e = function (input) {
    let cipher = crypto.createCipheriv(algorithm, key, vector)
    return cipher.update(input, 'utf-8', 'hex') + cipher.final('hex')
  }
  const d = function (input) {
    let decipher = crypto.createDecipheriv(algorithm, key, vector)
    return decipher.update(input, 'hex', 'utf-8') + decipher.final('utf-8')
  }
  return [e, d]
}

//helped by Sage
export function topTenScorers(statsObject) {
  return Object.entries(statsObject)
    .flatMap(([team, players]) => players.map((player) => [...player, team]))
    .filter((player) => player[1] >= 15)
    .map((player) => ({
      name: player[0],
      ppg: player[2] / player[1],
      team: player[3],
    }))
    .sort((sortedPlayer1, sortedPlayer2) => sortedPlayer2.ppg - sortedPlayer1.ppg)
    .slice(0, 10)
}

export async function multiply(x, y) {
  x = encodeURIComponent(x)
  y = encodeURIComponent(y)
  return fetch(`https://ordinary-hazel-pink.glitch.me/multiply?x=${x}&y=${y}`)
    .then((response) => response.json())
    .then((body) => {
      if ('result' in body) {
        return body.result
      } else {
        throw body
      }
    })
}
