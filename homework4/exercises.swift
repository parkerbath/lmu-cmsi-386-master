
struct NegativeAmountError: Error { }

func change(_ amount: Int) -> Result<(Int, Int, Int, Int), NegativeAmountError> {
    if amount < 0 {
        return .failure(NegativeAmountError())
	}
    let (quarters, remainder) = amount.quotientAndRemainder(dividingBy: 25)
    let (dimes, newRemainder) = remainder.quotientAndRemainder(dividingBy: 10)
    let (nickels, pennies) = newRemainder.quotientAndRemainder(dividingBy: 5)
    return .success((quarters, dimes, nickels, pennies))
}

extension String {
    var stretched: String {
        return self
            .filter { !$0.isWhitespace }
            .enumerated()
            .map { String(repeating: $1, count: $0 + 1 ) }
            .joined()
    }
}

extension Array {
    func mapThenUnique<T>(mapper: (Element) -> T) -> Set<T> {
        return Set(self.map(mapper))
    }
}

func powers(of base: Int, through limit: Int, then closure: (Int) -> Void) -> Void {
    var power = 1
    while power <= limit {
        closure(power)
        power *= base
    }
}

protocol Animal {
    var name: String { get }
    var sound: String { get }
}

extension Animal {
    func speak() -> String {
      return "\(name) says \(sound)"
    }
}

struct Horse: Animal {
    let name: String
    let sound = "neigh"
}

struct Cow: Animal {
    let name: String
    let sound = "moooo"
}

struct Sheep: Animal {
    let name: String
    let sound = "baaaa"
}

struct Sayer {
    var phrase: String = ""
    func and(_ word: String) -> Sayer {
        return Sayer(phrase: self.phrase + " " + word)
    }
}

func say(_ word: String) -> Sayer {
    return Sayer(phrase: word)
}

func twice<T>(_ f: (T) -> T, appliedTo x: T) -> T {
    return f(f(x))
}

func uppercasedFirst(of a: [String], longerThan length: Int) -> String? {
    return a.first ( where: { $0.count > length } )?.uppercased()
}
