### 1. On your machine, find the address of A[0][0] and A[3][7]. Explain why these values are what you found them to be.

```c++
struct {
int n;
char c;
} A[9][9];
```

> 1a)
> To find the addresses, we ran the short program below:

```c++
#include
using namespace std;
struct {
  int n;
  char c;
} A[9][9];

int main() {
cout << "Address of A[0][0] at our machine is "<< &(A[0][0]) << endl;
cout << "Address of A[3][7] at our machine is "<< &(A[3][7]) << endl;
}
```

> The addresses that we find on our machine are:
> Address of A[0][0] at our machine is 0x6011c0.
> Address of A[3][7] at our machine is 0x6012d0.
> The size of the element of the array is increased by 4 bytes because it is the int datatype. There
> are two ways to calculate the address of the two-dimensional arrays: by row and by column. For
> rows we have the formula: Address of A [ I ][ j ] = B + W _ [ N _ ( I – Lr ) + ( J – Lc ) ]
> B is the base address, I is the row, and J is the column where the address needs to be found. W
> is the storage size, Lr is the lower limit of the row, and Lc is the lower limit of the column. M is
> the number of row and N is the number of columns. In our code we have used the unary &
> operator along with the required address locations.

### 2. Rewrite these C++ declarations in Go.

```c++
double *a[n];
double (*b)[n];
double (*c())[n];
double (*d[n])();
double (_f(int (_)(int, int[]), int)) (int, ...);
```

> 2a)
> C++: double *a[n];
> Go: var a [n]*float64

> C++: double (*b)[n];
> Go: var (*b)[n]float64

> C++: double (_c())[n];
> Go: func c(arr . . ._ [n]float64)

> C++: double (*d[n])();
> Go: func d(arr . . . [n]*float64)

> C++: double (_f(int (_)(int, int[]), int)) (int, ...);
> Go: func f(*f (int, arr[]int), int, int))( int ... *float64)

### 3. What does this script print under (a) static scope rules and (b) dynamic scope rules?

```
var x = 1
function h() { var x = 9; return g() }
function f() { return x }
function g() { var x = 3; return f() }
print f()(h()) - x
```

> 3a) out: 0

> 3b) out: 2

### 4. Show the output of the following, assuming dynamic scope and (a) deep binding, and (b) shallow binding.

```
function g(h) {
  var x = 2
  h()
}

function main() {
  var x = 5
  function f() {
    print x + 3
  }
  g(f)
}

main()
```

> 4a) out: 8

> 4b) out: 5

### 5. Show the output of the following code fragment under the following four conditions: (a) pass by value, (b) pass by reference, (c) pass by value-result, and (d) pass-by-name.

```
x = 1
y = [2, 3, 4]
function f(a, b) { b++ ; a = x + 1 }
f(y[x], x)
print x, y[0], y[1], y[2]
```

> 5a) out: 1, 2, 3, 4

> 5b) out: 2, 2, 3, 4

> 5c) out: 2, 2, 2, 4

> 5d) out: 2, 2, 3, 3

### 6. Rewrite the following JavaScript function so that it uses only arrow functions with simple expressions, that is, no local variables and no statements and no side-effects. In other words, rewrite it into a more pure functional style. Note that this means you will replace error throwing with returning Swift-style result objects.

```javascript
function isPrime(n) {
  if (isNaN(n) || !Number.isInteger(n)) {
    throw 'Not an integer'
  } else if (n < 2 || n > Number.MAX_SAFE_INTEGER) {
    throw 'Number too big or too small'
  } else if (n === 2 || n === 3) {
    return true
  } else if (n % 2 === 0 || n % 3 === 0) {
    return false
  }
  for (let k = 5, w = 2; k \* k <= n; k += w, w = 6-w) {
    if (n % k === 0) {
      return false
    }
  }
  return true
}
```

> 6a) In JS:

```javascript
let isPrime = n => {
  if (isNaN(n) || !Number.isInteger(n)) {
    throws -> Not an integer
  } else if (n < 2 || n > Number.MAX_SAFE_INTEGER) {
    throws -> Small or too big
  }
  (n== 2 || n==3) ? 'true' : 'false'
  }
  {
    (n% 2 ==0 || n% ==0) ? 'false' : 'true'
  }
    n.foreach((element, index) => { (n%k == 0) ? ‘true’ : ‘false’
  });
return true;
}
```

### 7. Describe, in good English, and precise, erudite, and accurate language, why Python doesn't suffer from the billion-dollar mistake. Show me you understand the billion-dollar mistake. If you are working on a team, every single team member better contribute to or validate this answer. You need to understand this to pass the course, right?

> In Python, there is no null type. Instead of null, Python uses NoneType, which is used in place of null, but functions differently. NoneType contains the value None, which is not defined as any value; null, in other languages, is often defined as 0. None is also an object; functions can test if an object is None in Python. There is also only one None type; 0 does not pass for None, nor do any other values. Python allows
> programmers to test if an object is None by using the "obj is None" syntax, whereas 0, undefined, or other dubious values might pass for null in other languages.

### 8. Remember that old powers function you were asked to write so many times before? Here’s your chance to write it in either Go or Elixir. You’ll need to do some research because we have not covered these languages in much detail, but if/since you do/did the assigned readings, you will now have enough background. If you choose Go, simply give a small goroutine that writes, to a supplied channel, successive powers of a base starting at 1 (the power at exponent 0) and going up to some limit, e.g.

```go
powers(2, 70, ch)
```

> 8a) In Go:

```go
func powers (base, limit int, channel chan<- int) {
  result := 1;
  for result <= limit {
    channel <- result
    result *= base
  }
  close(channel)
}
```
