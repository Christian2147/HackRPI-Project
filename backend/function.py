import random
import string

def assign_random_characters():
    all_characters = list(string.ascii_lowercase + string.digits + string.punctuation)
    shuffled_characters = list(all_characters)
    random.shuffle(shuffled_characters)
    return dict(zip(string.ascii_lowercase, shuffled_characters))

# Assign random characters to each letter in the alphabet
random_mapping = assign_random_characters()

# Display the original and shuffled alphabets
print("Original Alphabet: ", ' '.join(list(string.ascii_lowercase)))
print("Shuffled Alphabet: ", ' '.join([random_mapping[letter] for letter in string.ascii_lowercase]))

# List of common English words
english_words = ["which", "there", "their", "about", "would", "these", "other", "words", "could", "write", "first", "water",
    "after", "where", "right", "think", "three", "years", "place", "sound", "great", "again", "still", "every",
    "small", "found", "those", "never", "under", "might", "while", "house", "world", "below", "asked", "going",
    "large", "until", "along", "shall", "being", "often", "earth", "began", "since", "study", "night", "light",
    "above", "paper", "parts", "young", "story", "point", "times", "heard", "whole", "white", "given", "means",
    "music", "miles", "thing", "today", "later", "using", "money", "lines", "order", "group", "among", "learn",
    "known", "space", "table", "early", "trees", "short", "hands", "state", "black", "shown", "stood", "front",
    "voice", "kinds", "makes", "comes", "close", "power", "lived", "vowel", "taken", "built", "heart", "ready",
    "quite", "class", "bring", "round", "horse", "shows", "piece", "green", "stand", "birds", "start", "river",
    "tried", "least", "field", "whose", "girls", "leave", "added", "color", "third", "hours", "moved", "plant",
    "doing", "names", "forms", "heavy", "ideas", "cried", "check", "floor", "begin", "woman", "alone", "plane",
    "spell", "watch", "carry", "wrote", "clear", "named", "books", "child", "glass", "human", "takes", "party",
    "build", "seems", "blood", "sides", "seven", "mouth", "solve", "north", "value", "death", "maybe", "happy",
    "tells", "gives", "looks", "shape", "lives", "steps", "areas", "sense", "speak", "force", "ocean", "speed",
    "women", "metal", "south", "grass", "scale", "cells", "lower", "sleep", "wrong", "pages", "ships", "needs",
    "rocks", "eight", "major", "level", "total", "ahead", "reach", "stars", "store", "sight", "terms", "catch",
    "works", "board", "cover", "songs", "equal", "stone", "waves", "guess", "dance", "spoke", "break", "cause",
    "radio", "weeks", "lands", "basic", "liked", "trade", "fresh", "final", "fight", "meant", "drive", "spent",
    "local", "waxes", "knows", "train", "bread", "homes", "teeth", "coast", "thick", "brown", "clean", "quiet",
    "sugar", "facts", "steel", "forth", "rules", "notes", "units", "peace", "month", "verbs", "seeds", "helps",
    "sharp", "visit", "woods", "chief", "walls", "cross", "wings", "grown", "cases", "foods", "crops", "fruit",
    "stick", "wants", "stage", "sheep", "nouns", "plain", "drink", "bones", "apart", "turns", "moves", "touch",
    "angle", "based", "range", "marks", "tired", "older", "farms", "spend", "shoes", "goods", "chair", "twice",
    "cents", "empty", "alike", "style", "broke", "pairs", "count", "enjoy", "score", "shore", "roots", "paint",
    "heads", "shook", "serve", "angry", "crowd", "wheel", "quick", "dress", "share", "alive", "noise", "solid",
    "cloth", "signs", "hills", "types", "drawn", "worth", "truck", "piano", "upper", "loved", "usual", "faces",
    "drove", "cabin", "boats", "towns", "proud", "court", "model", "prime", "fifty", "plans", "yards", "prove",
    "tools", "price", "sheet", "smell", "boxes", "raise", "match", "truth", "roads", "threw", "enemy", "lunch",
    "chart", "scene", "graph", "doubt", "guide", "winds", "block", "grain", "smoke", "mixed", "games", "wagon",
    "sweet", "topic", "extra", "plate", "title", "knife", "fence", "falls", "cloud", "wheat", "plays", "enter",
    "broad", "steam", "atoms", "press", "lying", "basis", "clock", "taste", "grows", "thank", "storm", "agree",
    "brain", "track", "smile", "funny", "beach", "stock", "hurry", "saved", "sorry", "giant", "trail", "offer",
    "ought", "rough", "daily", "avoid", "keeps", "throw", "allow", "cream", "laugh", "edges", "teach", "frame",
    "bells", "dream", "magic", "occur", "ended", "chord", "false", "skill", "holes", "dozen", "brave", "apple",
    "climb", "outer", "pitch", "ruler", "holds", "fixed", "costs", "calls", "blank", "staff", "labor", "eaten",
    "youth", "tones", "honor", "globe", "gases", "doors", "poles", "loose", "apply", "tears", "exact", "brush",
    "chest", "layer", "whale", "minor", "faith", "tests", "judge", "items", "worry", "waste", "hoped", "strip",
    "begun", "aside", "lakes", "bound", "depth", "candy", "event", "worse", "aware", "shell", "rooms", "ranch",
    "image", "snake", "aloud", "dried", "likes", "motor", "pound", "knees", "refer", "fully", "chain", "shirt",
    "flour", "drops", "spite", "orbit", "banks", "shoot", "curve", "tribe", "tight", "blind", "slept", "shade",
    "claim", "flies", "theme", "queen", "fifth", "union", "hence", "straw", "entry", "issue", "birth", "feels",
    "anger", "brief", "rhyme", "glory", "guard", "flows", "flesh", "owned", "trick", "yours", "sizes", "noted",
    "width", "burst", "route", "lungs", "uncle", "bears", "royal", "kings", "forty", "trial", "cards", "brass",
    "opera", "chose", "owner", "vapor", "beats", "mouse", "tough", "wires", "meter", "tower", "finds", "inner",
    "stuck", "arrow", "poems", "label", "swing", "solar", "truly", "tense", "beans", "split", "rises", "weigh",
    "hotel", "stems", "pride", "swung", "grade", "digit", "badly", "boots", "pilot", "sales", "swept", "lucky",
    "prize", "stove", "tubes", "acres", "wound", "steep", "slide", "trunk", "error", "porch", "slave", "exist",
    "faced", "mines", "marry", "juice", "raced", "waved", "goose", "trust", "fewer", "favor", "mills", "views",
    "joint", "eager", "spots", "blend", "rings", "adult", "index", "nails", "horns", "balls", "flame", "rates",
    "drill", "trace", "skins", "waxed", "seats", "stuff", "ratio", "minds", "dirty", "silly", "coins", "hello",
    "trips", "leads", "rifle", "hopes", "bases", "shine", "bench", "moral", "fires", "meals", "shake", "shops",
    "cycle", "movie", "slope", "canoe", "teams", "folks", "fired", "bands", "thumb", "shout", "canal", "habit",
    "reply", "ruled", "fever", "crust", "shelf", "walks", "midst", "crack", "print", "tales", "coach", "stiff",
    "flood", "verse", "awake", "rocky", "march", "fault", "swift", "faint", "civil", "ghost", "feast", "blade",
    "limit", "germs", "reads", "ducks", "dairy", "worst", "gifts", "lists", "stops", "rapid", "brick", "claws"]

