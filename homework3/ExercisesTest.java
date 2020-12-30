import java.util.HashMap;
import java.util.List; 
import java.util.ArrayList;
import java.util.Set;
import java.util.Map;
import java.util.Optional;

public class ExercisesTest extends TestSuite {
    public static void main(String[] args) {
        TestSuite.run(new ExercisesTest());
    }

    private static Map<String, List<String>> wnbaInput() {
        var stats = new HashMap<String, List<String>>();
        stats.put("ATL", List.of(
            "Betnijah Laney,16,263",
            "Courtney Williams,14,193"
        ));
        stats.put("CHI", List.of(
            "Kahleah Copper,17,267",
            "Allie Quigley,17,260",
            "Courtney Vandersloot,17,225"
        ));
        stats.put("CONN", List.of(
            "DeWanna Bonner,16,285",
            "Alyssa Thomas,16,241"
        ));
        stats.put("DAL", List.of(
            "Arike Ogunbowale,16,352",
            "Satou Sabally,12,153"
        ));
        stats.put("IND", List.of(
            "Kelsey Mitchell,16,280",
            "Tiffany Mitchell,13,172",
            "Candice Dupree,16,202"
        ));
        stats.put("LA", List.of(
            "Nneka Ogwumike,14,172",
            "Chelsea Gray,16,224",
            "Candace Parker,16,211"
        ));
        stats.put("LV", List.of(
            "A’ja Wilson,15,304",
            "Dearica Hamby,15,188",
            "Angel McCoughtry,15,220"
        ));
        stats.put("MIN", List.of(
            "Napheesa Collier,16,262",
            "Crystal Dangerfield,16,254"
        ));
        stats.put("NY", List.of(
            "Layshia Clarendon,15,18"
        ));
        stats.put("PHX", List.of(
            "Diana Taurasi,13,236",
            "Brittney Griner,12,212",
            "Skylar Diggins-Smith,16,261",
            "Bria Hartley,13,190"
        ));
        stats.put("SEA", List.of(
            "Breanna Stewart,16,317",
            "Jewell Loyd,16,223"
        ));
        stats.put("WSH", List.of(
            "Emma Meesseman,13,158",
            "Ariel Atkins,15,212",
            "Myisha Hines-Allen,15,236"
        ));
        return stats;
    }

    private static List<String> wnbaExpected = List.of(
        "Arike Ogunbowale|22.00|DAL",
        "A’ja Wilson|20.27|LV",
        "Breanna Stewart|19.81|SEA",
        "DeWanna Bonner|17.81|CONN",
        "Kelsey Mitchell|17.50|IND",
        "Betnijah Laney|16.44|ATL",
        "Napheesa Collier|16.38|MIN",
        "Skylar Diggins-Smith|16.31|PHX",
        "Crystal Dangerfield|15.88|MIN",
        "Myisha Hines-Allen|15.73|WSH"
    );

