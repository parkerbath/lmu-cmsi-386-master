import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.IntStream;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.concurrent.atomic.AtomicInteger;

public class Exercises {

	public static List<Integer> change(int amount) {
		if (amount < 0) {
			throw new IllegalArgumentException("Amount cannot be negative");
		}
		var denominations = List.of(25, 10, 5, 1);
		var coinCounts = new ArrayList<Integer>();

		for (var denomination : denominations) {
			coinCounts.add(amount / denomination);
			amount %= denomination;
		}
		return List.copyOf(coinCounts);
	}

	public static String stretched(String s) {
		s = s.replaceAll("\\s+", "");
		StringBuilder result = new StringBuilder();
		AtomicInteger count = new AtomicInteger(1);
		s.codePoints().forEach(c -> {
			result.append(String.valueOf(Character.toChars(c)).repeat(count.intValue()));
			count.getAndIncrement();
		});
		return result.toString();
	}

	public static <T, U> Set<U> mapThenUnique(List<T> source, Function<T, U> mapper) {
		return source.stream().map(mapper).collect(Collectors.toSet());
	}

	public static void powers(int base, int limit, Consumer<Integer> consumer) {
		for (var power = 1; power <= limit; power *= base) {
			consumer.accept(power);
		}
	}

	public static IntStream powers(int base) {
		return IntStream.iterate(1, x -> x * base);

	}

	static class Sayer {
		private String result;

		Sayer(String text) {
			this.result = text;
		}

		String ok() {
			return result;
		}

		Sayer and(String text) {
			return new Sayer(this.result + " " + text);
		}
	}

	public static Sayer say(String text) {
		return new Sayer(text);
	}

	public static String say() {
		return "";
	}

	public static <T> T twice(Function<T, T> f, T x) {
		return f.apply(f.apply(x));
	}

	public static Optional<String> firstLongStringUppercased(int length, List<String> Strings) {
		return Strings.stream().filter(x -> x.length() > length).findFirst().map(i -> i.toUpperCase());

	}

	// from Toal's Sunday(10/25/20) lecture
	public static List<String> topTenScorers(Map<String, List<String>> Statistics) {
		return Statistics.entrySet().stream()
				.flatMap(stat -> stat.getValue().stream().map(player -> player + "," + stat.getKey()))
				.map(player -> player.split("\\s*,\\s*")).map(Player::new).filter(player -> player.games >= 15)
				.sorted((player1, player2) -> Double.compare(player2.getPPG(), player1.getPPG()))
				.map(player -> player.toString()).limit(10).collect(Collectors.toList());
	}

	private static class Player {
		String name;
		int games;
		int points;
		String team;

		Player(String[] attributes) {
			this.name = attributes[0];
			this.games = Integer.parseInt(attributes[1]);
			this.points = Integer.parseInt(attributes[2]);
			this.team = attributes[3];

		}

		// returns points over games in float format
		public float getPPG() {
			return (float) points / games;
		}

		public String toString() {
			return String.format("%s|%.2f|%s", this.name, this.getPPG(), this.team);
		}
	}
}