def generate_random_word():
    lower_english_words = [word.lower() for word in english_words]
    five_letter_words = [word for word in lower_english_words if len(word) == 5]
    word1 = random.choice(five_letter_words)
    return f"{word1}"

# Generate a random 5-letter word, a space, and another random 5-letter word from the English language
random_words = generate_random_word()
print(random_words)
print(len(english_words))

def encrypt_word(word, mapping):
    encrypted_word = ""
    for letter in word:
        if letter in mapping:
            encrypted_word += mapping[letter]
        else:
            encrypted_word += letter
    return encrypted_word

def decrypt_word(encrypted_word, reverse_mapping):
    decrypted_word = ""
    for letter in encrypted_word:
        if letter in reverse_mapping:
            decrypted_word += reverse_mapping[letter]
        else:
            decrypted_word += letter
    return decrypted_word

if __name__ == "__main__":
    # Generate a random 5-letter word, a space, and another random 5-letter word from the English language
    word1 = generate_random_word()
    word2 = generate_random_word()

    # Assign random characters to each letter in the alphabet
    random_mapping = assign_random_characters()

    # Encrypt the random words
    encrypted_word1 = encrypt_word(word1, random_mapping)
    encrypted_word2 = encrypt_word(word2, random_mapping)

    # Create a reverse mapping for decryption
    reverse_mapping = {v: k for k, v in random_mapping.items()}

    # Decrypt the encrypted words
    decrypted_word1 = decrypt_word(encrypted_word1, reverse_mapping)
    decrypted_word2 = decrypt_word(encrypted_word2, reverse_mapping)

    print(f"Encrypted word 1: {encrypted_word1}")
    print(f"Encrypted word 2: {encrypted_word2}")
    print(f"Decrypted word 1: {decrypted_word1}")
    print(f"Decrypted word 2: {decrypted_word2}")