    @Override public TestSuite.Test[] getTests() {
        return new TestSuite.Test[] {

            new Test("Change works with 0", () -> {
                expectEqual(Exercises.change(0), List.of(0, 0, 0, 0));
            }), new Test("Change works with a bunch of values", () -> {
                expectEqual(Exercises.change(1), List.of(0, 0, 0, 1));
                expectEqual(Exercises.change(13), List.of(0, 1, 0, 3));
                expectEqual(Exercises.change(50), List.of(2, 0, 0, 0));
                expectEqual(Exercises.change(5), List.of(0, 0, 1, 0));
                expectEqual(Exercises.change(397), List.of(15, 2, 0, 2));
                expectEqual(Exercises.change(42), List.of(1, 1, 1, 2));
            }), new Test("Change works with a large number", () -> {
                expectEqual(Exercises.change(1000000017), List.of(40000000, 1, 1, 2));
            }), new Test("Change throws exception on negative argument", () -> expectThrows(
                () -> Exercises.change(-50),
                IllegalArgumentException.class, "Amount cannot be negative"

            )), new Test("Stretched works for blank strings", () -> {
                expectEqual(Exercises.stretched(""), "");
                expectEqual(Exercises.stretched("  "), "");
                expectEqual(Exercises.stretched("  \t\n  \t"), "");
            }), new Test("Stretched works for interesting strings, including emojis", () -> {
                expectEqual(Exercises.stretched("  Hi  hi  "), "Hiihhhiiii");
                expectEqual(Exercises.stretched("😁😂😱"), "😁😂😂😱😱😱");
                expectEqual(Exercises.stretched("hello world"),
                    "heelllllllooooowwwwwwooooooorrrrrrrrllllllllldddddddddd");

            }),  new Test("Map-then-unique works as expected", () -> {
                expectEqual(Exercises.mapThenUnique(List.of(2, 9, -9, 3), x -> x * x), Set.of(4, 9, 81));
                expectEqual(Exercises.mapThenUnique(List.of("abc", "Hi", "AbC"), String::toLowerCase),
                        Set.of("hi", "abc"));
                expectEqual(Exercises.mapThenUnique(List.of(), Math::sqrt), Set.of());

            }), new Test("Powers-with-consumer works as expected", () -> {
                var scratchPad = new ArrayList<Integer>();
                Exercises.powers(2, 64, scratchPad::add);
                expectEqual(scratchPad, List.of(1, 2, 4, 8, 16, 32, 64));
                scratchPad.clear();
                Exercises.powers(2, 63, scratchPad::add);
                expectEqual(scratchPad, List.of(1, 2, 4, 8, 16, 32));
                scratchPad.clear();
                Exercises.powers(-3, 343, scratchPad::add);
                expectEqual(scratchPad, List.of(1, -3, 9, -27, 81, -243));
                scratchPad.clear();

            }), new Test("Infinite stream version of powers works as expected", () -> {
                expectEqual(Exercises.powers(1).limit(5).toArray(),
                    new int[]{1, 1, 1, 1, 1});
                expectEqual(Exercises.powers(7).limit(10).toArray(),
                    new int[] { 1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607 });
                expectEqual(Exercises.powers(-3).limit(5).toArray(),
                    new int[] { 1, -3, 9, -27, 81 });
                expectEqual(Exercises.powers(10).limit(4).toArray(),
                    new int[] { 1, 10, 100, 1000 });

            }), new Test("Say returns empty string when no arguments", () -> {
                expectEqual(Exercises.say(), "");
            }), new Test("Say works with arguments", () -> {
                expectEqual(Exercises.say("A").ok(), "A");
                expectEqual(Exercises.say("A").and("B").ok(), "A B");
                expectEqual(Exercises.say("🐤🦇").and("$🦊👏🏽").and("!").ok(), "🐤🦇 $🦊👏🏽 !");

            }), new Test("Twice works for simple cases", () -> {
                expectEqual(Exercises.twice(x -> 2.0 * x, 5.0), 20.0);
                expectEqual(Exercises.twice(s -> s + "ee", "b"), "beeee");

            }),  new Test("First-long-uppercased works for simple cases", () -> {
                expectEqual(Exercises.firstLongStringUppercased(10, List.of()),
                    Optional.empty());
                expectEqual(Exercises.firstLongStringUppercased(5, List.of("hello", "world")),
                    Optional.empty());
                expectEqual(Exercises.firstLongStringUppercased(4, List.of("hello", "world")),
                    Optional.of("HELLO"));
                expectEqual(Exercises.firstLongStringUppercased(5, List.of("hello", "world!!")),
                    Optional.of("WORLD!!"));

            }), new Test("TopTenScorers works", () -> {
                expectEqual(Exercises.topTenScorers(Map.of()), List.of());
                expectEqual(Exercises.topTenScorers(wnbaInput()), wnbaExpected);
            }) 
        }; 
    }
}
