twelve = [[
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, and ",
        "a Partridge in a Pear Tree."],
       ["zero", "first", "second", "third", "fourth",
        "fifth", "sixth", "seventh", "eighth", 
        "ninth", "tenth", "eleventh", "twelfth"]]


def recite(start_verse: int, end_verse: int) -> list[str]:
    song = [f"On the {twelve[1][i]} day of Christmas my true love gave to me: {''.join([x for x in twelve[0][-i:]])}"
            for i in range(start_verse, end_verse + 1)]
    return song
