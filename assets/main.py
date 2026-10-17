

import pygame

from pathlib import Path

import numpy as np

pygame.init()

pygame.mixer.set_num_channels(16)



WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("A Day in Little F's Life")

clock = pygame.time.Clock()



# State: ASSETS — Base path for background images, UI artwork, portraits and sound files.
ASSETS = Path(__file__).resolve().parent / "assets"

# ==============================

# Background music: load the main soundtrack and control looping playback.

# ==============================



pygame.mixer.music.load(str(ASSETS / "background.ogg"))



pygame.mixer.music.set_volume(0.25)



# Function: play_background_music — Start the looping game soundtrack.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def play_background_music():

    """
    Start looping the main soundtrack after the player begins the game.
    """
    pygame.mixer.music.play(-1)







# Function: play_credits_music — Switch playback to the credits music.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def play_credits_music():

    # Stop the original background music

    """
    Load and play the credits track once, with a short fade-in.
    This helper is separate from the timed credits-transition playback.
    """
    pygame.mixer.music.fadeout(1000)



    # Load credits music

    pygame.mixer.music.load(

        str(ASSETS / "credits_music.ogg")

    )



    # Set credits music volume

    pygame.mixer.music.set_volume(0.35)



    # Fade in the new music

    pygame.mixer.music.play(

        loops=0,

        fade_ms=2000

    )





# ==============================

# Scene backgrounds and user interface assets: load images at game resolution.

# ==============================



# Function: load_background — Load a background image from assets and scale it to the game window.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def load_background(filename):

    """
    Load an opaque background image and resize it to the game window.
    The asset path is always resolved relative to main.py, not the terminal folder.
    """
    image = pygame.image.load(str(ASSETS / filename)).convert()

    return pygame.transform.smoothscale(image, (WIDTH, HEIGHT))





cover = load_background("cover.png")

scene1 = load_background("scene1.png")

scene2 = load_background("scene2.png")

scene3 = load_background("scene3.png")

scene4 = load_background("scene4.png")

scene5 = load_background("scene5.png")

scene6 = load_background("scene6.png")

scene7 = load_background("scene7.png")

# Scene 7 activity backgrounds: snack, chatting, sleeping, and studying.

scene7_eat = load_background("scene7_eat.png")

scene7_chat = load_background("scene7_chat.png")

scene7_sleep = load_background("scene7_sleep.png")

scene7_study = load_background("scene7_study.png")



scene8 = load_background("scene8.png")

# Scene 9: Afternoon
scene9 = load_background("scene9.png")

# Scene 10: After the afternoon class
scene10 = load_background("scene10.png")

# Scene 11: Special after-class event
scene11 = load_background("scene11.png")

# Scene 12: Normal after-class route
scene12 = load_background("scene12.png")

# Scene 13: Evening at the family dinner table.
scene13 = load_background("scene13.png")

# Scene 18: Little F is left to clean the classroom.
scene18 = load_background("scene18.png")

# Scene 17: Console incident background.
scene17 = load_background("scene17.png")

# Scene 19: Little F scrolling through his phone at night.
scene19 = load_background("scene19.png")

# Scene 20: Jiang wakes Little F after the morning lesson.
scene20 = load_background("scene20.png")

scene21 = load_background("scene21.png")

scene22 = load_background("scene22.png")

scene23 = load_background("scene23.png")

scene24 = load_background("scene24.png")

scene25 = load_background("scene25.png")

scene26 = load_background("scene26.png")

scene27 = load_background("scene27.png")
scene28 = load_background("scene28.png")


scene29 = load_background("scene29.png")
scene30 = load_background("scene30.png")


# =====================================
# COURTROOM UI ASSETS
# =====================================

objection_image = pygame.image.load(
    str(ASSETS / "objection.png")
).convert_alpha()

take_that_image = pygame.image.load(
    str(ASSETS / "take_that.png")
).convert_alpha()

hold_it_image = pygame.image.load(
    str(ASSETS / "hold_it.png")
).convert_alpha()

trial_inventory_image = pygame.image.load(
    str(ASSETS / "trial_inventory.png")
).convert_alpha()

# ==============================

# Bad-ending background images, selected when a character stat reaches zero.

# ==============================



bad_hunger = load_background("bad_hunger.png")

bad_energy = load_background("bad_energy.png")

bad_mood = load_background("bad_mood.png")

# Bad Ending 04: Homework inspection failure
bad_homework = load_background("bad_homework.png")

# Credits background

credits_image = load_background("credits.png")



# ==============================

# Four-option classroom menu: load button artwork and define clickable rectangles.

# ==============================



# Function: load_choice_ui — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def load_choice_ui(filename, size):

    """
    Load a transparent UI button image at the specified size.
    """
    image = pygame.image.load(

        str(ASSETS / filename)

    ).convert_alpha()

    return pygame.transform.scale(image, size)



CHOICE_UI_SIZE = (620, 110)



choice_eat_ui = load_choice_ui("choice_eat.png", CHOICE_UI_SIZE)

choice_chat_ui = load_choice_ui("choice_chat.png", CHOICE_UI_SIZE)

choice_sleep_ui = load_choice_ui("choice_sleep.png", CHOICE_UI_SIZE)

choice_study_ui = load_choice_ui("choice_study.png", CHOICE_UI_SIZE)

choice_ignore_her_ui = load_choice_ui("choice_ignore_her.png", CHOICE_UI_SIZE)
choice_talk_to_her_ui = load_choice_ui("choice_talk_to_her.png", CHOICE_UI_SIZE)

choice_eat_rect = choice_eat_ui.get_rect(center=(WIDTH // 2, 210))

choice_chat_rect = choice_chat_ui.get_rect(center=(WIDTH // 2, 330))

choice_sleep_rect = choice_sleep_ui.get_rect(center=(WIDTH // 2, 450))

choice_study_rect = choice_study_ui.get_rect(center=(WIDTH // 2, 570))

choice_accept_ui = load_choice_ui("choice_accept.png", CHOICE_UI_SIZE)
choice_decline_ui = load_choice_ui("choice_decline.png", CHOICE_UI_SIZE)


# Scene 23 quiz options
quiz_a_ui = load_choice_ui("抄作业.png", CHOICE_UI_SIZE)
quiz_b_ui = load_choice_ui("诚实做答.png", CHOICE_UI_SIZE)
quiz_c_ui = load_choice_ui("抄小孙的.png", CHOICE_UI_SIZE)

quiz_a_rect = quiz_a_ui.get_rect(center=(WIDTH // 2, 250))
quiz_b_rect = quiz_b_ui.get_rect(center=(WIDTH // 2, 390))
quiz_c_rect = quiz_c_ui.get_rect(center=(WIDTH // 2, 530))


# =====================================
# TUESDAY CLASS 7 - SINGLE CHOICE
# =====================================

tuesday_game_ui = load_choice_ui(
    "tuesday_game.png",
    (850, 285)
)

tuesday_game_rect = tuesday_game_ui.get_rect(
    center=(WIDTH // 2, HEIGHT // 2)
)

tuesday_game_choice_open = False



# =====================================
# CLASS 7 - CONSOLE OWNERSHIP CHOICES
# =====================================

CONSOLE_UI_SIZE = (850, 145)

console_a_ui = load_choice_ui(
    "console_a.png", CONSOLE_UI_SIZE
)

console_b_ui = load_choice_ui(
    "console_b.png", CONSOLE_UI_SIZE
)

console_a_rect = console_a_ui.get_rect(
    center=(WIDTH // 2, 310)
)

console_b_rect = console_b_ui.get_rect(
    center=(WIDTH // 2, 470)
)

# None = inactive, "accusation" = teacher dialogue,
# "choice" = player decision, "result" = branch dialogue.
console_event_stage = None
console_choice = None

# Scene 17: Delay the teacher's appearance.
SCENE17_DIALOGUE_DELAY = 2000
scene17_enter_time = 0


# =====================================
# HOMEWORK INSPECTION - CHOICE BUTTONS
# =====================================

HOMEWORK_UI_SIZE = (850, 145)

homework_a_ui = load_choice_ui(
    "homework_a.png", HOMEWORK_UI_SIZE
)

homework_b_ui = load_choice_ui(
    "homework_b.png", HOMEWORK_UI_SIZE
)

homework_c_ui = load_choice_ui(
    "homework_c.png", HOMEWORK_UI_SIZE
)

# Position the three buttons vertically.
homework_a_rect = homework_a_ui.get_rect(
    center=(WIDTH // 2, 240)
)

homework_b_rect = homework_b_ui.get_rect(
    center=(WIDTH // 2, 390)
)

homework_c_rect = homework_c_ui.get_rect(
    center=(WIDTH // 2, 540)
)



# =====================================
# SATURDAY TRANSITIONS
# =====================================

saturday_transition_start = 0
saturday_transition_background = None

saturday_court_start = 0
saturday_court_background = None

saturday_breakfast_active = False
saturday_court_ready = False

SATURDAY_FADE = 1500
SATURDAY_TITLE_FADE = 1200
SATURDAY_TITLE_HOLD = 1800
SATURDAY_BLACK_HOLD = 1000


# =====================================
# TUESDAY BREAKFAST - THREE CHOICE BUTTONS
# =====================================

TUESDAY_UI_SIZE = (800, 110)

tuesday_a_ui = load_choice_ui("tuesday_a.png", TUESDAY_UI_SIZE)
tuesday_b_ui = load_choice_ui("tuesday_b.png", TUESDAY_UI_SIZE)
tuesday_c_ui = load_choice_ui("tuesday_c.png", TUESDAY_UI_SIZE)

tuesday_a_rect = tuesday_a_ui.get_rect(center=(WIDTH // 2, 250))
tuesday_b_rect = tuesday_b_ui.get_rect(center=(WIDTH // 2, 390))
tuesday_c_rect = tuesday_c_ui.get_rect(center=(WIDTH // 2, 530))

# ==============================

# Status bar artwork: the frames are separate from their dynamic colored fills.

# ==============================



STATUS_UI_SIZE = (390, 130)



# Function: load_status_image — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def load_status_image(filename):

    """
    Load a transparent status-frame image using pixel-preserving scaling.
    """
    image = pygame.image.load(

        str(ASSETS / filename)

    ).convert_alpha()



    # Use nearest-neighbor scaling rather than smoothing so pixel-art edges remain crisp.

    return pygame.transform.scale(

        image, STATUS_UI_SIZE

    )





energy_ui = load_status_image("energy_bar.png")

hunger_ui = load_status_image("hunger_bar.png")

mood_ui = load_status_image("mood_bar.png")



# Load the WAKE UP quick-time-event overlay with its transparent background preserved.

wake_up_image = pygame.image.load(

    str(ASSETS / "wake_up.png")

).convert_alpha()



wake_up_image = pygame.transform.scale(

    wake_up_image, (1050, 530)

)



wake_up_rect = wake_up_image.get_rect(

    center=(WIDTH // 2, HEIGHT // 2)

)



start_button = pygame.image.load(

    str(ASSETS / "start_button.png")

).convert_alpha()



start_button = pygame.transform.smoothscale(

    start_button, (300, 100)

)



button_rect = start_button.get_rect(

    center=(WIDTH // 2, int(HEIGHT * 0.80))

)



dialogue_box = pygame.image.load(

    str(ASSETS / "dialogue_box.png")

).convert_alpha()



dialogue_box = dialogue_box.subsurface(

    dialogue_box.get_bounding_rect()

).copy()



BOX_WIDTH = 1180

BOX_HEIGHT = round(

    dialogue_box.get_height() * BOX_WIDTH / dialogue_box.get_width()

)



dialogue_box = pygame.transform.scale(

    dialogue_box, (BOX_WIDTH, BOX_HEIGHT)

)



box_rect = dialogue_box.get_rect(

    midbottom=(WIDTH // 2, HEIGHT - 20)

)

vape_icon = pygame.image.load(
    str(ASSETS / "mung_bean_vape.png")
).convert_alpha()


# Scene 24 - 60-point math test paper
test_paper_icon = pygame.image.load(
    str(ASSETS / "test_paper.png")
).convert_alpha()


font = pygame.font.SysFont("microsoftyahei", 28)

name_font = pygame.font.SysFont("microsoftyahei", 26)

hint_font = pygame.font.SysFont("microsoftyahei", 18)

title_font = pygame.font.SysFont("microsoftyahei", 64, bold=True)



# ==============================

# Character portrait system: look up emotion-specific PNGs and cache resized images.

# ==============================



PORTRAIT_DIR = ASSETS / "portraits"



PORTRAIT_SIZE = (350, 420)



# State: CHARACTER_FOLDER_MAP — Map dialogue speaker names to the corresponding portrait directories.
CHARACTER_FOLDER_MAP = {

    "Little F": "little_f",

    "Mom": "mom",

    "Dad": "dad",

    "Ms. Four-Eyesacher": "Ms. Four-Eyes",

    "jiang": "jiang",
    
    "Ouyang": "ouyang",

    "Sun": "sun",

    "Sun's Mom": "sun_mom",

    "Tang Jia Lao Si": "tang_jia_lao_si",

}



CHARACTER_SIDE_MAP = {

    "Little F": "left",

    "Mom": "right",

    "Dad": "right",

    "Ms. Four-Eyesacher": "right",

    "jiang": "right",

    "Ouyang": "right",

    "Sun": "right",

    "Sun's Mom": "right",
}



portrait_cache = {}



# Function: load_portrait — Load and cache a character portrait by name and expression; fall back to normal.png.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def load_portrait(character_name, expression):

    """
    Return a resized portrait for the requested speaker and expression.
    Use normal.png if the expression PNG does not exist; cache each result.
    If neither file is available, return None so dialogue still works.
    """
    folder_name = CHARACTER_FOLDER_MAP.get(character_name)

    if folder_name is None:

        return None



    key = (character_name, expression)



    if key in portrait_cache:

        return portrait_cache[key]



    portrait_path = (

        PORTRAIT_DIR

        / folder_name

        / f"{expression}.png"

    )



    if not portrait_path.exists():

        portrait_path = (

            PORTRAIT_DIR

            / folder_name

            / "normal.png"

        )



        if not portrait_path.exists():

            portrait_cache[key] = None

            return None



    image = pygame.image.load(str(portrait_path)).convert_alpha()

    image = pygame.transform.scale(image, PORTRAIT_SIZE)



    portrait_cache[key] = image

    return image



# ==============================

# Animalese dialogue audio: short letter sounds simulate speech during typewriter text.

# ==============================



VOICE_DIR = ASSETS / "voices"



# Map each dialogue speaker to a voice bank; update this mapping to customize voices.

# State: CHARACTER_VOICES — Map each speaker to an Animalese voice bank.
CHARACTER_VOICES = {

    "Little F": "light",

    "Dad": "deep",

    "Mom": "squeaky",

    "Ms. Four-Eyesacher": "squeaky",

    "jiang": "light",

    "Ouyang": "light",

    "Sun's Mom":"squeaky",

    "Tang Jia Lao Si": "deep",
}



VOICE_VOLUME = 0.45





# ==============================

# Teacher-specific pitch processing: make the squeaky voice more exaggerated.

# ==============================



TEACHER_NAME = "Ms. Four-Eyesacher"



# 1.0 keeps the source recording at its original pitch and duration.

# Around 1.4 raises the pitch noticeably and shortens each letter sound.

# Around 1.7 produces a much higher, cartoonishly shrill effect.

TEACHER_PITCH = 1.55

# Jiang's voice settings: bright, lively, and playful.
JIANG_PITCH = 1.35
JIANG_VOLUME = 0.55

# Dad's voice: deep, heavy, and authoritative.
DAD_PITCH = 1.5
DAD_VOLUME = 0.8


# =====================================
# SUN - NERDY, NASAL, LOW-PITCH VOICE
# =====================================

SUN_PITCH = 0.82
SUN_VOLUME = 0.65

sun_voice_cache = {}

dad_voice_cache = {}

jiang_voice_cache = {}



teacher_voice_cache = {}





# Function: get_teacher_sound — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_teacher_sound(letter):



    """
    Produce a higher-pitched version of the teacher's letter clip.
    Resample the existing squeaky sound and cache the result by letter.
    """
    letter = letter.lower()



    if letter in teacher_voice_cache:

        return teacher_voice_cache[letter]



    original = voice_sounds.get(

        "squeaky", {}

    ).get(letter)



    if original is None:

        return None




# Function: get_teacher_sound — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_teacher_sound(letter):
    """
    Generate and cache the teacher's exaggerated,
    high-pitched Animalese voice.
    """
    letter = letter.lower()

    if letter in teacher_voice_cache:
        return teacher_voice_cache[letter]

    original = voice_sounds.get("squeaky", {}).get(letter)

    if original is None:
        return None

    samples = pygame.sndarray.array(original)

    old_length = len(samples)
    new_length = max(1, int(old_length / TEACHER_PITCH))

    indices = np.linspace(
        0, old_length - 1, new_length
    ).astype(int)

    pitched_samples = np.ascontiguousarray(samples[indices])

    sound = pygame.sndarray.make_sound(pitched_samples)
    sound.set_volume(0.65)

    teacher_voice_cache[letter] = sound
    return sound



# Function: get_dad_sound — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_dad_sound(letter):
    """
    Generate a deep, heavy Animalese voice for Dad.

    Lower the pitch by extending each audio clip.
    Cache processed sounds for better performance.
    """
    letter = letter.lower()

    if letter in dad_voice_cache:
        return dad_voice_cache[letter]

    # Use the existing deep voice bank.
    original = voice_sounds.get("deep", {}).get(letter)

    if original is None:
        return None

    samples = pygame.sndarray.array(original)

    old_length = len(samples)

    # A pitch factor below 1.0 makes the sound lower.
    new_length = max(1, int(old_length / DAD_PITCH))

    # Resample the audio to the new duration.
    indices = np.linspace(
        0, old_length - 1, new_length
    ).astype(int)

    pitched_samples = np.ascontiguousarray(
        samples[indices]
    )

    sound = pygame.sndarray.make_sound(pitched_samples)
    sound.set_volume(DAD_VOLUME)

    dad_voice_cache[letter] = sound
    return sound


# Function: get_jiang_sound — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_jiang_sound(letter):
    """
    Generate and cache Jiang's bright,
    lively, higher-pitched Animalese voice.
    """
    letter = letter.lower()

    if letter in jiang_voice_cache:
        return jiang_voice_cache[letter]

    original = voice_sounds.get("light", {}).get(letter)

    if original is None:
        return None

    samples = pygame.sndarray.array(original)

    old_length = len(samples)
    new_length = max(1, int(old_length / JIANG_PITCH))

    indices = np.linspace(
        0, old_length - 1, new_length
    ).astype(int)

    pitched_samples = np.ascontiguousarray(samples[indices])

    sound = pygame.sndarray.make_sound(pitched_samples)
    sound.set_volume(JIANG_VOLUME)

    jiang_voice_cache[letter] = sound
    return sound


# Function: get_sun_sound — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_sun_sound(letter):
    """Generate Sun's slow, low, nerdy Animalese."""
    letter = letter.lower()

    if letter in sun_voice_cache:
        return sun_voice_cache[letter]

    # Use the existing tired voice bank.
    original = voice_sounds.get("tired", {}).get(letter)

    if original is None:
        return None

    samples = pygame.sndarray.array(original)

    old_length = len(samples)
    new_length = max(1, int(old_length / SUN_PITCH))

    indices = np.linspace(
        0, old_length - 1, new_length
    ).astype(int)

    pitched_samples = np.ascontiguousarray(
        samples[indices]
    )

    sound = pygame.sndarray.make_sound(pitched_samples)
    sound.set_volume(SUN_VOLUME)

    sun_voice_cache[letter] = sound
    return sound



    # Read raw audio samples from the preloaded Pygame Sound object.

    samples = pygame.sndarray.array(original)



    # Resample to fewer samples to increase pitch and shorten the clip; cache the result.

    old_length = len(samples)

    new_length = max(

        1, int(old_length / TEACHER_PITCH)

    )



    indices = np.linspace(

        0,

        old_length - 1,

        new_length

    ).astype(int)



    pitched_samples = np.ascontiguousarray(

        samples[indices]

    )



    sound = pygame.sndarray.make_sound(

        pitched_samples

    )



    sound.set_volume(0.65)



    teacher_voice_cache[letter] = sound



    return sound





# Reserve a mixer channel for voice effects so they can be stopped independently.

voice_channel = pygame.mixer.Channel(5)



# Load available per-letter OGG clips for all five voice banks into a lookup table.

voice_sounds = {}



for voice_type in ["light", "deep", "squeaky", "robot", "tired"]:



    voice_sounds[voice_type] = {}

    folder = VOICE_DIR / voice_type



    for char in "abcdefghijklmnopqrstuvwxyz0123456789":



        filename = folder / f"snd_{voice_type}_{char}.ogg"



        if filename.exists():

            sound = pygame.mixer.Sound(str(filename))

            sound.set_volume(VOICE_VOLUME)



            voice_sounds[voice_type][char] = sound




# Function: play_letter_sound — Play the voice-bank sound for each newly revealed alphanumeric character.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def play_letter_sound(character_name, letter):
    """
    Play an Animalese letter sound using the
    correct character-specific voice.
    """
    if not letter.isascii() or not letter.isalnum():
        return

    letter = letter.lower()

    if character_name == TEACHER_NAME:
        # High-pitched, exaggerated teacher voice.
        sound = get_teacher_sound(letter)

    elif character_name == "jiang":
        # Bright and playful Jiang voice.
        sound = get_jiang_sound(letter)
    elif character_name == "Sun":
        # Sun's slow and nerdy voice.
        sound = get_sun_sound(letter)
    elif character_name == "Dad":
        # Use Dad's deeper, heavier voice.
        sound = get_dad_sound(letter)

    else:
        # Default character voice.
        voice_type = CHARACTER_VOICES.get(
            character_name, "light"
        )

        sound = voice_sounds.get(
            voice_type, {}
        ).get(letter)

    if sound is not None:
        sound.play()











# Function: stop_voice — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def stop_voice():

    """
    Stop playback on the reserved character-voice mixer channel.
    """
    voice_channel.stop()







# ==============================

# Narrative dialogue data: entries contain a speaker, optional expression, and text.

# ==============================



# State: dialogues — Dialogue sequence currently presented to the player.
dialogues = [

    ("Little F", "Finish high school first...?"),

    ("Little F", "Interesting."),

]

# Preserve the original first-scene dialogue.
scene1_dialogues = dialogues.copy()

scene2_dialogues = [

    (

        "Little F",

        "Wait, seriously? Tang Jia Lao Si is coming? "

        "I still want to find out if the main character "

        "ends up ruling the whole world!"

    ),

]

# Scene 3 dialogue: the late-night argument between Little F and his mother.

scene3_dialogues = [

    ("Mom", "F! Have you completely lost your mind?! It's three in the morning! What the hell are you doing?!"),



    ("Little F", "Mom, please! Tang Jia Lao Si is coming to Xinhua Bookstore for a book signing! I'm begging you! Can you please take me there?"),



    ("Mom", "I don't give a damn who this Tang Jia Lao Si guy is! Your teacher called me to school FOUR TIMES just last week!"),



    ("Mom", "How about you stop making your teacher bother me before you even THINK about asking me for anything?!"),



    ("Mom", "And NOW! RIGHT THIS SECOND! GET YOUR ASS BACK TO BED!!!"),

]



# ==============================

# Scene 4 dialogue: Little F responds and makes a promise to himself.

# ==============================



scene4_dialogues = [

    ("Little F", "As the Invincible Old Man once said, a true man isn't defined by how many punches he can throw, but by how many punches he can take."),



    ("Little F", "Fine! If that's how you see me, then I'll prove you wrong! I'll make sure my teacher never calls you to school again!")

]



# Scene 5 dialogue: the morning wake-up after the opening QTE.

scene5_dialogues = [

    ("Little F", "normal", "I\\'m tired as hell... I\\'m never staying up this late again!"),

     ("Mom", "angry", "Little F! Breakfast is getting cold!"),



]

# ==============================

# Scene 6 dialogue: breakfast, hunger and energy warnings, and the teacher reminder.

# ==============================



scene6_dialogues = [

    ("Mom", "angry", "It's already 7:30! Are you going to school or what?!"),

    ("Mom", "normal", "Make sure you eat properly! Keep an eye on your hunger meter, or your stomach problems will act up again!"),

    ("Mom", "angry", "And NO JUNK FOOD! You hear me?!"),

    ("Mom", "normal", "And don't forget about your energy meter! Stop falling asleep in class!"),

    ("Mom", "angry", "Your math teacher told you to stay after school on Monday to correct your mistakes!"),

    ("Mom", "angry", "If you dare sneak off, you're gonna get your ass kicked when you get home!")

]

# ==============================

# Scene 7 opening dialogue: introduce the school day before offering choices.

# ==============================



scene7_dialogues = [

    ("Little F", "normal", "Time to go to school..."),

]





# Classroom branch: secretly eat a snack to offset the hunger loss.

scene7_eat_dialogues = [

    ("Little F", "happy", "Why the hell can't I get Song Jiang from these Water Margin collectible cards?!"),

    ("Ms. Four-Eyesacher", "normal", "Alright, class dismissed!"),

]



# Classroom branch: chat with classmates to offset the mood loss.

scene7_chat_dialogues = [

    ("Little F", "happy", "What a noob! You can't even beat me at tic-tac-toe!"),

    ("Ms. Four-Eyesacher", "normal", "Alright, class dismissed!"),

]



# Classroom branch: take a nap to offset the energy loss.

scene7_sleep_dialogues = [

    ("Little F", "normal", "Heh... I feel like I'm Evil Mark..."),

    ("Ms. Four-Eyesacher", "normal", "Alright, class dismissed!"),

]



# Classroom branch: study attentively without an extra stat recovery.

scene7_study_dialogues = [

    ("Little F", "angry", "Study hard and serve the motherland!"),

    ("Ms. Four-Eyesacher", "normal", "Alright, class dismissed!"),

]



# Opening dialogue for the second class.
scene7_second_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "class begin! Today we're going to learn about equilateral triangles!"
    ),
]

# =====================================
# TUESDAY - FIRST CLASS DIALOGUE
# =====================================

scene7_tuesday_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "you guys are the worst students I've ever seen!"
    ),
]

scene7_tuesday_second_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, everyone! Break time is over! Let's continue with our lesson!"
    ),
]



# =====================================
# THURSDAY - CLASS 11 OPENING
# =====================================

scene7_thursday_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "WHY DID OUR CLASS LOSE POINTS FOR CLEANLINESS AGAIN YESTERDAY?!"
    ),
]








# Scene 8 placeholder dialogue, reached only if no bad ending is triggered.

scene8_dialogues = [

    ("Little F", "normal", "Finally, that class is over!"),

]




# =====================================
# HOMEWORK INSPECTION EVENT - CLASS 2
# =====================================

homework_intro_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "mocking",
        "Alright, everyone! I'm going to check the homework I assigned yesterday!"
    ),
    (
        "Little F",
        "silent",
        "Oh crap... I didn't do any of it!"
    ),
]

homework_a_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "LITTLE F! WHY IS YOUR HOMEWORK COMPLETELY BLANK?!"
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "That's it! I'm calling your mother!"
    ),
]

homework_b_dialogues = [
    (
        "Little F",
        "normal",
        "Quick! I'll just scribble something down!"
    ),
    (
        "Ms. Four-Eyesacher", "angry", "HOW MANY TIMES HAVE I TAUGHT YOU THIS?! IT'S SUCH A SIMPLE QUESTION, AND YOU STILL GOT IT WRONG!!!"
    ),
]

homework_c_dialogues = [
    (
        "Little F",
        "normal",
        "Sorry, teacher... I forgot my homework at home."
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "AGAIN?! DO YOU THINK I'M STUPID?!"
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "I'm calling your mother RIGHT NOW!"
    ),
]

# Placeholder dialogue after successfully surviving inspection.
homework_survived_dialogues = [
    (
        "Little F",
        "silent",
        "That was way too close..."
    ),
]


# Scene 9: Afternoon
scene9_dialogues = [
    (
        "Little F",
        "silent",
        "Finally... It's afternoon already."
    ),

    ("Ms. Four-Eyesacher", "normal", "Come on, everyone! Wake up and pay attention! Let's get started with our afternoon lesson!"),
]



# =====================================
# FOURTH CLASS - OPENING DIALOGUE
# =====================================

scene9_fourth_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, everyone! Settle down! It's time for our next lesson!"
    ),
]


# Special conversation triggered only when the
# player chooses Chat during Class 4.
scene9_special_chat_dialogues = [
    (
        "Little F",
        "normal",
        "Hey, did you hear about what happened after school?"
    ),
    (
        "jiang",
        "shy",
        "There's this new uncle selling sizzling squid outside our school, and it's sooo good!"
    ),
    (
        "Little F",
        "happy",
        "Wait, seriously?"
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "QUIT TALKING! CLASS DISMISSED!"
    ),
]


# =====================================
# TUESDAY - CLASS 7 SPECIAL DIALOGUE
# =====================================

scene9_tuesday_class7_dialogues = [
    (
        "Ouyang",
        "smug",
        "Yo, Little F! Check this shit out! The new Swish!"
    ),
    (
        "Little F",
        "happy",
        "Damn, that's sick! Let's give it a try!"
    ),
  (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, everyone! Settle down! It's time for our next lesson!"
    ),
]


# =====================================
# CLASS 7 - CONSOLE INCIDENT DIALOGUES
# =====================================

# Teacher catches Little F and Ouyang playing.
console_accusation_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "ARE YOU TWO OUT OF YOUR MINDS?! "
        "HOW DARE YOU BRING A GAME CONSOLE TO SCHOOL?!"
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "TELL ME THE TRUTH! "
        "WHO DOES THIS THING BELONG TO?!"
    ),
]

# Option A: Little F takes the blame.
console_a_dialogues = [
    (
        "Ouyang",
        "happy",
        "You're my true bro, Little F!"
    ),
    (
        "Ms. Four-Eyesacher",
        "angry",
        "YOU'RE DONE FOR! "
        "GET YOUR MOTHER DOWN HERE!"
    ),
]

# Option B: Little F blames Ouyang.
console_b_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "OUYANG! BRING YOUR PARENTS HERE AFTER CLASS!"
    ),
    (
        "Ouyang",
        "angry",
        "Little F, you absolute bastard! "
        "I was nice enough to let you play, "
        "and you actually ratted me out?! "
        "Just you wait!"
    ),
]


# =====================================
# SCENE 10 - AFTERNOON CLASS DISMISSED
# =====================================

scene10_dialogues = [
    (
        "Little F",
        "silent",
        "I think i gonna die..."
    ),
]

# Dialogue displayed after reaching Bad Ending 04.
bad_homework_dialogues = [
    (
        "Little F",
        "cry",
        "I'm so dead when Mom gets here..."
    ),
]



# =====================================
# SCENE 11 - NORMAL ROUTE
# =====================================

scene11_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "Hurry up and write it properly! I don't want to see any more mistakes!"
    ),
    (
        "Little F",
        "cry",
        "I'm starving to death! I can't even think straight!"
    ),
]


# =====================================
# SCENE 12 - SQUID EVENT WITH JIANG
# =====================================

scene12_dialogues = [
    (
        "Little F",
        "happy",
        "OH MY GOD! THIS IS SO FREAKING DELICIOUS!"
    ),
    (
        "jiang",
        "happy",
        "See? I told you!"
    ),
]



# =====================================
# SCENE 13 - EVENING DINNER
# =====================================

scene13_dialogues = [
    (
        "Little F",
        "cry",
        "Finally, I get to eat something after a long day of school and classes!"
    ),
]



scene14_dialogues = [
    (
        "Little F",
        "normal",
        "Phew... This exhausting Monday is finally over..."
    ),
]


# =====================================
# THURSDAY NIGHT - BEDROOM
# =====================================

scene14_thursday_dialogues = [
    (
        "Little F",
        "silent",
        "What a long day... My legs are killing me."
    ),
]


scene15_dialogues = [
    (
        "Little F",
        "silent",
        "Aaaaah! I woke up with a stiff neck!"
    ),

]

scene16_mom_dialogues = [
    (
        "Mom",
        "normal",
        "I heard your cousin on your second uncles side dropped out of school because of depression."
        "Kids these days are so fragile! How come we never heard of so many mental health problems back in our day?"
    ),

]

# Father's response is identical for all three choices.
scene16_dad_dialogues = [
    (
        "Dad",
        "angry",
        "Enough already! Hurry up and finish your breakfast!"
    ),
]



# =====================================
# THURSDAY - NEW BREAKFAST DIALOGUE
# =====================================

scene6_thursday_dialogues = [
    (
        "Mom",
        "normal",
        "Little F, I've signed you up for three new tutoring "
        "classes next week. Don't forget to go!"
    ),
    (
        "Dad",
        "angry",
        "What's the point of signing someone like him up "
        "for extra classes? It's just a waste of money!"
    ),
]


# =====================================
# TUESDAY - CLASS 7 DISMISSAL
# =====================================

scene9_tuesday_dismissal_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, class dismissed!"
    ),
]


# =====================================
# THURSDAY - CLASS 9 AFTER-CLASS EVENT
# =====================================

class9_ouyang_dialogues = [
    (
        "Ouyang",
        "smug",
        "Little F, this is hilarious! "
        "You slept through the entire morning and missed PE! "
        "The PE teacher said you've gotta run ten laps "
        "around the field after school!"
    ),
    (
        "Little F",
        "silent",
        "Alright,alright.... "
    ),
    
]

# =====================================
# THURSDAY - CLASS 10 OPENING
# =====================================

class10_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, everyone! Time for our last class of the day!"
    ),
]


# =====================================
# SCENE 18 - CLASSROOM CLEANING
# =====================================

scene18_dialogues = [
    (
        "Little F",
        "silent",
        "Why the hell am I the only one who has to clean up?!"
    ),
]

# ==============================

# BAD ENDING DIALOGUES

# ==============================



# Bad Ending 1: Hunger reaches zero

bad_hunger_dialogues = [

    ("Little F", "silent", "My stomach... It hurts so bad..."),

    ("Little F", "cry", "If only I could make it there..."),

]



# Bad Ending 2: Energy reaches zero

bad_energy_dialogues = [

    ("Little F", "silent", "I... can't keep my eyes open..."),

    ("Ms. Four-Eyesacher", "angry", "Little F! You've got some nerve! Get your mother down here RIGHT NOW!"),

]



# Bad Ending 3: Mood reaches zero

bad_mood_dialogues = [

    ("Little F", "angry", "I'm so sick of all this..."),

    ("Little F", "happy", "Teyvat, here I come...!"),

]



# =====================================
# TUESDAY EVENING - FAMILY DINNER
# =====================================

scene13_tuesday_dialogues = [
    (
        "Dad",
        "normal",
        "Business hasn't been going so well this year..."
    ),
    (
        "Little F",
        "silent",
        "..."
    ),
]

# =====================================
# TUESDAY NIGHT - BEDROOM
# =====================================

scene14_tuesday_dialogues = [
    (
        "Little F",
        "silent",
        "Another day finally over..."
    ),
]


# =====================================
# SCENE 19 - LATE NIGHT PHONE CHAT
# =====================================

scene19_dialogues = [
   (
        "Lone Wolf",
        "normal",
        "You guys know that Little F is a total piece of shit, right? "
        "He got his game console confiscated and then tried to blame someone else!"
    ),
    (
        "Invincible T-Rex",
        "normal",
        "Right?! I heard he even got caught jerking off in class back in elementary school! "
        "No wonder he turned out like this!"
    ),
    (
        "Piggy",
        "normal",
        "No way... Are you sure that's true? "
        "I don't think it's right to talk about him like that..."
    ),
    (
        "Demon King",
        "normal",
        "What, do you have a crush on him or something? "
        "Why are you defending him? "
        "That loser is never gonna amount to anything anyway."

    ),
        (
        "Little F",
        "silent",
        "..."
    ),
]  


# =====================================
# FRIDAY - BREAKFAST
# =====================================

scene6_friday_dialogues = [
    (
        "Mom",
        "normal",
        "I heard your school is setting up study groups. "
        "Have you joined one?"
    ),
]




# =====================================
# FRIDAY - SCHOOL MONTAGE DIALOGUES
# =====================================

friday_school_intro_dialogues = [
    (
        "Little F",
        "happy",
        "Friday! Friday! Friday! Friday! "
        "Book signing! Book signing! Book signing!"
    ),
]

friday_school_end_dialogues = [
    (
        "Little F",
        "normal",
        "Today went by kinda fast... "
        "What did we even learn in class?"
    ),
]


# =====================================
# FRIDAY NIGHT - IGNORE JIANG ROUTE
# =====================================

friday_home_dinner_dialogues = [
    (
        "Mom",
        "angry",
        "Even Ouyang joined the study group! "
        "Why didn't you?! And you still have the nerve to come home?!"
    ),
    (
        "Little F",
        "silent",
        "H-how was I supposed to know?! "
        "Nobody even told me!"
    ),
    (
        "Mom",
        "angry",
        "What, are your ears growing out of your ass?! "
        "Since you hate studying so much, "
        "you're not going ANYWHERE this weekend!"
    ),
    (
        "Little F",
        "cry",
        "NOOO... PLEASE..."
    ),
]

# =====================================
# FRIDAY NIGHT - STUDY GROUP ROUTE
# =====================================

friday_study_group_intro_dialogues = [
    (
        "jiang",
        "happy",
        "Little F! You're here! We've all been waiting for you!"
    ),
    (
        "Sun's Mom",
        "normal",
        "Go on, have a seat."
    ),
]

friday_study_group_insult_dialogues = [
    (
        "Sun's Mom",
        "normal",
        "Hey, Jiang's mom, why is this kid here too? "
        "He never seemed very bright to me."
    ),
    (
        "Little F",
        "silent",
        "..."
    ),
]

# =====================================
# FRIDAY NIGHT - FINAL BEDROOM DIALOGUE
# =====================================

friday_final_bedroom_dialogues = [
    (
        "Little F",
        "angry",
        "Even if they begged me to go, I wouldn't want to!"
    ),
]



# =====================================
# SATURDAY - THE WEEKEND TRIAL
# =====================================

saturday_breakfast_dialogues = [
    (
        "Little F",
        "happy",
        "Mom! Remember what you promised me last week?"
    ),
    (
        "Mom",
        "normal",
        "I forgot. Your mom's been busy as hell all day!"
    ),
    (
        "Little F",
        "happy",
        "The book signing! The Invincible Old Man's book signing! "
        "You promised I could go! "
        "And I made it through the whole week without "
        "getting you called into school!"
    ),
    (
        "Mom",
        "thinking",
        "Do you really think... "
        "you've behaved well enough?"
    ),
    (
        "Dad",
        "normal",
        "ENOUGH ARGUING! "
        "LET THE TRIAL BEGIN!!!"
    ),
]




# =====================================
# FINAL CHAPTER - THE WEEKEND TRIAL
# =====================================

trial_opening_dialogues = [
    ("Dad", "normal",
     "The case of whether Little F deserves to attend "
     "the book signing this weekend is now officially in session! "
     "First, I call the plaintiff, Mom!"),

    ("Mom", "angry",
     "Hmph! I think the evidence is already clear. "
     "There's no reason for Little F to go today!"),

    ("Little F", "angry",
     "OBJECTION! Your Honor, I demand testimony!"),

    ("Dad", "normal",
     "Since you insist, the testimony shall now begin!"),

    ("Mom", "angry",
     "First of all, you haven't come home on time "
     "even once since Monday! Especially on Friday! "
     "You didn't get home until nine o'clock!"),

    ("Little F", "angry",
     "OBJECTION! I was attending the study group on Friday!"),

    ("Mom", "thinking",
     "What? Oh... I think I forgot about that..."),

    ("Dad", "normal",
     "Order! Order! I'll let that one slide."),

    ("Mom", "angry",
     "HOLD IT! But have your grades improved at all this week?")
]

trial_evidence_dialogues = [
    ("Little F", "thinking",
     "Wait... I think I've got something that proves it. "
     "It's time to show her!")
]

trial_no_evidence_dialogues = [
    ("Little F", "sad",
     "Well... when you put it that way, "
     "I guess I really haven't...")
]

trial_present_dialogues = [
    ("Little F", "happy",
     "TAKE THAT! Here's my Thursday math test! "
     "Take a good look!"),

    ("Mom", "surprise",
     "You actually passed?! I... I guess I lost. "
     "Fine, you can go."),

    ("Dad", "normal",
     "Very well! Since there are no further objections, "
     "I hereby declare that Little F may attend "
     "the manga book signing!")
]



# =====================================
# SCENE 30 - FINAL BOOK SIGNING
# =====================================

scene30_dialogues = [
    (
        "Little F",
        "happy",
        "Mr. Tang! So, did the Invincible Old Man "
        "ever finish middle school?"
    ),
    (
        "Tang Jia Lao Si",
        "normal",
        "Uh... No. Because I never went to middle school "
        "myself, so I had no idea how to write that part..."
    ),
    (
        "Little F",
        "silent",
        "....."
    ),
]

# =====================================
# THURSDAY - MORNING DIALOGUES
# =====================================

thursday_mom_dialogues = [
    (
        "Mom",
        "angry",
        "Were you secretly playing on your phone again last night?! "
        "It's already eight o'clock! Forget breakfast! "
        "Get your ass to school RIGHT NOW!!!"
    ),
]

thursday_class_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "mocking",
        "Just look at the state of you lot! I bet none of you have been focusing on your studies!"
    ),
]


# =====================================
# CLASS 8 - FALLING ASLEEP
# =====================================

class8_sleep_dialogues = [
    (
        "Little F",
        "silent",
        "I'm so sleepy... I really shouldn't have stayed up so late..."
    ),
]

# =====================================
# SCENE 20 - JIANG WAKES LITTLE F
# =====================================

scene20_dialogues = [
    (
        "jiang",
        "helpless",
        "Are you crazy?! You've been asleep all morning!"
    ),
]


# =====================================
# SCENE 21 - TRACK RUNNING EVENT
# =====================================

scene21_dialogues = [
    (
        "Little F",
        "cry",
        "My legs... I think they've disappeared..."
    ),
    (
        "Little F",
        "normal",
        "Huh? Isn't that Xiao Jiang? What's she doing over there?"
    ),
]

scene21_ignore_dialogues = [
    (
        "Little F",
        "silent",
        "Looks like she walked away..."
    ),
]

scene21_talk_dialogues = [
    (
        "jiang",
        "normal",
        "Ms. Four-Eyesacher said this morning that she's forming a study group. You should come with us."
    ),
    (
        "jiang",
        "happy",
        "By the way, it's getting late. You must be hungry. Here, have my cake."
    ),
]


scene22_dialogues = [
    (
        "Ouyang",
        "smug",
        "Little F, look at this. It's the newest vape — milk tea cup style. Mung bean cake flavor. Wanna try it?"
    ),
]

scene22_accept_dialogues = [
    (
        "Little F",
        "normal",
        "Cough cough cough... who even likes this stuff?"
    ),
]

scene22_decline_dialogues = [
    (
        "Little F",
        "normal",
        "I'm not one of those troublemakers. No thanks."
    ),
]

scene7_thursday_second_class_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, class, settle down. Let's continue with the next lesson."
    ),
]
# =====================================
# THURSDAY DINNER VARIANTS (SCENE 13)
# =====================================

scene13_thursday_ignore_dialogues = [
    (
        "Mom",
        "angry",
        "It's almost 9 o'clock again. No dinner for you tonight. Go back to your room."
    ),
]

scene13_thursday_talk_dialogues = [
    (
        "Mom",
        "normal",
        "You worked hard today. Come and eat."
    ),
]
# =====================================
# CLASS 9 - THURSDAY AFTERNOON
# =====================================

thursday_afternoon_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "normal",
        "Alright, everyone! Let's start our afternoon lesson!"
    ),
]



# =====================================
# THURSDAY - CLASS 13 & WEEKLY QUIZ
# =====================================

class13_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "smug",
        "It's finally time for our weekly quiz! "
        "Put all your books away, NOW!!!"
    ),
]

sun_quiz_intro_dialogues = [
    (
        "Sun",
        "happy",
        "Hey, Little F! Have you heard about that new milk tea cup vape? "
        "I've always wanted to try one, but I don't know where to buy it."
    ),
]

sun_quiz_accept_dialogues = [
    (
        "Sun",
        "surprise",
        "Whoa! How did you get one of those?! "
        "Give it to me, and I'll let you copy my answers "
        "in the next quiz!"
    ),
]

sun_quiz_decline_dialogues = [
    (
        "Little F",
        "normal",
        "I don't have that thing. Just go away."
    ),
]

scene23_a_dialogues = [
    (
        "Ms. Four-Eyesacher",
        "angry",
        "YOU'RE CHEATING AGAIN?! "
        "GET YOUR MOTHER HERE AND SHOW HER WHAT YOU'VE DONE!"
    ),
]

scene23_b_dialogues = [
    (
        "Little F",
        "cry",
        "This is so hard... Why can't I answer any of these questions?! "
        "I'm so screwed!!!"
    ),
]

scene23_c_dialogues = [
    (
        "Little F",
        "happy",
        "Huh, this test is surprisingly easy!"
    ),
]


# =====================================
# SCENE 24 - EXAM RESULTS
# =====================================

scene24_honest_dialogues = [
    (
        "Little F",
        "sad",
        "30 points... What am I supposed to do now...?"
    ),
]

scene24_cheat_dialogues = [
    (
        "Little F",
        "happy",
        "60 points! Not bad at all!"
    ),
]

scene14_quiz_night_dialogues = [
    (
        "Little F",
        "sad",
        "I don't even feel like eating... I'm so depressed..."
    ),
]


# Match each bad ending with its dialogue list

# State: BAD_ENDING_DIALOGUES — Map a bad-ending identifier to its dialogue sequence.
BAD_ENDING_DIALOGUES = {

    "bad_hunger": bad_hunger_dialogues,

    "bad_energy": bad_energy_dialogues,

    "bad_mood": bad_mood_dialogues,

    "bad_homework": bad_homework_dialogues,

}





# State: dialogue_index — Index of the active line in the dialogue sequence.
dialogue_index = 0

text_start = 0



# Typewriter interval in milliseconds per character; smaller values display text faster.

CHAR_INTERVAL = 60





# ==============================

# Player stats: hunger, energy, and mood are clamped to the 0–100 range.

# ==============================



hunger = 100

energy = 100

mood = 100



stats_enabled = False





# ==============================

# Class settlement animation: interpolate displayed stats independently of actual stats.

# ==============================



SETTLEMENT_DURATION = 800   # 变化持续0.8秒

SETTLEMENT_HOLD = 1000      # 结算后停留1秒



settlement_active = False

settlement_start = 0



settlement_from = (100, 100, 100)

settlement_to = (100, 100, 100)



# Display-only stat values; they move smoothly while the underlying stats update immediately.

display_hunger = 100

display_energy = 100

display_mood = 100





# =====================================
# TRIAL STATE
# =====================================

trial_inventory_open = False
trial_flash_kind = None
trial_flash_start = 0
trial_last_line = None

TRIAL_FLASH_DURATION = 850

trial_fade_start = 0
trial_fade_target = None
trial_fade_background = None

TRIAL_FADE_DURATION = 1300
TRIAL_BLACK_HOLD = 1000

scene29_start = 0
SCENE29_HOLD = 2500



# Function: change_stats — Update hunger, energy and mood, clamping each score between 0 and 100.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def change_stats(hunger_change=0, energy_change=0, mood_change=0):

    """
    Apply permanent changes to the three gameplay stats.
    Clamp each new value between 0 and 100, then print the result.
    """
    global hunger, energy, mood



    hunger = max(0, min(100, hunger + hunger_change))

    energy = max(0, min(100, energy + energy_change))

    mood = max(0, min(100, mood + mood_change))



    print(

        f"Hunger: {hunger}% | "

        f"Energy: {energy}% | "

        f"Mood: {mood}%"

    )



# Function: restore_stats_after_sleep — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def restore_stats_after_sleep():
    """
    Restore 10 points to each stat after waking up.

    The player's current stats are preserved.
    Every value is capped at 100.
    """
    global display_hunger, display_energy, display_mood

    # Apply the daily morning recovery.
    change_stats(
        hunger_change=10,
        energy_change=10,
        mood_change=10
    )

    # Synchronize the visible status bars.
    display_hunger = hunger
    display_energy = energy
    display_mood = mood

    print("MORNING RECOVERY: All stats +10")






# ==============================

# Bad-ending detection: select the ending associated with the first depleted stat.

# ==============================



# State: pending_bad_ending — Identifier for a bad ending queued to play.
pending_bad_ending = None





# Function: check_bad_ending — Detect a depleted stat and queue the appropriate bad ending.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def check_bad_ending():

    """
    Set a pending bad ending if any gameplay stat has reached zero.
    Priority is hunger, then energy, then mood when multiple stats are empty.
    """
    global pending_bad_ending



    # Do not overwrite an ending that has already been selected.

    if pending_bad_ending is not None:

        return



    if hunger <= 0:

        pending_bad_ending = "bad_hunger"



    elif energy <= 0:

        pending_bad_ending = "bad_energy"



    elif mood <= 0:

        pending_bad_ending = "bad_mood"



    if pending_bad_ending:

        print("BAD ENDING:", pending_bad_ending)





# ==============================

# Bad-ending transition timing: fade to black, hold, then fade in the ending image.

# ==============================



BAD_FADE_OUT = 1000   # 1秒逐渐变黑

BAD_BLACK_HOLD = 2000 # 黑屏停留2秒

BAD_FADE_IN = 1500    # 1.5秒逐渐显示坏结局





bad_transition_start = 0

bad_transition_target = None

bad_transition_background = None



# Credits transition settings

CREDITS_FADE_OUT = 1000

CREDITS_BLACK_HOLD = 2000

CREDITS_FADE_IN = 1500



credits_transition_start = 0

credits_transition_background = None



credits_music_started = False



# ==============================
# CLASS PROGRESSION SYSTEM
# ==============================

class_number = 1
MAX_CLASSES = 2


# =====================================
# AFTERNOON SPECIAL EVENT FLAGS
# =====================================

# Tracks whether the player discovers the special
# conversation during the fourth class.
afternoon_chat_triggered = False


# ==============================

# Class activity rules: apply base penalties once and compensate based on the chosen activity.

# ==============================

# Tracks which lesson the player is currently attending.
class_number = 1
MAX_CLASSES = 2

current_class_choice = None

class_reward_given = False




# Scene 24 state
scene24_paper_start = 0
scene24_fade_start = 0
scene24_fade_background = None

SCENE24_POP_DURATION = 1000
SCENE24_SLIDE_DURATION = 500
SCENE24_FADE_DURATION = 1500
SCENE24_BLACK_DURATION = 2000

# Keep the test result for future endings.
# State: thursday_test_paper_owned — True only if the player has earned the 60-point paper as trial evidence.
thursday_test_paper_owned = False

# Marks the dedicated bedroom dialogue after the quiz.
quiz_night_active = False


# Function: begin_class — Initialize the next class and its classroom state.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def begin_class():

    """
    Clear the prior classroom choice and settlement guard only.
    Do not reset the player's accumulated stats.
    """
    global current_class_choice, class_reward_given



    # Start a new class by clearing the previous choice and settlement flag.

    # Do not reset the player stats when starting a new class.

    current_class_choice = None

    class_reward_given = False





# Function: choose_class_activity — Apply the selected classroom action and its stat effects.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def choose_class_activity(choice):

    """
    Validate and store an activity without modifying stats yet.
    """
    global current_class_choice



    valid_choices = ("eat", "chat", "sleep", "study")



    if choice not in valid_choices:

        return



    # Store the selected activity for settlement after the class scene ends.

    # Do not apply any stat changes at the moment the player selects an activity.

    current_class_choice = choice







# Function: finish_class_activity — Finalize this event and transition to the next story phase.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def finish_class_activity():

    """
    Commit the per-class -10 penalties plus the choice-dependent refund.
    Apply effects exactly once, then check for a bad ending.
    """
    global class_reward_given



    # Guard against applying the same class penalties or rewards more than once.

    if class_reward_given or current_class_choice is None:

        return



    # Apply a baseline penalty of 10 points to hunger, energy, and mood for each class.

    hunger_change = -10

    energy_change = -10

    mood_change = -10



    # Offset one penalty by 10 points according to the selected classroom activity.

    if current_class_choice == "eat":

        hunger_change += 20



    elif current_class_choice == "chat":

        mood_change += 20



    elif current_class_choice == "sleep":

        energy_change += 20



    elif current_class_choice == "study":

        pass



    # Commit all three stat adjustments together after the teacher dismisses class.

    change_stats(

        hunger_change=hunger_change,

        energy_change=energy_change,

        mood_change=mood_change

    )



    # Check the resulting stats for a zero value after applying the class settlement.

    check_bad_ending()



    class_reward_given = True







# Function: start_class_settlement — Begin the timed end-of-class stat animation.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_class_settlement():

    """
    Capture pre- and post-settlement values and start a UI animation.
    The actual game stats are updated now; only the displayed bars interpolate.
    """
    global settlement_active, settlement_start

    global settlement_from, settlement_to

    global display_hunger, display_energy, display_mood



    if settlement_active or class_reward_given:

        return



    # Capture the initial stat values so the UI can animate from the correct starting point.

    settlement_from = (hunger, energy, mood)



    # The class has ended: apply the accumulated effects of the selected activity once.

    finish_class_activity()



    # Capture the final values that the visible bars should animate toward.

    settlement_to = (hunger, energy, mood)



    display_hunger, display_energy, display_mood = settlement_from



    settlement_start = pygame.time.get_ticks()

    settlement_active = True



# Function: start_bad_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_bad_transition():

    """
    Capture the outgoing scene and begin fading toward a bad ending.
    """
    global current_scene

    global bad_transition_start

    global bad_transition_target

    global bad_transition_background



    # Remember the specific ending selected by the stat checker.

    bad_transition_target = pending_bad_ending



    if bad_transition_target is None:

        return



    # Capture the currently rendered frame so the fade begins from the previous scene.

    bad_transition_background = screen.copy()



    bad_transition_start = pygame.time.get_ticks()

    current_scene = "bad_transition"



    stop_voice()







# Function: draw_bad_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_bad_transition():

    """
    Render fade-out, full black, and fade-in phases for an ending.
    Once complete, load that ending's dialogue and reset the typewriter.
    """
    global current_scene, dialogues, dialogue_index



    elapsed = pygame.time.get_ticks() - bad_transition_start



    ending_images = {
        "bad_hunger": bad_hunger,
        "bad_energy": bad_energy,
        "bad_mood": bad_mood,
        "bad_homework": bad_homework,
    }

    target_image = ending_images[bad_transition_target]



    # Stage 1: Fade to black

    if elapsed < BAD_FADE_OUT:

        screen.blit(bad_transition_background, (0, 0))



        alpha = int(255 * elapsed / BAD_FADE_OUT)

        black_overlay.set_alpha(alpha)

        screen.blit(black_overlay, (0, 0))



    # Stage 2: Hold black

    elif elapsed < BAD_FADE_OUT + BAD_BLACK_HOLD:

        screen.fill((0, 0, 0))



    # Stage 3: Fade in bad ending

    elif elapsed < BAD_FADE_OUT + BAD_BLACK_HOLD + BAD_FADE_IN:

        screen.blit(target_image, (0, 0))



        fade_elapsed = elapsed - BAD_FADE_OUT - BAD_BLACK_HOLD

        alpha = int(255 * (1 - fade_elapsed / BAD_FADE_IN))



        black_overlay.set_alpha(alpha)

        screen.blit(black_overlay, (0, 0))



    # Stage 4: Enter bad ending

    else:

        current_scene = bad_transition_target

        dialogues = BAD_ENDING_DIALOGUES[current_scene]

        dialogue_index = 0



        reset_typewriter()

        screen.blit(target_image, (0, 0))

        draw_dialogue()











# Function: start_credits_transition — Capture the ending frame and start the fade into credits.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_credits_transition():

    """
    Capture the final ending frame, start the credits fade, and fade out music.
    """
    global current_scene

    global credits_transition_start

    global credits_transition_background



    # Save the current bad ending screen

    credits_transition_background = screen.copy()



    # Start the credits transition

    credits_transition_start = pygame.time.get_ticks()

    current_scene = "credits_transition"



    # Stop character voices

    stop_voice()



    # Fade out current background music

    pygame.mixer.music.fadeout(1000)









# Function: draw_credits_transition — Render the timed fade and credits screen.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_credits_transition():

    """
    Draw the credits fade phases and begin the replacement music once.
    Music loading occurs after the initial fade interval.
    """
    global current_scene

    global credits_music_started

    elapsed = pygame.time.get_ticks() - credits_transition_start

    elapsed = pygame.time.get_ticks() - credits_transition_start



    # Start credits music once, after 1 second

    if elapsed >= 1000 and not credits_music_started:

        pygame.mixer.music.load(

            str(ASSETS / "credits_music.ogg")

        )

        pygame.mixer.music.set_volume(0.35)

        pygame.mixer.music.play(

            loops=0,

            fade_ms=2000

        )

        credits_music_started = True



    # Keep your original fade transition code below





    # Stage 1: Fade to black

    if elapsed < CREDITS_FADE_OUT:

        screen.blit(credits_transition_background, (0, 0))



        alpha = int(255 * elapsed / CREDITS_FADE_OUT)

        black_overlay.set_alpha(alpha)

        screen.blit(black_overlay, (0, 0))



    # Stage 2: Hold black screen

    elif elapsed < CREDITS_FADE_OUT + CREDITS_BLACK_HOLD:

        screen.fill((0, 0, 0))



    # Stage 3: Fade in credits

    elif elapsed < CREDITS_FADE_OUT + CREDITS_BLACK_HOLD + CREDITS_FADE_IN:

        screen.blit(credits_image, (0, 0))



        fade_elapsed = (

            elapsed - CREDITS_FADE_OUT - CREDITS_BLACK_HOLD

        )



        alpha = int(255 * (1 - fade_elapsed / CREDITS_FADE_IN))

        black_overlay.set_alpha(alpha)

        screen.blit(black_overlay, (0, 0))



    # Stage 4: Finish credits transition

    else:

        current_scene = "credits"

        screen.blit(credits_image, (0, 0))

        print("Credits displayed successfully!")




# Function: draw_tuesday_game_choice — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_game_choice():
    """Draw the single video-game choice for Class 7."""
    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )
    overlay.fill((0, 0, 0, 125))
    screen.blit(overlay, (0, 0))

    screen.blit(tuesday_game_ui, tuesday_game_rect)


# Function: draw_console_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_console_choices():
    """Draw the two console ownership choices."""
    overlay = pygame.Surface(
        (WIDTH, HEIGHT), pygame.SRCALPHA
    )
    overlay.fill((0, 0, 0, 125))
    screen.blit(overlay, (0, 0))

    screen.blit(console_a_ui, console_a_rect)
    screen.blit(console_b_ui, console_b_rect)



# =====================================
# CLASS 7 - AFTER INCIDENT TRANSITIONS
# =====================================

POST_CONSOLE_FADE_OUT = 1000
POST_CONSOLE_BLACK_HOLD = 2000
POST_CONSOLE_FADE_IN = 1500

post_console_transition_start = 0
post_console_transition_background = None
post_console_transition_target = None

# Tracks whether Class 7 is displaying dismissal dialogue.
class7_post_console_phase = None

# =====================================
# TUESDAY EVENING - STORY STATE
# =====================================

# True when Tuesday's cleaning event is finished
# and the player enters the Tuesday dinner storyline.
tuesday_evening_active = False


# =====================================
# TUESDAY NIGHT - SCENE 19 TRANSITION
# =====================================

SCENE19_BLACK_DURATION = 1500

scene19_transition_start = 0


# Function: start_scene19_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene19_transition():
    """Start a brief black screen before the phone chat."""
    global current_scene, scene19_transition_start

    scene19_transition_start = pygame.time.get_ticks()
    current_scene = "scene19_transition"

    stop_voice()


# Function: draw_scene19_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene19_transition():
    """Display black, then initialize Scene 19."""
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - scene19_transition_start

    if elapsed < SCENE19_BLACK_DURATION:
        screen.fill((0, 0, 0))
        return

    # Enter the phone chat scene after 1.5 seconds.
    current_scene = "scene19"
    dialogues = scene19_dialogues
    dialogue_index = 0

    reset_typewriter()

    screen.blit(scene19, (0, 0))
    draw_dialogue()

    print("TUESDAY NIGHT: Entering Scene 19")



# Function: start_post_console_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_post_console_transition(target_scene):
    """Start a fade transition after the console incident."""
    global current_scene
    global post_console_transition_start
    global post_console_transition_background
    global post_console_transition_target

    if target_scene not in ("scene9", "scene18"):
        return

    post_console_transition_target = target_scene
    post_console_transition_background = screen.copy()
    post_console_transition_start = pygame.time.get_ticks()

    current_scene = "post_console_transition"
    stop_voice()


# Function: draw_post_console_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_post_console_transition():
    """Fade to the classroom or the cleaning scene."""
    global current_scene, dialogues, dialogue_index
    global class7_post_console_phase
    global class_choice_open, tuesday_game_choice_open

    elapsed = (
        pygame.time.get_ticks()
        - post_console_transition_start
    )

    if post_console_transition_target == "scene9":
        target_image = scene9
        target_dialogues = scene9_tuesday_dismissal_dialogues
    else:
        target_image = scene18
        target_dialogues = scene18_dialogues

    # Stage 1: Fade the previous scene to black.
    if elapsed < POST_CONSOLE_FADE_OUT:
        screen.blit(post_console_transition_background, (0, 0))

        alpha = int(255 * elapsed / POST_CONSOLE_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 2: Hold on a black screen.
    elif elapsed < (
        POST_CONSOLE_FADE_OUT + POST_CONSOLE_BLACK_HOLD
    ):
        screen.fill((0, 0, 0))

    # Stage 3: Fade in the next background.
    elif elapsed < (
        POST_CONSOLE_FADE_OUT
        + POST_CONSOLE_BLACK_HOLD
        + POST_CONSOLE_FADE_IN
    ):
        screen.blit(target_image, (0, 0))

        fade_elapsed = (
            elapsed
            - POST_CONSOLE_FADE_OUT
            - POST_CONSOLE_BLACK_HOLD
        )

        alpha = int(
            255 * (1 - fade_elapsed / POST_CONSOLE_FADE_IN)
        )

        black_overlay.set_alpha(max(0, alpha))
        screen.blit(black_overlay, (0, 0))

    # Stage 4: Enter the next story scene.
    else:
        current_scene = post_console_transition_target
        dialogues = target_dialogues
        dialogue_index = 0

        class_choice_open = False
        tuesday_game_choice_open = False

        if current_scene == "scene9":
            class7_post_console_phase = "dismissal"
        else:
            class7_post_console_phase = "cleaning"

        reset_typewriter()

        screen.blit(target_image, (0, 0))
        draw_dialogue()

        print("POST CONSOLE TRANSITION:", current_scene)


# Function: start_console_incident — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_console_incident():
    """Start the Class 7 console incident in Scene 14."""
    global current_scene, dialogues, dialogue_index
    global console_event_stage, console_choice
    global class_choice_open, tuesday_game_choice_open
    global scene17_enter_time

    # Enter Scene 17 and begin the dramatic pause.
    current_scene = "scene17"
    dialogues = console_accusation_dialogues
    dialogue_index = 0

    # Record the time when the scene begins.
    scene17_enter_time = pygame.time.get_ticks()

    # Hide dialogue and portraits during the pause.
    console_event_stage = "waiting"


  
    console_choice = None

    class_choice_open = False
    tuesday_game_choice_open = False

    stop_voice()
    reset_typewriter()

    print("CONSOLE EVENT: Teacher confrontation")


# Function: select_console_option — Handle the player choice and update story or gameplay flags.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_console_option(choice):
    """Resolve who takes responsibility for the console."""
    global dialogues, dialogue_index
    global console_event_stage, console_choice

    if current_scene != "scene17":
        return

    if console_event_stage != "choice":
        return

    if choice not in ("a", "b"):
        return

    console_choice = choice
    console_event_stage = "result"

    if choice == "a":
        dialogues = console_a_dialogues
    else:
        dialogues = console_b_dialogues

    dialogue_index = 0
    stop_voice()
    reset_typewriter()

    print("CONSOLE OPTION:", choice.upper())


# Function: finish_console_incident — Finalize this event and transition to the next story phase.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def finish_console_incident():
    """Apply the outcome after the branch dialogue ends."""
    global console_event_stage
    global pending_bad_ending
    global display_mood

    if console_event_stage != "result":
        return

    # Mark the event complete to prevent repeated stat changes.
    console_event_stage = "finished"
    stop_voice()

    if console_choice == "a":
        # Taking the blame triggers Bad Ending 4.
        pending_bad_ending = "bad_homework"
        start_bad_transition()
        print("CONSOLE EVENT: Bad Ending 4 triggered")
        return


    if console_choice == "b":
        # Ouyang's betrayal dialogue has finished.
        # Apply the Mood penalty only once.
        change_stats(mood_change=-10)
        display_mood = mood

        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

        print("CONSOLE EVENT: Mood -10")

        # Return to Scene 9 for the final class dismissal.
        start_post_console_transition("scene9")
        return



# Function: select_tuesday_game — Handle the player choice and update story or gameplay flags.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_tuesday_game():
    """
    Start the console incident when the player
    chooses to play video games with Ouyang.
    """
    if current_scene != "scene9":
        return

    if not tuesday_game_choice_open:
        return

    # Begin the teacher confrontation in Scene 17.
    start_console_incident()





# Function: update_class_settlement — Advance the stat animation and proceed when settlement finishes.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def update_class_settlement():

    """
    Animate displayed stats with ease-out interpolation and a hold.
    After the hold, enter a pending bad ending or continue to Scene 8.
    """
    global settlement_active, current_scene

    global dialogues, dialogue_index

    global display_hunger, display_energy, display_mood



    if not settlement_active:

        return



    elapsed = pygame.time.get_ticks() - settlement_start



    progress = min(1.0, elapsed / SETTLEMENT_DURATION)



    # Cubic ease-out interpolation: bars change quickly at first and slow near their targets.

    eased = 1 - (1 - progress) ** 3



    display_hunger = round(

        settlement_from[0] +

        (settlement_to[0] - settlement_from[0]) * eased

    )



    display_energy = round(

        settlement_from[1] +

        (settlement_to[1] - settlement_from[1]) * eased

    )



    display_mood = round(

        settlement_from[2] +

        (settlement_to[2] - settlement_from[2]) * eased

    )



    # Wait through the full animation and hold period before entering the next scene.

    if elapsed >= SETTLEMENT_DURATION + SETTLEMENT_HOLD:



        settlement_active = False



        display_hunger = hunger

        display_energy = energy

        display_mood = mood





   # Check the result after the settlement animation

        if pending_bad_ending is not None:

            # Start the bad ending fade transition

            dialogues = []

            dialogue_index = 0

            start_bad_transition()





        else:
            # Choose the destination after class settlement.

            if class_number == 4:
                # Class 4: Select the route after settlement.
                if afternoon_chat_triggered:
                    # Chat with Jiang -> Scene 12.
                    start_route_transition("scene12")
                else:
                    # Other activities -> Scene 11.
                    start_route_transition("scene11")

                return

            elif class_number == 9:
                # Thursday Class 9:
                # Show Ouyang's teasing dialogue after settlement.
                current_scene = "scene10"
                dialogues = class9_ouyang_dialogues

                dialogue_index = 0
                reset_typewriter()

                print("CLASS 9: Ouyang after-class event")
                return

            elif class_number == 10:
                # After Class 10, go to the track running event.
                start_scene21_transition()
                return


            elif class_number == 11:
                # Thursday first class finished.
                # Go to Scene 22 instead of the next lesson.
                print("CLASS 11 FINISHED -> SCENE 22")
                start_scene22_transition()
                return

            elif class_number == 12:
                # Thursday morning second class ends.
                enter_thursday_class13()
                return

            elif class_number == 13:
                # Thursday afternoon class ends.
                # Sun approaches before the weekly quiz.
                start_sun_quiz_event()
                return


            elif class_number == 3:
                # The first afternoon class ends at Scene 10.
                current_scene = "scene10"
                dialogues = scene10_dialogues

            else:
                # Morning classes continue to Scene 8.
                current_scene = "scene8"
                dialogues = scene8_dialogues

            dialogue_index = 0
            reset_typewriter()


# Function: advance_sun_quiz_event — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def advance_sun_quiz_event():
    global dialogues, dialogue_index, sun_quiz_phase

    if sun_quiz_phase == "intro":
        if thursday_vape_choice == "accept":
            dialogues = sun_quiz_accept_dialogues
        else:
            dialogues = sun_quiz_decline_dialogues

        sun_quiz_phase = "response"
        dialogue_index = 0
        stop_voice()
        reset_typewriter()
        return

    if sun_quiz_phase == "response":
        sun_quiz_phase = "finished"
        enter_scene23()


# Function: select_scene23_choice — Save the Thursday quiz choice, which determines whether the 60-point evidence can be earned.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_scene23_choice(choice):
    global current_scene, dialogues, dialogue_index
    global scene23_choice_open
    global thursday_quiz_choice, thursday_quiz_honest
    global scene23_accusation_start
    global thursday_test_paper_owned

    if current_scene != "scene23" or not scene23_choice_open:
        return

    if choice not in ("a", "b", "c"):
        return

    # C is unlocked only if Little F accepted the vape.
    if choice == "c" and thursday_vape_choice != "accept":
        return

    scene23_choice_open = False

    thursday_quiz_choice = choice
    thursday_quiz_honest = (choice == "b")

    # Only copying Sun's answers awards the 60-point paper.
    thursday_test_paper_owned = (choice == "c")

    print(
        "QUIZ RESULT:",
        choice,
        "PAPER OWNED:",
        thursday_test_paper_owned
    )

    dialogue_index = 0
    stop_voice()

    if choice == "a":
        # Wait two seconds before the teacher accuses Little F.
        current_scene = "scene23_accusation_wait"
        scene23_accusation_start = pygame.time.get_ticks()

    elif choice == "b":
        current_scene = "scene23_b"
        dialogues = scene23_b_dialogues
        reset_typewriter()

    elif choice == "c":
        current_scene = "scene23_c"
        dialogues = scene23_c_dialogues
        reset_typewriter()

    print("THURSDAY QUIZ CHOICE:", choice)


# Function: draw_scene23_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene23_choices():
    screen.blit(quiz_b_ui, quiz_b_rect)
    screen.blit(quiz_a_ui, quiz_a_rect)

    if thursday_vape_choice == "accept":
        screen.blit(quiz_c_ui, quiz_c_rect)


# Function: draw_scene23_accusation_wait — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene23_accusation_wait():
    global current_scene, dialogues, dialogue_index

    screen.blit(scene23, (0, 0))

    elapsed = pygame.time.get_ticks() - scene23_accusation_start

    if elapsed < SCENE23_ACCUSATION_DELAY:
        return

    current_scene = "scene23_a"
    dialogues = scene23_a_dialogues
    dialogue_index = 0

    stop_voice()
    reset_typewriter()

# =====================================
# THURSDAY TRACK EVENT (SCENE 21)
# =====================================

scene21_choice_open = False
scene21_choice_rects = {}

# Stores the current choice in Scene 21:
# "ignore" or "talk"
scene21_choice_result = None

# This one is important:
# keep it for the next mom dialogue and Friday night ending.
# State: thursday_track_choice — Wednesday track choice, used to select the Friday story route.
thursday_track_choice = None




# =====================================
# FRIDAY NIGHT FINAL EVENT
# =====================================

friday_night_route = None
friday_final_finished = False

friday_night_transition_start = 0
friday_night_transition_background = None
friday_night_transition_target = None

FRIDAY_NIGHT_FADE = 1500
FRIDAY_NIGHT_BLACK = 1000

friday_study_silence_start = 0
FRIDAY_STUDY_SILENCE = 3000

friday_study_penalty_applied = False

# =====================================
# NEW THURSDAY BREAKFAST STATE
# =====================================

new_thursday_breakfast_active = False
new_thursday_breakfast_finished = False

# Prevent dinner settlement from applying multiple times.
thursday_dinner_route_active = False
thursday_dinner_settled = False

# Fade transition from Class 10 -> Scene 21
scene21_transition_active = False
scene21_transition_start = 0
scene21_transition_background = None

SCENE21_FADE_OUT = 1500
SCENE21_BLACK_HOLD = 1000
SCENE21_FADE_IN = 1500


# ==============================

# Scene 7 branching configuration: associate each activity with its scene and dialogue.

# ==============================



class_choice_open = False




# =====================================
# HOMEWORK EVENT STATE
# =====================================

homework_choice_open = False

HOMEWORK_EVENT_SCENES = (
    "homework_intro",
    "homework_a",
    "homework_b",
    "homework_c",
    "homework_survived",
)


# Function: start_homework_event — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_homework_event():
    global current_scene, dialogues, dialogue_index
    global homework_choice_open

    current_scene = "homework_intro"
    dialogues = homework_intro_dialogues
    dialogue_index = 0
    homework_choice_open = False

    reset_typewriter()


# Function: select_homework_option — Handle the player choice and update story or gameplay flags.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_homework_option(choice):
    global current_scene, dialogues, dialogue_index
    global homework_choice_open

    if not homework_choice_open:
        return

    options = {
        "a": ("homework_a", homework_a_dialogues),
        "b": ("homework_b", homework_b_dialogues),
        "c": ("homework_c", homework_c_dialogues),
    }

    if choice not in options:
        return

    current_scene, dialogues = options[choice]
    dialogue_index = 0
    homework_choice_open = False

    reset_typewriter()

# Function: draw_scene21_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene21_choices():
    """Draw the two choice buttons in Scene 21."""
    global scene21_choice_rects

    top_margin = HEIGHT - 300
    gap = 30

    # Top button: B = TALK TO HER
    talk_rect = choice_talk_to_her_ui.get_rect(
        center=(WIDTH // 2, top_margin)
    )

    # Bottom button: A = IGNORE HER
    ignore_rect = choice_ignore_her_ui.get_rect(
        center=(WIDTH // 2, top_margin + choice_talk_to_her_ui.get_height() + gap)
    )

    screen.blit(choice_talk_to_her_ui, talk_rect)
    screen.blit(choice_ignore_her_ui, ignore_rect)

    scene21_choice_rects = {
        "talk": talk_rect,
        "ignore": ignore_rect,
    }


CLASS_SCENES = {

    "eat": ("scene7_eat", scene7_eat_dialogues),

    "chat": ("scene7_chat", scene7_chat_dialogues),

    "sleep": ("scene7_sleep", scene7_sleep_dialogues),

    "study": ("scene7_study", scene7_study_dialogues),

}



CLASS_BACKGROUNDS = {

    "scene7_eat": scene7_eat,

    "scene7_chat": scene7_chat,

    "scene7_sleep": scene7_sleep,

    "scene7_study": scene7_study,

}







# Delay the classroom branch change to give players time to register their selection.

CHOICE_DELAY = 1000  # 1000毫秒 = 1秒

choice_transition_active = False

choice_transition_start = 0

choice_pending_scene = None

choice_pending_dialogues = None

# =====================================
# SCENE 22 - THURSDAY VAPE EVENT
# =====================================

scene22_choice_open = False
scene22_choice_made = None          # "accept" / "decline"
thursday_vape_choice = None         # Save for later afternoon event

scene22_transition_start = 0
scene22_vape_anim_start = 0

SCENE22_FADE_OUT = 500
SCENE22_BLACK_HOLD = 600
SCENE22_FADE_IN = 500

SCENE22_VAPE_POP_DURATION = 1000
SCENE22_VAPE_SLIDE_DURATION = 500

scene22_energy_reward_given = False


# Thursday quiz state
# State: thursday_quiz_choice — Thursday quiz answer (A/B/C); must agree with the evidence ownership flag.
thursday_quiz_choice = None
thursday_quiz_honest = False

sun_quiz_phase = None
scene23_choice_open = False
scene23_accusation_start = 0

SCENE23_ACCUSATION_DELAY = 2000




# Function: select_class_option — Handle the player choice and update story or gameplay flags.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_class_option(choice):

    """
    Validate the menu selection and schedule its scene change.
    Close the menu immediately, but defer the new activity scene.
    """
    global class_choice_open

    global afternoon_chat_triggered

    global choice_transition_active

    global choice_transition_start

    global choice_pending_scene

    global choice_pending_dialogues



    if not class_choice_open or choice_transition_active:

        return



    if choice not in CLASS_SCENES:

        return



    # Record the activity now; numerical effects are deferred until class dismissal.

    choose_class_activity(choice)

    
    # Use the existing classroom activity backgrounds.
    choice_pending_scene, choice_pending_dialogues = CLASS_SCENES[choice]

    # Only Class 4 has the special chat event.
    if class_number == 4 and choice == "chat":
        afternoon_chat_triggered = True
        choice_pending_dialogues = scene9_special_chat_dialogues




    # Hide the menu to avoid another choice while the transition is pending.

    class_choice_open = False



    # Start the non-blocking transition timer; the main loop continues rendering.

    choice_transition_start = pygame.time.get_ticks()

    choice_transition_active = True



    stop_voice()



# Function: select_scene21_choice — Remember whether Little F talked to Jiang; this changes the Friday route.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_scene21_choice(choice):
    """Resolve the Scene 21 choice."""
    global current_scene, dialogues, dialogue_index
    global scene21_choice_open, scene21_choice_result
    global thursday_track_choice

    if not scene21_choice_open:
        return

    scene21_choice_open = False
    scene21_choice_result = choice
    thursday_track_choice = choice

    stop_voice()

    if choice == "talk":
        current_scene = "scene21_talk"
        dialogues = scene21_talk_dialogues
        dialogue_index = 0
        reset_typewriter()

        print("SCENE21 CHOICE: TALK route selected")

    elif choice == "ignore":
        current_scene = "scene21_ignore"
        dialogues = scene21_ignore_dialogues
        dialogue_index = 0
        reset_typewriter()

        print("SCENE21 CHOICE: IGNORE route selected")

# Function: enter_thursday_dinner_scene — Enter the next story phase and set its scene and dialogue.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def enter_thursday_dinner_scene():
    """Return to Scene 13 and load the proper mom dialogue."""
    global current_scene, dialogues, dialogue_index
    global thursday_dinner_route_active, thursday_dinner_settled

    current_scene = "scene13"
    dialogue_index = 0

    thursday_dinner_route_active = True
    thursday_dinner_settled = False

    if thursday_track_choice == "talk":
        dialogues = scene13_thursday_talk_dialogues

        # Mom lets Little F eat dinner.
        change_stats(hunger_change=40)
        print("DINNER ROUTE: TALK -> Hunger +40")

    else:
        dialogues = scene13_thursday_ignore_dialogues
        print("DINNER ROUTE: IGNORE -> No dinner")

    stop_voice()
    reset_typewriter()



# Function: update_choice_transition — Update event progress using the current state and elapsed time.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def update_choice_transition():

    """
    Switch to the chosen activity after the non-blocking delay.
    """
    global choice_transition_active

    global current_scene, dialogues, dialogue_index



    if not choice_transition_active:

        return



    elapsed = pygame.time.get_ticks() - choice_transition_start



    if elapsed >= CHOICE_DELAY:

        current_scene = choice_pending_scene

        dialogues = choice_pending_dialogues

        dialogue_index = 0



        choice_transition_active = False

        reset_typewriter()







# ==============================

# Render the four clickable classroom options over a dimmed background.

# ==============================





# Function: draw_class_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class_choices():



    """
    Dim the current classroom background and render four choices.
    """
    overlay = pygame.Surface(

        (WIDTH, HEIGHT), pygame.SRCALPHA

    )

    overlay.fill((0, 0, 0, 120))

    screen.blit(overlay, (0, 0))





# Function: draw_class_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class_choices():
    """Display the four regular classroom activity buttons."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))

    screen.blit(choice_chat_ui, choice_chat_rect)
    screen.blit(choice_eat_ui, choice_eat_rect)
    screen.blit(choice_sleep_ui, choice_sleep_rect)
    screen.blit(choice_study_ui, choice_study_rect)

    hint = hint_font.render(
        "1.Chat  2.Snack  3.Nap  4.Study",
        True,
        (255, 245, 210)
    )
    screen.blit(
        hint,
        (WIDTH // 2 - hint.get_width() // 2, 650)
    )


# Function: draw_homework_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_homework_choices():
    """Display only the three homework inspection buttons."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 125))
    screen.blit(overlay, (0, 0))

    screen.blit(homework_a_ui, homework_a_rect)
    screen.blit(homework_b_ui, homework_b_rect)
    screen.blit(homework_c_ui, homework_c_rect)



# =====================================
# TUESDAY BREAKFAST - EVENT STATE
# =====================================

tuesday_choice_open = False
tuesday_breakfast_finished = False


# Function: start_tuesday_breakfast — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_tuesday_breakfast():
    """Enter Tuesday breakfast using Scene 6's background."""
    global current_scene, dialogues, dialogue_index
    global tuesday_choice_open, tuesday_breakfast_finished

    current_scene = "scene16"
    dialogues = scene16_mom_dialogues
    dialogue_index = 0

    tuesday_choice_open = False
    tuesday_breakfast_finished = False

    reset_typewriter()


# Function: select_tuesday_option — Handle the player choice and update story or gameplay flags.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_tuesday_option(choice):
    """Resolve the player's response and begin Dad's dialogue."""
    global dialogues, dialogue_index
    global tuesday_choice_open, tuesday_breakfast_finished
    global display_mood

    if not tuesday_choice_open:
        return

    if choice not in ("a", "b", "c"):
        return

    # Close the choice menu immediately.
    tuesday_choice_open = False
    tuesday_breakfast_finished = True

    # Choices A and C reduce Mood by 10 points.
    # Choice B has no penalty.
    if choice != "b":
        change_stats(mood_change=-10)
        display_mood = mood

        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

    # All choices lead to exactly the same reply from Dad.
    dialogues = scene16_dad_dialogues
    dialogue_index = 0

    reset_typewriter()

    print("TUESDAY BREAKFAST CHOICE:", choice.upper())


# Function: draw_tuesday_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_choices():
    """Draw the three clickable breakfast dialogue choices."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 125))
    screen.blit(overlay, (0, 0))

    screen.blit(tuesday_a_ui, tuesday_a_rect)
    screen.blit(tuesday_b_ui, tuesday_b_rect)
    screen.blit(tuesday_c_ui, tuesday_c_rect)


    # Display the matching number-key shortcuts below the selection buttons.

    hint = hint_font.render(

        "1.Chat  2.Snack  3.Nap  4.Study",

        True,

        (255, 245, 210)

    )



    screen.blit(

        hint,

        (WIDTH // 2 - hint.get_width() // 2, 650)

    )









# ==============================

# Pixel-style status UI: place the three meters across the top of the screen.

# ==============================





# ==============================

# Status bar fill alignment: each image has its own inner fill rectangle.

# ==============================



# Function: draw_one_status_ui — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_one_status_ui(image, value, x, y, color, fill_rect):



    # Unpack the fill region specific to this meter; these coordinates are image-relative.

    """
    Draw one filled meter and overlay the corresponding pixel-art frame.
    fill_rect specifies the inner region relative to the image position.
    """
    left, top, width, height = fill_rect



    fill_width = round(width * max(0, min(100, value)) / 100)



    # Draw only the fraction of the bar corresponding to the current display value.

    if fill_width > 0:

        pygame.draw.rect(

            screen,

            color,

            (

                x + left,

                y + top,

                fill_width,

                height

            )

        )



    # Blit the transparent pixel-art frame over the colored fill.

    screen.blit(image, (x, y))





# Function: draw_status_ui — Draw hunger, energy and mood meters unless hidden for this scene.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_status_ui():



    # Energy meter: blue fill beneath the ZZZ icon.

    """
    Position energy, hunger, and mood meters along the top edge.
    """
    draw_one_status_ui(

        energy_ui,

        display_energy,

        10, 5,

        (93, 182, 245),

        (127, 52, 237, 26)

    )



    # Hunger meter: orange fill beneath the food icon.

    draw_one_status_ui(

        hunger_ui,

        display_hunger,

        435, 5,

        (250, 170, 44),

        (113, 52, 252, 26)

    )



    # Mood meter: red fill beneath the heart icon.

    draw_one_status_ui(

        mood_ui,

        display_mood,

        860, 5,

        (240, 70, 90),

        (83, 52, 284, 26)

    )





# Track the last spoken character to avoid replaying the same letter sound.

last_visible_count = 0





# ==============================

# Global fade surfaces and transition durations, specified in milliseconds.

# ==============================



black_overlay = pygame.Surface((WIDTH, HEIGHT))

black_overlay.fill((0, 0, 0))



FADE_OUT_TIME = 1000

BLACK_TIME = 1000

FADE_IN_TIME = 1500



# Dedicated fade durations for the breakfast-to-classroom transition, in milliseconds.

SCENE_FADE_OUT = 1200

SCENE_FADE_IN = 1500

# ==============================
# CLASS LOOP TRANSITION
# ==============================

CLASS_FADE_OUT = 1000
CLASS_BLACK_HOLD = 2000
CLASS_FADE_IN = 1500

class_transition_start = 0
class_transition_background = None


# ==============================
# AFTERNOON TRANSITION SETTINGS
# ==============================

AFTERNOON_FADE_OUT = 1000
AFTERNOON_BLACK_HOLD = 2000
AFTERNOON_FADE_IN = 1500

afternoon_transition_start = 0
afternoon_transition_background = None
afternoon_next_class = False


# =====================================
# AFTER-CLASS ROUTE TRANSITION
# =====================================

ROUTE_FADE_OUT = 1000
ROUTE_BLACK_HOLD = 2000
ROUTE_FADE_IN = 1500

route_transition_start = 0
route_transition_target = None
route_transition_background = None
route_reward_applied = False


scene_transition_start = 0



# State: current_scene — Active story state used by rendering, input, sound and dialogue routing.
current_scene = "menu"

transition_start = 0



# ==============================

# Intertitle cutscene: fade in a centered title, hold it, and fade out.

# ==============================



INTERTITLE_FADE_IN = 1200

INTERTITLE_HOLD = 1000

INTERTITLE_FADE_OUT = 1200



intertitle_text = ""

intertitle_start = 0

intertitle_next_scene = None

intertitle_next_dialogues = None

# ==============================

# QTE configuration: number of required key presses and flicker interval.

# ==============================



QTE_REQUIRED_PRESSES = 20

QTE_FLASH_INTERVAL = 180



qte_press_count = 0

qte_start_time = 0

qte_next_scene = None

qte_next_dialogues = None





# Function: parse_dialogue_entry — Normalize legacy and new dialogue entries into speaker, expression and text.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def parse_dialogue_entry(entry):

    """

    Accept two dialogue tuple formats:

    Legacy: (name, text)

    Expressive: (name, expression, text)

    """

    if len(entry) == 2:

        name, text = entry

        expression = "normal"

    else:

        name, expression, text = entry



    return name, expression, text



# ==============================

# Text layout helpers for wrapping dialogue without disrupting typewriter indices.

# ==============================



# Function: wrap_text — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def wrap_text(text, max_width):

    """

    Wrap text to the dialogue width while tracking original character indices.

    The original indices keep typewriter rendering and audio in sync.

    """

    lines = []

    line = ""

    indices = []



    for i, char in enumerate(text):



        if char == "\n":

            lines.append((line, indices))

            line = ""

            indices = []

            continue



        if font.size(line + char)[0] > max_width and line:

            lines.append((line, indices))

            line = ""

            indices = []



        line += char

        indices.append(i)



    lines.append((line, indices))

    return lines





# Function: visible_character_count — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def visible_character_count():

    """
    Calculate how many text characters should currently be visible.
    """
    elapsed = pygame.time.get_ticks() - text_start

    return max(0, elapsed // CHAR_INTERVAL)


TUESDAY_FADE_OUT = 1000
TUESDAY_TITLE_FADE = 800
TUESDAY_TITLE_HOLD = 2000

tuesday_transition_start = 0
tuesday_transition_background = None



# =====================================
# THURSDAY - DAY TITLE TRANSITION
# =====================================

THURSDAY_FADE_IN = 1500
THURSDAY_TITLE_HOLD = 1500
THURSDAY_FADE_OUT = 1500

thursday_title_start = 0



# =====================================
# THURSDAY - BLACK SCREEN BEFORE CLASS
# =====================================

THURSDAY_MOM_HOLD_DURATION = 1000
thursday_mom_hold_start = 0


# Function: start_thursday_mom_hold — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_thursday_mom_hold():
    """Begin a one-second black screen after Mom's dialogue."""
    global current_scene, thursday_mom_hold_start

    current_scene = "thursday_mom_hold"
    thursday_mom_hold_start = pygame.time.get_ticks()

    stop_voice()


# Function: draw_thursday_mom_hold — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_thursday_mom_hold():
    """Wait on a black screen before Thursday's first class."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    screen.fill((0, 0, 0))

    elapsed = pygame.time.get_ticks() - thursday_mom_hold_start

    if elapsed < THURSDAY_MOM_HOLD_DURATION:
        return

    # Start Thursday's first class after the pause.
    class_number = 8
    current_scene = "scene7"

    dialogues = thursday_class_dialogues
    dialogue_index = 0

    begin_class()
    class_choice_open = False

    reset_typewriter()

    print("THURSDAY: Entering Class 8")


# Function: start_thursday_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_thursday_transition():
    """Begin Thursday with a black screen and title."""
    global current_scene, thursday_title_start

    thursday_title_start = pygame.time.get_ticks()
    current_scene = "thursday_transition"

    stop_voice()
    print("THURSDAY: Title transition started")


# Function: draw_thursday_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_thursday_transition():
    """Fade the Thursday title in and out on black."""
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - thursday_title_start

    screen.fill((0, 0, 0))

    title_surface = title_font.render(
        "WEDNESDAY", True, (255, 255, 255)
    ).convert_alpha()

    title_rect = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    if elapsed < THURSDAY_FADE_IN:
        alpha = int(255 * elapsed / THURSDAY_FADE_IN)

    elif elapsed < THURSDAY_FADE_IN + THURSDAY_TITLE_HOLD:
        alpha = 255

    elif elapsed < (
        THURSDAY_FADE_IN
        + THURSDAY_TITLE_HOLD
        + THURSDAY_FADE_OUT
    ):
        fade_elapsed = (
            elapsed - THURSDAY_FADE_IN - THURSDAY_TITLE_HOLD
        )

        alpha = int(
            255 * (1 - fade_elapsed / THURSDAY_FADE_OUT)
        )

    else:
        # Title has disappeared.
        # Begin Mom's dialogue while keeping the screen black.
        current_scene = "thursday_mom"
        dialogues = thursday_mom_dialogues
        dialogue_index = 0

        reset_typewriter()
        stop_voice()

        print("THURSDAY: Mom dialogue begins")
        return

    title_surface.set_alpha(max(0, min(255, alpha)))
    screen.blit(title_surface, title_rect)


# =====================================
# NEW THURSDAY TITLE TRANSITION
# =====================================

NEW_THURSDAY_FADE = 1500
NEW_THURSDAY_TITLE_HOLD = 2000

new_thursday_start = 0
new_thursday_background = None



# =====================================
# THURSDAY NIGHT -> FRIDAY MORNING
# =====================================

FRIDAY_FADE = 1500
FRIDAY_TITLE_FADE = 1000
FRIDAY_TITLE_HOLD = 2000

friday_transition_start = 0
friday_transition_background = None

friday_breakfast_active = False
friday_breakfast_finished = False



# =====================================
# FRIDAY SCHOOL MONTAGE STATE
# =====================================

friday_school_start = 0
friday_montage_start = 0
friday_montage_penalty_applied = False

FRIDAY_SCHOOL_FADE = 1500
FRIDAY_SCHOOL_BLACK_HOLD = 1000

FRIDAY_MONTAGE_SCENE_DURATION = 1200


# Function: start_friday_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_friday_transition():
    global current_scene
    global friday_transition_start
    global friday_transition_background

    friday_transition_start = pygame.time.get_ticks()
    friday_transition_background = screen.copy()

    current_scene = "friday_transition"
    stop_voice()


# Function: draw_friday_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_friday_transition():
    global current_scene, dialogues, dialogue_index
    global friday_breakfast_active, friday_breakfast_finished

    elapsed = pygame.time.get_ticks() - friday_transition_start

    screen.fill((0, 0, 0))

    # 1. Fade the bedroom to black.
    if elapsed < FRIDAY_FADE:
        screen.blit(friday_transition_background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(int(255 * elapsed / FRIDAY_FADE))
        screen.blit(overlay, (0, 0))
        return

    title_elapsed = elapsed - FRIDAY_FADE
    fade = FRIDAY_TITLE_FADE
    hold = FRIDAY_TITLE_HOLD

    # 2. FRIDAY title fades in, holds, then fades out.
    if title_elapsed < fade:
        alpha = int(255 * title_elapsed / fade)
    elif title_elapsed < fade + hold:
        alpha = 255
    elif title_elapsed < fade * 2 + hold:
        alpha = int(
            255 * (1 - (title_elapsed - fade - hold) / fade)
        )
    else:
        # 3. Enter Friday's breakfast.
        current_scene = "scene6"
        dialogues = scene6_friday_dialogues
        dialogue_index = 0

        friday_breakfast_active = True
        friday_breakfast_finished = False

        restore_stats_after_sleep()

        stop_voice()
        reset_typewriter()

        print("FRIDAY: Breakfast begins")
        return

    title = title_font.render(
        "FRIDAY", True, (255, 255, 255)
    ).convert_alpha()

    title.set_alpha(max(0, min(255, alpha)))
    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    )


# Function: start_saturday_transition — Begin the Saturday title sequence after Friday ends.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_saturday_transition():
    global current_scene
    global saturday_transition_start
    global saturday_transition_background

    saturday_transition_background = screen.copy()
    saturday_transition_start = pygame.time.get_ticks()

    current_scene = "saturday_transition"
    stop_voice()


# Function: draw_saturday_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_saturday_transition():
    global current_scene, dialogues, dialogue_index
    global saturday_breakfast_active

    elapsed = pygame.time.get_ticks() - saturday_transition_start

    fade = SATURDAY_FADE
    title_fade = SATURDAY_TITLE_FADE
    hold = SATURDAY_TITLE_HOLD

    screen.fill((0, 0, 0))

    # Stage 1: Bedroom fades to black.
    if elapsed < fade:
        screen.blit(saturday_transition_background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(int(255 * elapsed / fade))
        screen.blit(overlay, (0, 0))
        return

    title_elapsed = elapsed - fade

    # Stage 2: SATURDAY fades in.
    if title_elapsed < title_fade:
        alpha = int(255 * title_elapsed / title_fade)

    # Stage 3: Hold SATURDAY.
    elif title_elapsed < title_fade + hold:
        alpha = 255

    # Stage 4: Fade the title away.
    elif title_elapsed < title_fade * 2 + hold:
        progress = (
            title_elapsed - title_fade - hold
        ) / title_fade

        alpha = int(255 * (1 - progress))

    # Stage 5: Enter Saturday breakfast.
    else:
        current_scene = "scene6"
        dialogues = saturday_breakfast_dialogues
        dialogue_index = 0
        saturday_breakfast_active = True

        stop_voice()
        reset_typewriter()

        print("SATURDAY: Weekend trial breakfast")
        return

    title = title_font.render(
        "SATURDAY", True, (255, 255, 255)
    ).convert_alpha()

    title.set_alpha(max(0, min(255, alpha)))

    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    )


# Function: start_friday_night_transition — Transition to Friday dinner or the study group, depending on the saved route.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_friday_night_transition(target):
    global current_scene
    global friday_night_transition_start
    global friday_night_transition_background
    global friday_night_transition_target

    friday_night_transition_background = screen.copy()
    friday_night_transition_start = pygame.time.get_ticks()
    friday_night_transition_target = target

    current_scene = "friday_night_transition"
    stop_voice()


# Function: draw_friday_night_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_friday_night_transition():
    global current_scene, dialogues, dialogue_index
    global friday_night_route
    global friday_study_penalty_applied

    elapsed = (
        pygame.time.get_ticks()
        - friday_night_transition_start
    )

    if elapsed < FRIDAY_NIGHT_FADE:
        screen.blit(
            friday_night_transition_background,
            (0, 0)
        )

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(
            int(255 * elapsed / FRIDAY_NIGHT_FADE)
        )
        screen.blit(overlay, (0, 0))
        return

    if elapsed < FRIDAY_NIGHT_FADE + FRIDAY_NIGHT_BLACK:
        screen.fill((0, 0, 0))
        return

    target = friday_night_transition_target

    if target == "scene13":
        current_scene = "scene13"
        friday_night_route = "home"
        dialogues = friday_home_dinner_dialogues

    elif target == "scene25":
        current_scene = "scene25"
        friday_night_route = "study"
        friday_study_penalty_applied = False
        dialogues = friday_study_group_intro_dialogues

    elif target == "friday_bedroom":
        current_scene = "friday_bedroom"
        dialogues = friday_final_bedroom_dialogues

    else:
        print("UNKNOWN FRIDAY DESTINATION:", target)
        return

    dialogue_index = 0
    stop_voice()
    reset_typewriter()

    print("FRIDAY NIGHT ENTERED:", current_scene)

# Function: start_friday_study_silence — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_friday_study_silence():
    global current_scene, friday_study_silence_start

    friday_study_silence_start = pygame.time.get_ticks()
    current_scene = "friday_study_silence"

    stop_voice()


# Function: draw_friday_study_silence — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_friday_study_silence():
    global current_scene, dialogues, dialogue_index

    screen.blit(scene25, (0, 0))

    elapsed = (
        pygame.time.get_ticks()
        - friday_study_silence_start
    )

    if elapsed < FRIDAY_STUDY_SILENCE:
        return

    current_scene = "scene25_insult"
    dialogues = friday_study_group_insult_dialogues
    dialogue_index = 0

    stop_voice()
    reset_typewriter()


# Function: start_friday_school_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_friday_school_transition():
    """Fade out Friday breakfast before entering Scene 7."""
    global current_scene, friday_school_start

    friday_school_start = pygame.time.get_ticks()
    current_scene = "friday_school_transition"

    stop_voice()


# Function: draw_friday_school_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_friday_school_transition():
    """Fade breakfast to black, then enter Scene 7."""
    global current_scene, dialogues, dialogue_index
    global friday_montage_penalty_applied

    elapsed = pygame.time.get_ticks() - friday_school_start

    if elapsed < FRIDAY_SCHOOL_FADE:
        screen.blit(scene6, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(
            int(255 * elapsed / FRIDAY_SCHOOL_FADE)
        )
        screen.blit(overlay, (0, 0))

    elif elapsed < (
        FRIDAY_SCHOOL_FADE + FRIDAY_SCHOOL_BLACK_HOLD
    ):
        screen.fill((0, 0, 0))

    else:
        current_scene = "friday_school_intro"
        dialogues = friday_school_intro_dialogues
        dialogue_index = 0

        friday_montage_penalty_applied = False

        stop_voice()
        reset_typewriter()

        print("FRIDAY: School intro started")



# Function: start_saturday_court_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_saturday_court_transition():
    global current_scene
    global saturday_court_start
    global saturday_court_background

    saturday_court_background = screen.copy()
    saturday_court_start = pygame.time.get_ticks()

    current_scene = "saturday_court_transition"
    stop_voice()


# Function: draw_saturday_court_transition — Fade from Saturday breakfast into the courtroom.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_saturday_court_transition():
    global current_scene, saturday_court_ready
    global saturday_breakfast_active
    global dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - saturday_court_start

    if elapsed < SATURDAY_FADE:
        # Fade the breakfast scene out.
        screen.blit(saturday_court_background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(
            int(255 * elapsed / SATURDAY_FADE)
        )
        screen.blit(overlay, (0, 0))
        return

    elif elapsed < SATURDAY_FADE + SATURDAY_BLACK_HOLD:
        screen.fill((0, 0, 0))
        return

    # Arrive at Scene 26.


    # Enter the courtroom.
    current_scene = "scene26"
    saturday_court_ready = True
    saturday_breakfast_active = False

    # Start the opening trial dialogue.
    dialogues = trial_opening_dialogues
    dialogue_index = 0

    stop_voice()
    reset_typewriter()

    print("SATURDAY: Trial opening dialogue started")


# =====================================
# SATURDAY TRIAL - SPEAKER CAMERA
# =====================================

# State: TRIAL_BACKGROUNDS — Associate each trial speaker with their courtroom image.
TRIAL_BACKGROUNDS = {
    "Dad": scene26,
    "Mom": scene27,
    "Little F": scene28,
}


# State: TRIAL_FLASH_IMAGES — Map courtroom callouts to the corresponding overlay art.
TRIAL_FLASH_IMAGES = {
    "objection": objection_image,
    "take_that": take_that_image,
    "hold_it": hold_it_image,
}


# Function: set_trial_dialogues — Game helper: execute the named behavior; review callers and shared state before modifying.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def set_trial_dialogues(scene_name, lines):
    global current_scene, dialogues, dialogue_index
    global trial_last_line

    current_scene = scene_name
    dialogues = lines
    dialogue_index = 0
    trial_last_line = None

    stop_voice()
    reset_typewriter()


# Function: start_trial_flash — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_trial_flash(kind):
    global trial_flash_kind, trial_flash_start

    trial_flash_kind = kind
    trial_flash_start = pygame.time.get_ticks()


# Function: draw_trial_flash — Display the timed OBJECTION, HOLD IT or TAKE THAT splash image.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_trial_flash():
    global trial_flash_kind

    if trial_flash_kind is None:
        return

    elapsed = pygame.time.get_ticks() - trial_flash_start

    if elapsed >= TRIAL_FLASH_DURATION:
        trial_flash_kind = None
        return

    image = TRIAL_FLASH_IMAGES[trial_flash_kind]

    # A short, dramatic pop-in.
    progress = min(1.0, elapsed / 120)
    scale = 0.65 + 0.35 * progress

    target_w = int(WIDTH * 0.78 * scale)
    target_h = int(
        image.get_height()
        * target_w / image.get_width()
    )

    scaled = pygame.transform.scale(
        image, (target_w, target_h)
    )

    rect = scaled.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    screen.blit(scaled, rect)


# Function: draw_trial_scene — COURT CAMERA: Select the active speaker background for Dad, Mom or Little F.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_trial_scene():
    global trial_last_line

    background = scene26

    if dialogue_index < len(dialogues):
        name, expression, text = parse_dialogue_entry(
            dialogues[dialogue_index]
        )
        background = TRIAL_BACKGROUNDS.get(name, scene26)

        # Trigger the appropriate flash only once per line.
        line_key = (current_scene, dialogue_index)

        if line_key != trial_last_line:
            trial_last_line = line_key

            if current_scene == "scene26":
                if dialogue_index in (2, 5):
                    start_trial_flash("objection")
                elif dialogue_index == 8:
                    start_trial_flash("hold_it")

            elif current_scene == "trial_present":
                if dialogue_index == 0:
                    start_trial_flash("take_that")

    screen.blit(background, (0, 0))

    # Dialogue box and Animalese, without portraits.
    draw_dialogue()
    draw_trial_flash()


# Function: draw_trial_inventory — Draw the trial inventory; its hitbox is provided by get_trial_paper_rect.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_trial_inventory():
    # Full inventory image containing the test paper.
    image = pygame.transform.scale(
        trial_inventory_image, (WIDTH, HEIGHT)
    )
    screen.blit(image, (0, 0))



# Function: get_trial_paper_rect — Retrieve or calculate the requested resource or value.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def get_trial_paper_rect():
    # Clickable area for the first inventory slot.
    # Based on the inventory image scaled to 1280x720.
    return pygame.Rect(
        int(WIDTH * 0.065),
        int(HEIGHT * 0.73),
        int(WIDTH * 0.09),
        int(HEIGHT * 0.20)
    )


# Function: select_trial_paper — Use the selected evidence item to enter the TAKE THAT dialogue.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_trial_paper():
    global trial_inventory_open

    if current_scene != "trial_inventory":
        return

    if not thursday_test_paper_owned:
        return

    trial_inventory_open = False
    set_trial_dialogues(
        "trial_present",
        trial_present_dialogues
    )
    print("TRIAL: 60-point math test presented")



# Function: resolve_trial_evidence — FINAL TRIAL: Validate the quiz choice and the 60-point test paper before allowing evidence.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def resolve_trial_evidence():
    """Determine the verdict route from Thursday's quiz."""

    has_valid_paper = (
        thursday_quiz_choice == "c"
        and thursday_test_paper_owned
    )

    print("========== TRIAL CHECK ==========")
    print("Thursday quiz:", thursday_quiz_choice)
    print("Test paper owned:", thursday_test_paper_owned)
    print("Evidence valid:", has_valid_paper)
    print("=================================")

    if has_valid_paper:
        set_trial_dialogues(
            "trial_evidence",
            trial_evidence_dialogues
        )
    else:
        set_trial_dialogues(
            "trial_no_evidence",
            trial_no_evidence_dialogues
        )



# Function: start_trial_ending_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_trial_ending_transition(target):
    global current_scene, trial_fade_start
    global trial_fade_target, trial_fade_background

    trial_fade_target = target
    trial_fade_start = pygame.time.get_ticks()
    trial_fade_background = screen.copy()

    current_scene = "trial_ending_transition"
    stop_voice()



# Function: draw_trial_ending_transition — Fade to Scene 29 or 30; initialize Scene 30 dialogue on arrival.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_trial_ending_transition():
    global current_scene, scene29_start
    global dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - trial_fade_start


    if elapsed < TRIAL_FADE_DURATION:
        screen.blit(trial_fade_background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(
            int(255 * elapsed / TRIAL_FADE_DURATION)
        )
        screen.blit(overlay, (0, 0))
        return

    if elapsed < TRIAL_FADE_DURATION + TRIAL_BLACK_HOLD:
        screen.fill((0, 0, 0))
        return

    current_scene = trial_fade_target


    if current_scene == "scene29":
        scene29_start = pygame.time.get_ticks()

    elif current_scene == "scene30":
        # Start the final book-signing dialogue.
        dialogues = scene30_dialogues
        dialogue_index = 0

        stop_voice()
        reset_typewriter()

        print("SCENE 30: Final book-signing dialogue started")

    print("TRIAL ENDING:", current_scene)


# Function: draw_scene29_ending — Display the bad-ending image before automatically entering the credits.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene29_ending():
    screen.blit(scene29, (0, 0))

    elapsed = pygame.time.get_ticks() - scene29_start

    if elapsed >= SCENE29_HOLD:
        start_credits_transition()



# Function: start_friday_montage — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_friday_montage():
    """Begin the automatic Friday classroom montage."""
    global current_scene, friday_montage_start

    friday_montage_start = pygame.time.get_ticks()
    current_scene = "friday_montage"

    stop_voice()


# Function: draw_friday_montage — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_friday_montage():
    """Cycle through Scenes 8, 9 and 10 without dialogue."""
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - friday_montage_start
    duration = FRIDAY_MONTAGE_SCENE_DURATION

    if elapsed < duration:
        screen.blit(scene8, (0, 0))

    elif elapsed < duration * 2:
        screen.blit(scene9, (0, 0))

    elif elapsed < duration * 3:
        screen.blit(scene10, (0, 0))

    else:
        # The school day ends at Scene 10.
        current_scene = "friday_school_end"
        dialogues = friday_school_end_dialogues
        dialogue_index = 0

        stop_voice()
        reset_typewriter()

        print("FRIDAY: School montage completed")


# Function: start_new_thursday_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_new_thursday_transition():
    global current_scene
    global new_thursday_start, new_thursday_background

    new_thursday_background = screen.copy()
    new_thursday_start = pygame.time.get_ticks()

    current_scene = "new_thursday_transition"
    stop_voice()


# Function: draw_new_thursday_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_new_thursday_transition():
    global current_scene, dialogues, dialogue_index
    global new_thursday_breakfast_active
    global new_thursday_breakfast_finished

    elapsed = pygame.time.get_ticks() - new_thursday_start

    fade = NEW_THURSDAY_FADE
    hold = NEW_THURSDAY_TITLE_HOLD

    screen.fill((0, 0, 0))

    # Stage 1: Fade the bedroom into black.
    if elapsed < fade:
        screen.blit(new_thursday_background, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(int(255 * elapsed / fade))
        screen.blit(overlay, (0, 0))
        return

    # Create the day title.
    title = title_font.render(
        "THURSDAY", True, (255, 255, 255)
    ).convert_alpha()

    title_rect = title.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    title_elapsed = elapsed - fade

    # Stage 2: Fade title in.
    if title_elapsed < fade:
        alpha = int(255 * title_elapsed / fade)

    # Stage 3: Hold title.
    elif title_elapsed < fade + hold:
        alpha = 255

    # Stage 4: Fade title out.
    elif title_elapsed < fade * 2 + hold:
        fade_elapsed = title_elapsed - fade - hold
        alpha = int(255 * (1 - fade_elapsed / fade))

    # Stage 5: Enter the new breakfast.
    else:
        current_scene = "scene6"
        dialogues = scene6_thursday_dialogues
        dialogue_index = 0

        new_thursday_breakfast_active = True
        new_thursday_breakfast_finished = False

        stop_voice()
        reset_typewriter()

        print("NEW THURSDAY: Breakfast started")
        return

    title.set_alpha(max(0, min(255, alpha)))
    screen.blit(title, title_rect)


# Function: start_tuesday_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_tuesday_transition():
    """Start the transition from Monday to Tuesday."""
    global current_scene
    global tuesday_transition_start
    global tuesday_transition_background

    tuesday_transition_background = screen.copy()
    tuesday_transition_start = pygame.time.get_ticks()

    current_scene = "tuesday_transition"
    stop_voice()


# Function: draw_tuesday_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_transition():
    """Show the Tuesday title before the morning scene."""
    global current_scene, dialogues, dialogue_index
    global display_hunger, display_energy, display_mood

    elapsed = pygame.time.get_ticks() - tuesday_transition_start

    title_font = pygame.font.SysFont(
        "arial", 90, bold=True
    )

    title = title_font.render(
        "TUESDAY", True, (255, 255, 255)
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    # Stage 1: Fade Monday's bedroom to black.
    if elapsed < TUESDAY_FADE_OUT:
        screen.blit(tuesday_transition_background, (0, 0))

        alpha = int(255 * elapsed / TUESDAY_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))
        return

    # Stage 2: Fade the Tuesday title in.
    title_elapsed = elapsed - TUESDAY_FADE_OUT

    if title_elapsed < TUESDAY_TITLE_FADE:
        alpha = int(
            255 * title_elapsed / TUESDAY_TITLE_FADE
        )

        screen.fill((0, 0, 0))
        title.set_alpha(alpha)
        screen.blit(title, title_rect)
        return

    # Stage 3: Hold the title on screen.
    if title_elapsed < TUESDAY_TITLE_FADE + TUESDAY_TITLE_HOLD:
        screen.fill((0, 0, 0))
        screen.blit(title, title_rect)
        return

    # Stage 4: Fade the title out.
    fade_elapsed = (
        title_elapsed
        - TUESDAY_TITLE_FADE
        - TUESDAY_TITLE_HOLD
    )

    if fade_elapsed < TUESDAY_TITLE_FADE:
        screen.fill((0, 0, 0))

        alpha = int(
            255 * (1 - fade_elapsed / TUESDAY_TITLE_FADE)
        )

        title.set_alpha(max(0, alpha))
        screen.blit(title, title_rect)
        return

    # Stage 5: Begin Tuesday morning.
    current_scene = "scene15"
    dialogues = scene15_dialogues
    dialogue_index = 0

    restore_stats_after_sleep()
    reset_typewriter()

    screen.blit(scene5, (0, 0))
    draw_dialogue()


# Function: start_intertitle — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_intertitle(text, next_scene, next_dialogues):

    """
    Schedule a title-card transition before the QTE.
    """
    global current_scene, intertitle_text, intertitle_start

    global intertitle_next_scene, intertitle_next_dialogues

    global dialogue_index, dialogues



    current_scene = "intertitle"

    intertitle_text = text

    intertitle_start = pygame.time.get_ticks()

    intertitle_next_scene = next_scene

    intertitle_next_dialogues = next_dialogues



    dialogue_index = 0

    dialogues = next_dialogues







# Function: draw_intertitle — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_intertitle():

    """
    Animate title-card transparency and proceed to the QTE afterward.
    """
    global current_scene



    elapsed = pygame.time.get_ticks() - intertitle_start



    total_time = (

        INTERTITLE_FADE_IN

        + INTERTITLE_HOLD

        + INTERTITLE_FADE_OUT

    )



    screen.fill((0, 0, 0))



    # Diagnostic logging for the intertitle during its first few frames.

    if elapsed < 100:

        print("黑幕开始，字幕：", repr(intertitle_text))



    if elapsed < INTERTITLE_FADE_IN:

        alpha = int(255 * elapsed / INTERTITLE_FADE_IN)



    elif elapsed < INTERTITLE_FADE_IN + INTERTITLE_HOLD:

        alpha = 255



    elif elapsed < total_time:

        fade_elapsed = (

            elapsed - INTERTITLE_FADE_IN

            - INTERTITLE_HOLD

        )

        alpha = int(

            255 * (1 - fade_elapsed / INTERTITLE_FADE_OUT)

        )



    else:

        print("黑幕结束，进入QTE")

        start_qte(

            intertitle_next_scene,

            intertitle_next_dialogues

        )

        return



    # Render the English intertitle using an Arial font.

    test_font = pygame.font.SysFont("arial", 80, bold=True)



    text_surface = test_font.render(

        intertitle_text, True, (255, 255, 255)

    )

    text_surface.set_alpha(alpha)



    text_rect = text_surface.get_rect(

        center=(WIDTH // 2, HEIGHT // 2)

    )

    screen.blit(text_surface, text_rect)





# Function: reset_typewriter — Restart the typewriter clock at the beginning of a new line.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def reset_typewriter():

    """
    Restart per-line text timing and stop any prior speech effects.
    """
    global text_start, last_visible_count

    text_start = pygame.time.get_ticks()

    last_visible_count = 0

    stop_voice()


# =====================================
# EVENING TRANSITION - SCENE 13
# =====================================

EVENING_FADE_OUT = 1000
EVENING_BLACK_HOLD = 2000
EVENING_FADE_IN = 1500

evening_transition_start = 0
evening_transition_background = None


# Function: start_evening_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_evening_transition():
    """Start the transition from Scene 11/12 to Scene 13."""
    global current_scene
    global evening_transition_start
    global evening_transition_background

    evening_transition_background = screen.copy()
    evening_transition_start = pygame.time.get_ticks()

    current_scene = "evening_transition"
    stop_voice()


# Function: draw_evening_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_evening_transition():
    """Fade into the evening dinner scene."""
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - evening_transition_start

    if elapsed < EVENING_FADE_OUT:
        # Gradually darken the previous scene.
        screen.blit(evening_transition_background, (0, 0))

        alpha = int(255 * elapsed / EVENING_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    elif elapsed < EVENING_FADE_OUT + EVENING_BLACK_HOLD:
        # Remain on a black screen.
        screen.fill((0, 0, 0))

    elif elapsed < (
        EVENING_FADE_OUT + EVENING_BLACK_HOLD + EVENING_FADE_IN
    ):
        # Gradually reveal the evening background.
        screen.blit(scene13, (0, 0))

        fade_elapsed = (
            elapsed - EVENING_FADE_OUT - EVENING_BLACK_HOLD
        )

        alpha = int(255 * (1 - fade_elapsed / EVENING_FADE_IN))
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    else:
        # Start Scene 13 and reset its dialogue.
        current_scene = "scene13"
        dialogues = scene13_dialogues
        dialogue_index = 0
        reset_typewriter()

        screen.blit(scene13, (0, 0))
        draw_dialogue()






# Function: start_route_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_route_transition(target_scene):
    """
    Start the transition to Scene 11 or Scene 12
    after the fourth class settlement.
    """
    global current_scene
    global route_transition_start
    global route_transition_target
    global route_transition_background
    global route_reward_applied

    if target_scene not in ("scene11", "scene12"):
        return

    route_transition_target = target_scene
    route_transition_start = pygame.time.get_ticks()
    route_transition_background = screen.copy()
    route_reward_applied = False

    current_scene = "route_transition"
    stop_voice()


# Function: draw_route_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_route_transition():
    """
    Fade out the classroom, hold black, and
    fade into the selected after-class scene.
    """
    global current_scene, dialogues, dialogue_index
    global route_reward_applied
    global display_hunger

    elapsed = pygame.time.get_ticks() - route_transition_start

    target_image = (
        scene12 if route_transition_target == "scene12"
        else scene11
    )

    # Stage 1: Fade the classroom to black.
    if elapsed < ROUTE_FADE_OUT:
        screen.blit(route_transition_background, (0, 0))

        alpha = int(255 * elapsed / ROUTE_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 2: Hold a completely black screen.
    elif elapsed < ROUTE_FADE_OUT + ROUTE_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: Reveal the destination background.
    elif elapsed < ROUTE_FADE_OUT + ROUTE_BLACK_HOLD + ROUTE_FADE_IN:
        screen.blit(target_image, (0, 0))

        fade_elapsed = (
            elapsed - ROUTE_FADE_OUT - ROUTE_BLACK_HOLD
        )

        alpha = int(
            255 * (1 - fade_elapsed / ROUTE_FADE_IN)
        )

        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 4: Apply the route effect once and enter the scene.

    # Stage 4: Apply the route effect once and enter the scene.
    else:
        if not route_reward_applied:
            route_reward_applied = True

            if route_transition_target == "scene12":
                # Restore hunger completely after eating squid.
                change_stats(hunger_change=100 - hunger)
                print("SQUID EVENT: Hunger restored to 100%")

            else:
                # Apply an additional hunger penalty.
                change_stats(hunger_change=-30)
                print("NORMAL ROUTE: Hunger decreased by 30%")

            # Synchronize the visible hunger bar.
            display_hunger = hunger
            check_bad_ending()

        # Enter a bad ending if any stat reaches zero.
        if pending_bad_ending is not None:
            start_bad_transition()
            return

        # Switch to the selected story scene.
        current_scene = route_transition_target

        if current_scene == "scene12":
            dialogues = scene12_dialogues
        else:
            dialogues = scene11_dialogues

        dialogue_index = 0
        reset_typewriter()

        screen.blit(target_image, (0, 0))
        draw_dialogue()




# =====================================
# TUESDAY CLASS 6 TRANSITION
# =====================================

TUESDAY_CLASS_FADE_OUT = 1000
TUESDAY_CLASS_BLACK_HOLD = 2000
TUESDAY_CLASS_FADE_IN = 1500

tuesday_class_transition_start = 0
tuesday_class_transition_background = None


# Function: start_tuesday_second_class_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_tuesday_second_class_transition():
    """Begin the transition to Tuesday's second class."""
    global current_scene
    global tuesday_class_transition_start
    global tuesday_class_transition_background

    tuesday_class_transition_background = screen.copy()
    tuesday_class_transition_start = pygame.time.get_ticks()

    current_scene = "tuesday_class_transition"
    stop_voice()


# Function: draw_tuesday_second_class_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_second_class_transition():
    """Fade into Scene 7 and begin Class 6."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    elapsed = pygame.time.get_ticks() - tuesday_class_transition_start

    if elapsed < TUESDAY_CLASS_FADE_OUT:
        screen.blit(tuesday_class_transition_background, (0, 0))
        alpha = int(255 * elapsed / TUESDAY_CLASS_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    elif elapsed < TUESDAY_CLASS_FADE_OUT + TUESDAY_CLASS_BLACK_HOLD:
        screen.fill((0, 0, 0))

    elif elapsed < (
        TUESDAY_CLASS_FADE_OUT
        + TUESDAY_CLASS_BLACK_HOLD
        + TUESDAY_CLASS_FADE_IN
    ):
        screen.blit(scene7, (0, 0))

        fade_elapsed = (
            elapsed
            - TUESDAY_CLASS_FADE_OUT
            - TUESDAY_CLASS_BLACK_HOLD
        )

        alpha = int(255 * (1 - fade_elapsed / TUESDAY_CLASS_FADE_IN))
        black_overlay.set_alpha(max(0, alpha))
        screen.blit(black_overlay, (0, 0))

    else:
        # Enter Tuesday's second lesson.
        class_number = 6
        current_scene = "scene7"
        dialogues = scene7_tuesday_second_dialogues
        dialogue_index = 0

        begin_class()
        class_choice_open = False
        reset_typewriter()

        print("TUESDAY: Entering Class 6")

        screen.blit(scene7, (0, 0))
        draw_dialogue()


# =====================================
# TUESDAY CLASS 7 TRANSITION
# =====================================

tuesday_class7_transition_start = 0
tuesday_class7_transition_background = None

# Function: start_tuesday_class7_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_tuesday_class7_transition():
    """Begin the transition to Tuesday afternoon."""
    global current_scene
    global tuesday_class7_transition_start
    global tuesday_class7_transition_background

    tuesday_class7_transition_background = screen.copy()
    tuesday_class7_transition_start = pygame.time.get_ticks()

    current_scene = "tuesday_class7_transition"
    stop_voice()


# Function: draw_tuesday_class7_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_class7_transition():
    """Fade from the morning break into Scene 9."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open
    global tuesday_game_choice_open

    elapsed = (
        pygame.time.get_ticks()
        - tuesday_class7_transition_start
    )

    fade_out = 1000
    black_hold = 2000
    fade_in = 1500

    if elapsed < fade_out:
        screen.blit(tuesday_class7_transition_background, (0, 0))
        black_overlay.set_alpha(int(255 * elapsed / fade_out))
        screen.blit(black_overlay, (0, 0))

    elif elapsed < fade_out + black_hold:
        screen.fill((0, 0, 0))

    elif elapsed < fade_out + black_hold + fade_in:
        screen.blit(scene9, (0, 0))
        fade_elapsed = elapsed - fade_out - black_hold
        alpha = int(255 * (1 - fade_elapsed / fade_in))
        black_overlay.set_alpha(max(0, alpha))
        screen.blit(black_overlay, (0, 0))

    else:
        # Start the seventh lesson.
        class_number = 7
        current_scene = "scene9"

        dialogues = scene9_tuesday_class7_dialogues
        dialogue_index = 0

        begin_class()
        class_choice_open = False
        tuesday_game_choice_open = False

        reset_typewriter()
        print("TUESDAY: Entering Class 7")


# =====================================
# CLASS 8 - FALLING ASLEEP TRANSITION
# =====================================

CLASS8_SLEEP_FADE = 2000
CLASS8_BLACK_HOLD = 1500

class8_sleep_start = 0
class8_sleep_background = None


# Function: start_class8_sleep_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_class8_sleep_transition():
    """Fade out the classroom as Little F falls asleep."""
    global current_scene
    global class8_sleep_start, class8_sleep_background

    class8_sleep_background = screen.copy()
    class8_sleep_start = pygame.time.get_ticks()

    current_scene = "class8_sleep_transition"
    stop_voice()


# Function: draw_class8_sleep_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class8_sleep_transition():
    """Darken the classroom before entering Scene 20."""
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - class8_sleep_start

    if elapsed < CLASS8_SLEEP_FADE:
        screen.blit(class8_sleep_background, (0, 0))

        alpha = int(255 * elapsed / CLASS8_SLEEP_FADE)

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))

    elif elapsed < CLASS8_SLEEP_FADE + CLASS8_BLACK_HOLD:
        screen.fill((0, 0, 0))

    else:
        # Little F wakes up to Jiang calling him.
        current_scene = "scene20"
        dialogues = scene20_dialogues
        dialogue_index = 0

        reset_typewriter()
        stop_voice()

        print("CLASS 8: Entering Scene 20")



# =====================================
# SCENE 20 -> CLASS 9 TRANSITION
# =====================================

CLASS9_BLACK_DURATION = 1000
class9_transition_start = 0


# Function: start_class9_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_class9_transition():
    """Begin a short black screen before afternoon class."""
    global current_scene, class9_transition_start

    class9_transition_start = pygame.time.get_ticks()
    current_scene = "class9_transition"
    stop_voice()


# Function: draw_class9_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class9_transition():
    """Enter Class 9 after the black-screen pause."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    screen.fill((0, 0, 0))

    elapsed = pygame.time.get_ticks() - class9_transition_start

    if elapsed < CLASS9_BLACK_DURATION:
        return

    class_number = 9
    current_scene = "scene9"

    dialogues = thursday_afternoon_dialogues
    dialogue_index = 0

    begin_class()
    class_choice_open = False

    reset_typewriter()
    stop_voice()

    print("THURSDAY: Entering Class 9")



# =====================================
# THURSDAY - CLASS 9 TO CLASS 10
# =====================================

CLASS10_FADE_OUT = 1500
CLASS10_BLACK_HOLD = 2000
CLASS10_FADE_IN = 1500

class10_transition_start = 0
class10_transition_background = None


# Function: start_class10_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_class10_transition():
    """Begin the transition from Class 9 to Class 10."""
    global current_scene
    global class10_transition_start
    global class10_transition_background

    class10_transition_background = screen.copy()
    class10_transition_start = pygame.time.get_ticks()

    current_scene = "class10_transition"
    stop_voice()

    print("CLASS 9: Transition to Class 10 started")


# Function: draw_class10_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class10_transition():
    """Fade out, hold black, and reveal Class 10."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    elapsed = pygame.time.get_ticks() - class10_transition_start

    # Stage 1: Gradually darken the previous scene.
    if elapsed < CLASS10_FADE_OUT:
        screen.blit(class10_transition_background, (0, 0))

        alpha = int(255 * elapsed / CLASS10_FADE_OUT)

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)

        screen.blit(overlay, (0, 0))

    # Stage 2: Hold a completely black screen.
    elif elapsed < CLASS10_FADE_OUT + CLASS10_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: Gradually reveal the classroom.
    elif elapsed < (
        CLASS10_FADE_OUT
        + CLASS10_BLACK_HOLD
        + CLASS10_FADE_IN
    ):
        screen.blit(scene9, (0, 0))

        fade_elapsed = (
            elapsed - CLASS10_FADE_OUT - CLASS10_BLACK_HOLD
        )

        alpha = int(
            255 * (1 - fade_elapsed / CLASS10_FADE_IN)
        )

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(max(0, alpha))

        screen.blit(overlay, (0, 0))

    # Stage 4: Enter Class 10.
    else:
        class_number = 10
        current_scene = "scene9"

        dialogues = class10_dialogues
        dialogue_index = 0

        begin_class()
        class_choice_open = False

        stop_voice()
        reset_typewriter()

        print("THURSDAY: Class 10 started")


# Function: start_afternoon_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_afternoon_transition(next_class=False):
    global current_scene
    global afternoon_transition_start
    global afternoon_transition_background
    global afternoon_next_class

    # Remember whether this transition begins Class 4.
    afternoon_next_class = next_class

    # Capture the current scene before fading out.
    afternoon_transition_background = screen.copy()
    afternoon_transition_start = pygame.time.get_ticks()

    current_scene = "afternoon_transition"
    stop_voice()



# Function: draw_afternoon_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_afternoon_transition():
    global current_scene, dialogues, dialogue_index
    global display_mood
    global class_number

    elapsed = pygame.time.get_ticks() - afternoon_transition_start

    # Stage 1: Fade out the homework scene.
    if elapsed < AFTERNOON_FADE_OUT:
        screen.blit(afternoon_transition_background, (0, 0))

        alpha = int(255 * elapsed / AFTERNOON_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 2: Hold a fully black screen.
    elif elapsed < AFTERNOON_FADE_OUT + AFTERNOON_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: Reveal the afternoon background.
    elif elapsed < (
        AFTERNOON_FADE_OUT + AFTERNOON_BLACK_HOLD + AFTERNOON_FADE_IN
    ):
        screen.blit(scene9, (0, 0))

        fade_elapsed = (
            elapsed - AFTERNOON_FADE_OUT - AFTERNOON_BLACK_HOLD
        )

        alpha = int(255 * (1 - fade_elapsed / AFTERNOON_FADE_IN))
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 4: Enter Scene 9 and begin its dialogue.


    else:
        current_scene = "scene9"

        if afternoon_next_class:
            # Start the fourth class.
            class_number = 4
            dialogues = scene9_fourth_dialogues

        else:
            # Start the third class after the homework event.
            class_number = 3
            dialogues = scene9_dialogues

        dialogue_index = 0
        reset_typewriter()

        screen.blit(scene9, (0, 0))
        draw_dialogue()


# Function: start_scene21_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene21_transition():
    """Start the fade transition from Class 10 to Scene 21."""
    global current_scene
    global scene21_transition_active
    global scene21_transition_start
    global scene21_transition_background

    scene21_transition_active = True
    scene21_transition_start = pygame.time.get_ticks()
    scene21_transition_background = screen.copy()

    current_scene = "scene21_transition"
    stop_voice()

    print("SCENE21 TRANSITION: Started")


# Function: draw_scene21_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene21_transition():
    """Fade out from Class 10 and fade into Scene 21."""
    global current_scene, dialogues, dialogue_index
    global scene21_transition_active

    elapsed = pygame.time.get_ticks() - scene21_transition_start

    # Stage 1: fade out current scene
    if elapsed < SCENE21_FADE_OUT:
        screen.blit(scene21_transition_background, (0, 0))

        alpha = int(255 * elapsed / SCENE21_FADE_OUT)

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))

    # Stage 2: black screen hold
    elif elapsed < SCENE21_FADE_OUT + SCENE21_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: fade into Scene 21
    elif elapsed < SCENE21_FADE_OUT + SCENE21_BLACK_HOLD + SCENE21_FADE_IN:
        screen.blit(scene21, (0, 0))

        fade_elapsed = elapsed - SCENE21_FADE_OUT - SCENE21_BLACK_HOLD
        alpha = int(255 * (1 - fade_elapsed / SCENE21_FADE_IN))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(max(0, alpha))
        screen.blit(overlay, (0, 0))

    # Stage 4: officially enter Scene 21
    else:
        current_scene = "scene21"
        dialogues = scene21_dialogues
        dialogue_index = 0

        scene21_transition_active = False

        stop_voice()
        reset_typewriter()

        print("SCENE21 TRANSITION: Entered Scene 21")

# Function: start_scene22_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene22_transition():
    global current_scene, scene22_transition_start
    global scene22_choice_open, scene22_choice_made
    global scene22_energy_reward_given

    current_scene = "scene22_transition"
    scene22_transition_start = pygame.time.get_ticks()

    scene22_choice_open = False
    scene22_choice_made = None
    scene22_energy_reward_given = False

    stop_voice()
    reset_typewriter()

# Function: draw_scene22_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene22_transition():
    global current_scene, dialogues, dialogue_index

    elapsed = pygame.time.get_ticks() - scene22_transition_start
    total = SCENE22_FADE_OUT + SCENE22_BLACK_HOLD + SCENE22_FADE_IN

    # Stage 1: fade to black
    if elapsed < SCENE22_FADE_OUT:
        screen.fill((0, 0, 0))
        alpha = int(255 * elapsed / SCENE22_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 2: hold black
    elif elapsed < SCENE22_FADE_OUT + SCENE22_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: fade into scene22
    elif elapsed < total:
        screen.blit(scene22, (0, 0))
        fade_elapsed = elapsed - SCENE22_FADE_OUT - SCENE22_BLACK_HOLD
        alpha = int(255 * (1 - fade_elapsed / SCENE22_FADE_IN))
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 4: enter scene22
    else:
        current_scene = "scene22"
        dialogues = scene22_dialogues
        dialogue_index = 0
        reset_typewriter()

# Function: draw_scene22_choices — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene22_choices():
    accept_rect = choice_accept_ui.get_rect(center=(WIDTH // 2, 470))
    decline_rect = choice_decline_ui.get_rect(center=(WIDTH // 2, 580))

    screen.blit(choice_accept_ui, accept_rect)
    screen.blit(choice_decline_ui, decline_rect)

    return accept_rect, decline_rect

# Function: start_scene22_vape_animation — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene22_vape_animation():
    global current_scene, scene22_vape_anim_start
    current_scene = "scene22_vape_anim"
    scene22_vape_anim_start = pygame.time.get_ticks()
    stop_voice()


# Function: draw_scene22_vape_anim — Animate the vape item scaling up and sliding offscreen.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene22_vape_anim():
    global current_scene, dialogues, dialogue_index

    screen.blit(scene22, (0, 0))

    elapsed = pygame.time.get_ticks() - scene22_vape_anim_start
    total = SCENE22_VAPE_POP_DURATION + SCENE22_VAPE_SLIDE_DURATION

    base_w, base_h = vape_icon.get_size()

    # Stage 1: pop bigger in center
    if elapsed < SCENE22_VAPE_POP_DURATION:
        progress = elapsed / SCENE22_VAPE_POP_DURATION

        scale = 0.2 + 0.8 * progress
        new_w = int(base_w * scale)
        new_h = int(base_h * scale)

        scaled_icon = pygame.transform.smoothscale(vape_icon, (new_w, new_h))
        rect = scaled_icon.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(scaled_icon, rect)

    # Stage 2: slide to the right edge
    elif elapsed < total:
        progress = (elapsed - SCENE22_VAPE_POP_DURATION) / SCENE22_VAPE_SLIDE_DURATION

        scale = 1.0
        new_w = int(base_w * scale)
        new_h = int(base_h * scale)

        scaled_icon = pygame.transform.smoothscale(vape_icon, (new_w, new_h))

        start_x = WIDTH // 2
        end_x = WIDTH + new_w // 2
        current_x = int(start_x + (end_x - start_x) * progress)

        rect = scaled_icon.get_rect(center=(current_x, HEIGHT // 2))
        screen.blit(scaled_icon, rect)

    # Stage 3: enter Little F reaction dialogue
    else:
        current_scene = "scene22_accept_result"
        dialogues = scene22_accept_dialogues
        dialogue_index = 0
        reset_typewriter()



# Function: start_scene24 — Enter the correct exam-results branch based on the Thursday quiz choice.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene24():
    global current_scene, dialogues, dialogue_index
    global scene24_paper_start, thursday_test_paper_owned

    stop_voice()

    if thursday_quiz_choice == "c":
        # Copied Sun's answers: receive the 60-point paper.
        thursday_test_paper_owned = True
        scene24_paper_start = pygame.time.get_ticks()
        current_scene = "scene24_paper_anim"

    elif thursday_quiz_choice == "b":
        # Honest answer: no paper reward.
        current_scene = "scene24_honest"
        dialogues = scene24_honest_dialogues
        dialogue_index = 0
        reset_typewriter()


    elif thursday_quiz_choice == "b":
        # Honest answer must not retain a previous test paper.
        thursday_test_paper_owned = False

        current_scene = "scene24_honest"
        dialogues = scene24_honest_dialogues
        dialogue_index = 0
        reset_typewriter()



# Function: draw_scene24_paper_anim — Animate the earned 60-point paper enlarging and sliding offscreen.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene24_paper_anim():
    global current_scene, dialogues, dialogue_index

    screen.blit(scene24, (0, 0))

    elapsed = pygame.time.get_ticks() - scene24_paper_start
    total = SCENE24_POP_DURATION + SCENE24_SLIDE_DURATION

    # Keep the complete paper within a useful visual size.
    target_height = int(HEIGHT * 0.65)
    target_width = int(
        test_paper_icon.get_width()
        * target_height / test_paper_icon.get_height()
    )

    if elapsed < total:
        if elapsed < SCENE24_POP_DURATION:
            progress = elapsed / SCENE24_POP_DURATION
            scale = 0.15 + 0.85 * min(1.0, progress * 4)
            center_x = WIDTH // 2

        else:
            progress = (
                elapsed - SCENE24_POP_DURATION
            ) / SCENE24_SLIDE_DURATION

            scale = 1.0
            center_x = int(
                WIDTH // 2
                + (WIDTH + target_width // 2 - WIDTH // 2)
                * progress
            )

        new_width = max(1, int(target_width * scale))
        new_height = max(1, int(target_height * scale))

        image = pygame.transform.scale(
            test_paper_icon,
            (new_width, new_height)
        )

        rect = image.get_rect(
            center=(center_x, HEIGHT // 2)
        )

        screen.blit(image, rect)

    else:
        # After the inventory animation, play Little F's dialogue.
        current_scene = "scene24_cheat"
        dialogues = scene24_cheat_dialogues
        dialogue_index = 0

        stop_voice()
        reset_typewriter()


# Function: start_scene24_night_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_scene24_night_transition():
    global current_scene
    global scene24_fade_start, scene24_fade_background

    scene24_fade_background = screen.copy()
    scene24_fade_start = pygame.time.get_ticks()

    current_scene = "scene24_night_transition"
    stop_voice()


# Function: draw_scene24_night_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_scene24_night_transition():
    global current_scene, dialogues, dialogue_index
    global quiz_night_active

    elapsed = pygame.time.get_ticks() - scene24_fade_start

    if elapsed < SCENE24_FADE_DURATION:
        screen.blit(scene24_fade_background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))

        alpha = int(
            255 * elapsed / SCENE24_FADE_DURATION
        )

        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))

    elif elapsed < (
        SCENE24_FADE_DURATION + SCENE24_BLACK_DURATION
    ):
        screen.fill((0, 0, 0))

    else:
        # Return to the bedroom.
        current_scene = "scene14"
        dialogues = scene14_quiz_night_dialogues
        dialogue_index = 0

        quiz_night_active = True

        stop_voice()
        reset_typewriter()

        print("SCENE 24 -> QUIZ NIGHT BEDROOM")

# =====================================
# SCENE 22 -> THURSDAY CLASS 12
# =====================================

# Function: enter_thursday_next_class_after_scene22 — Enter the next story phase and set its scene and dialogue.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def enter_thursday_next_class_after_scene22():
    """Enter Thursday's second lesson after the vape event."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    # Thursday's second class.
    class_number = 12
    current_scene = "scene7"

    # Load the new teacher dialogue.
    dialogues = scene7_thursday_second_class_dialogues
    dialogue_index = 0

    # Reset the classroom system.
    class_choice_open = False
    begin_class()

    # Reset audio and typewriter.
    stop_voice()
    reset_typewriter()

    print("SCENE 22 -> CLASS 12")



# =====================================
# SCENE 22 - A/B CHOICE HANDLER
# =====================================

# Function: select_scene22_choice — Remember the vape decision; it affects access to Sun's quiz answers.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def select_scene22_choice(choice):
    """Handle Accept / Decline choice in Scene 22."""
    global scene22_choice_open, scene22_choice_made
    global current_scene, dialogues, dialogue_index
    global thursday_vape_choice

    if current_scene != "scene22":
        return

    if not scene22_choice_open:
        return

    # Close the choice menu.
    scene22_choice_open = False

    # Save the decision for the afternoon event.
    scene22_choice_made = choice
    thursday_vape_choice = choice

    stop_voice()

    if choice == "accept":
        # A: Play the vape animation.
        start_scene22_vape_animation()

    elif choice == "decline":
        # B: Little F refuses.
        current_scene = "scene22_decline_result"
        dialogues = scene22_decline_dialogues
        dialogue_index = 0
        reset_typewriter()

    print("SCENE 22 CHOICE:", choice)



# Function: enter_thursday_class13 — Enter the next story phase and set its scene and dialogue.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def enter_thursday_class13():
    """Start Thursday afternoon's first lesson."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    class_number = 13
    current_scene = "scene9"
    dialogues = class13_dialogues
    dialogue_index = 0

    begin_class()
    class_choice_open = False

    stop_voice()
    reset_typewriter()

    print("THURSDAY: Class 13 started")


# Function: start_sun_quiz_event — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_sun_quiz_event():
    """Start Sun's conversation after Class 13."""
    global current_scene, dialogues, dialogue_index
    global sun_quiz_phase

    current_scene = "thursday_sun_event"
    dialogues = sun_quiz_intro_dialogues
    dialogue_index = 0
    sun_quiz_phase = "intro"

    stop_voice()
    reset_typewriter()


# Function: enter_scene23 — Enter the next story phase and set its scene and dialogue.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def enter_scene23():
    """Enter the quiz scene with route-dependent choices."""
    global current_scene, dialogues, dialogue_index
    global scene23_choice_open

    current_scene = "scene23"
    dialogues = []
    dialogue_index = 0
    scene23_choice_open = True

    stop_voice()
    print("SCENE 23: Quiz choices ready")

# =====================================
# TUESDAY SCHOOL TRANSITION
# =====================================

TUESDAY_SCHOOL_FADE_OUT = 1000
TUESDAY_SCHOOL_BLACK_HOLD = 2000
TUESDAY_SCHOOL_FADE_IN = 1500

tuesday_school_start = 0
tuesday_school_background = None


# Function: start_tuesday_school_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_tuesday_school_transition():
    """Start the transition from Tuesday breakfast to class."""
    global current_scene, tuesday_school_start
    global tuesday_school_background

    tuesday_school_background = screen.copy()
    tuesday_school_start = pygame.time.get_ticks()

    current_scene = "tuesday_school_transition"
    stop_voice()


# Function: draw_tuesday_school_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_tuesday_school_transition():
    """Fade out breakfast and reveal the classroom."""
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open

    elapsed = pygame.time.get_ticks() - tuesday_school_start

    if elapsed < TUESDAY_SCHOOL_FADE_OUT:
        # Fade the breakfast scene to black.
        screen.blit(tuesday_school_background, (0, 0))

        alpha = int(
            255 * elapsed / TUESDAY_SCHOOL_FADE_OUT
        )
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    elif elapsed < (
        TUESDAY_SCHOOL_FADE_OUT + TUESDAY_SCHOOL_BLACK_HOLD
    ):
        # Hold a completely black screen.
        screen.fill((0, 0, 0))

    elif elapsed < (
        TUESDAY_SCHOOL_FADE_OUT
        + TUESDAY_SCHOOL_BLACK_HOLD
        + TUESDAY_SCHOOL_FADE_IN
    ):
        # Fade into the classroom.
        screen.blit(scene7, (0, 0))

        fade_elapsed = (
            elapsed
            - TUESDAY_SCHOOL_FADE_OUT
            - TUESDAY_SCHOOL_BLACK_HOLD
        )

        alpha = int(
            255 * (1 - fade_elapsed / TUESDAY_SCHOOL_FADE_IN)
        )

        black_overlay.set_alpha(max(0, alpha))
        screen.blit(black_overlay, (0, 0))

    else:
        # Enter Tuesday's first class.
        class_number = 5

        current_scene = "scene7"
        dialogues = scene7_tuesday_dialogues
        dialogue_index = 0

        # Reset the activity selection without changing stats.
        begin_class()
        class_choice_open = False

        reset_typewriter()

        print("TUESDAY: Entering Class 5")

        screen.blit(scene7, (0, 0))
        draw_dialogue()



# Function: start_class_loop_transition — Start an event or transition and initialize its state and clock.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_class_loop_transition():
    global current_scene
    global class_transition_start
    global class_transition_background

    # Capture the final frame of Scene 8.
    class_transition_background = screen.copy()

    # Record when the transition starts.
    class_transition_start = pygame.time.get_ticks()

    # Enter the transition state.
    current_scene = "class_loop_transition"

    # Stop any remaining character voice.
    stop_voice()


# Function: draw_class_loop_transition — Render this scene or animation on each frame of the main loop.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_class_loop_transition():
    global current_scene, dialogues, dialogue_index
    global class_choice_open

    elapsed = pygame.time.get_ticks() - class_transition_start

    # Stage 1: Gradually fade Scene 8 to black.
    if elapsed < CLASS_FADE_OUT:
        screen.blit(class_transition_background, (0, 0))

        alpha = int(255 * elapsed / CLASS_FADE_OUT)
        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 2: Hold the black screen.
    elif elapsed < CLASS_FADE_OUT + CLASS_BLACK_HOLD:
        screen.fill((0, 0, 0))

    # Stage 3: Gradually reveal the classroom.
    elif elapsed < CLASS_FADE_OUT + CLASS_BLACK_HOLD + CLASS_FADE_IN:
        screen.blit(scene7, (0, 0))

        fade_elapsed = elapsed - CLASS_FADE_OUT - CLASS_BLACK_HOLD
        alpha = int(255 * (1 - fade_elapsed / CLASS_FADE_IN))

        black_overlay.set_alpha(alpha)
        screen.blit(black_overlay, (0, 0))

    # Stage 4: Enter the next class.
    else:
        current_scene = "scene7"
        dialogues = scene7_second_dialogues
        dialogue_index = 0

        # Reset the classroom selection, not player stats.
        begin_class()
        class_choice_open = False

        reset_typewriter()

        screen.blit(scene7, (0, 0))
        draw_dialogue()







# ==============================

# WAKE UP quick-time event: count spacebar presses and flash the prompt image.

# ==============================



# Function: start_qte — Initialize the opening wake-up quick-time event.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def start_qte(next_scene, next_dialogues):

    """
    Initialize the WAKE UP challenge and remember its destination.
    """
    global current_scene, qte_press_count

    global qte_start_time, qte_next_scene

    global qte_next_dialogues



    # Enter QTE mode rather than advancing the story normally.

    current_scene = "wake_qte"



    # Reset the counter so every new QTE requires all presses.

    qte_press_count = 0



    # Record the start timestamp used to animate the flashing QTE prompt.

    qte_start_time = pygame.time.get_ticks()



    # Save the scene and dialogue to load after the QTE succeeds.

    qte_next_scene = next_scene

    qte_next_dialogues = next_dialogues



    stop_voice()


    # Switch to the second soundtrack at the WAKE UP QTE.
    pygame.mixer.music.load(
        str(ASSETS / "wake_up_music.ogg")
    )
    pygame.mixer.music.set_volume(0.35)
    pygame.mixer.music.play(loops=-1, fade_ms=1000)




# Function: press_qte_space — Handle the QTE spacebar input and progress.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def press_qte_space():

    """
    Count QTE key presses and advance once the target is reached.
    """
    global qte_press_count, current_scene

    global dialogues, dialogue_index



    # Count one additional spacebar press.

    qte_press_count += 1



    print("WAKE UP:", qte_press_count, "/", QTE_REQUIRED_PRESSES)



    # When all required presses are reached, continue to the configured next scene.

    if qte_press_count >= QTE_REQUIRED_PRESSES:



        current_scene = qte_next_scene

        dialogues = qte_next_dialogues

        dialogue_index = 0



        reset_typewriter()





# Function: draw_qte — Render the wake-up QTE and its progress display.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_qte():



    # Clear the screen to black before rendering the flashing prompt.

    """
    Flash the WAKE UP overlay against a black screen.
    """
    screen.fill((0, 0, 0))



    elapsed = pygame.time.get_ticks() - qte_start_time



    # Toggle the overlay visibility at the configured QTE flash interval.

    visible = (elapsed // QTE_FLASH_INTERVAL) % 2 == 0



    if visible:

        screen.blit(wake_up_image, wake_up_rect)





# =====================================
# DEVELOPER MODE - SCENE TELEPORT
# =====================================

DEBUG_MODE = True
debug_jump_open = False
debug_scene_input = ""

# Format: scene name -> (background scene, dialogue list, class number)
# State: DEBUG_SCENES — F1 debug destinations and the dialogue/class state loaded for each.
DEBUG_SCENES = {
    "1": ("scene1", None, 1),
    "2": ("scene2", scene2_dialogues, 1),
    "3": ("scene3", scene3_dialogues, 1),
    "4": ("scene4", scene4_dialogues, 1),
    "5": ("scene5", scene5_dialogues, 1),
    "6": ("scene6", scene6_dialogues, 1),
    "7": ("scene7", scene7_dialogues, 1),
    "8": ("scene8", scene8_dialogues, 1),
    "9": ("scene9", scene9_dialogues, 3),
    "10": ("scene10", scene10_dialogues, 3),
    "11": ("scene11", scene11_dialogues, 4),
    "12": ("scene12", scene12_dialogues, 4),
    "13": ("scene13", scene13_dialogues, 4),
    "14": ("scene14", scene14_dialogues, 4),
    "15": ("scene15", scene15_dialogues, 4),
    "16": ("scene16", scene16_mom_dialogues, 4),
    "18": ("scene18", scene18_dialogues, 7),
    "19": ("scene19", scene19_dialogues, 7),
    "20": ("scene20", scene20_dialogues, 8),
    
    "22": ("scene22", scene22_dialogues, 11),

    "25": (
        "scene25",
        friday_study_group_intro_dialogues,
        13
    ),

    "friday_home": (
        "scene13",
        friday_home_dinner_dialogues,
        13
    ),

    "friday_bedroom": (
        "friday_bedroom",
        friday_final_bedroom_dialogues,
        13
    ),
    "26": ("scene26", [], 13),
    "30": ("scene30", scene30_dialogues, 13),
    "tuesday_class": ("scene7", scene7_tuesday_dialogues, 5),
    # Extra test scenes
    "class2": ("scene7", scene7_second_dialogues, 2),
    "class4": ("scene9", scene9_fourth_dialogues, 4),
    "homework": ("homework_intro", homework_intro_dialogues, 2),

    "eat": ("scene7_eat", scene7_eat_dialogues, 1),
    "chat": ("scene7_chat", scene7_chat_dialogues, 1),
    "nap": ("scene7_sleep", scene7_sleep_dialogues, 1),
    "study": ("scene7_study", scene7_study_dialogues, 1),

    "bad_hunger": ("bad_hunger", bad_hunger_dialogues, 1),
    "bad_energy": ("bad_energy", bad_energy_dialogues, 1),
    "bad_mood": ("bad_mood", bad_mood_dialogues, 1),
    "bad_homework": ("bad_homework", bad_homework_dialogues, 2),
    "t2": (
    "scene7",
    scene7_tuesday_second_dialogues,
    6
),
}




# Function: debug_jump_to_scene — DEVELOPER MENU: Jump to a scene; earlier choices may not be initialized by a direct jump.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def debug_jump_to_scene(scene_key):
    """
    Teleport directly to a scene for testing.
    Reset temporary transitions and dialogue state.
    """
    global tuesday_evening_active
    global class7_post_console_phase
    global tuesday_choice_open
    global tuesday_breakfast_finished
    global current_scene, dialogues, dialogue_index
    global class_number, class_choice_open
    global homework_choice_open
    global settlement_active, choice_transition_active
    global class_reward_given, current_class_choice
    global afternoon_chat_triggered
    global pending_bad_ending
    global stats_enabled
    global hunger, energy, mood
    global display_hunger, display_energy, display_mood
    global debug_jump_open

    global scene22_choice_open, scene22_choice_made

    scene_key = str(scene_key).strip().lower()


    if scene_key not in DEBUG_SCENES:
        print("DEBUG: Unknown scene:", scene_key)
        return

    target, target_dialogues, target_class = DEBUG_SCENES[scene_key]

    # Set the Friday night route for debug jumps.
    if scene_key == "friday_home":
        friday_night_route = "home"

    elif scene_key in ("25", "friday_bedroom"):
        friday_night_route = "study"

    else:
        friday_night_route = None

    # Cancel ongoing transitions and selections.
    settlement_active = False

    # Reset Scene 22 when jumping directly into it.
    if target == "scene22":
        scene22_choice_open = False
        scene22_choice_made = None

    # Cancel ongoing transitions and selections.
    settlement_active = False
    choice_transition_active = False
    class_choice_open = False
    homework_choice_open = False
    class_reward_given = False
    current_class_choice = None
    afternoon_chat_triggered = False
    pending_bad_ending = None
    # Clear Tuesday breakfast choice states when teleporting.
    tuesday_choice_open = False
    tuesday_breakfast_finished = False
    # Prepare classroom progression.
    class_number = target_class
    class7_post_console_phase = None
    tuesday_evening_active = False

    

    # Reset stats to safe test values.
    hunger = 100
    energy = 100
    mood = 100

    display_hunger = hunger
    display_energy = energy
    display_mood = mood

    # Show the status HUD during gameplay.
    stats_enabled = target not in (
        "scene1", "scene2", "scene3",
        "scene4", "scene5", "scene6"
    )

    # Special initialization for classroom activities.
    if target in CLASS_BACKGROUNDS:
        current_class_choice = {
            "scene7_eat": "eat",
            "scene7_chat": "chat",
            "scene7_sleep": "sleep",
            "scene7_study": "study"
        }[target]

    # Load the target scene and dialogues.
    current_scene = target

    if target_dialogues is not None:
        dialogues = target_dialogues
    else:
        dialogues = scene1_dialogues

    dialogue_index = 0
    reset_typewriter()
    # Initialize the Tuesday breakfast event when teleporting.
    if target == "scene16":
        start_tuesday_breakfast()

    debug_jump_open = False

    print(
        "DEBUG TELEPORT:",
        current_scene,
        "| Class:", class_number
    )






# Function: advance_dialogue — CORE STORY ROUTER: Advance text and dispatch scene transitions after each dialogue group.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def advance_dialogue():

    """
    Complete partially typed dialogue or advance to the next entry.
    When the scene's lines are exhausted, dispatch the appropriate transition.
    """
    global trial_inventory_open
    
    global saturday_breakfast_active

    global friday_final_finished

    global friday_night_route
   
    global friday_final_finished
    
    global friday_study_penalty_applied
    
    global display_energy, display_mood

    global friday_breakfast_active

    global friday_breakfast_finished

    global friday_montage_penalty_applied
    
    global display_hunger, display_energy, display_mood
    
    global friday_breakfast_active, friday_breakfast_finished

    global quiz_night_active

    global pending_bad_ending

    global sun_quiz_phase
    
    global scene23_choice_open
   
    global new_thursday_breakfast_active
    
    global new_thursday_breakfast_finished
    
    global current_scene
    
    global tuesday_choice_open

    global tuesday_evening_active
    
    global display_hunger, display_energy, display_mood
    
    global class_number
    
    global dialogue_index, dialogues, current_scene

    global text_start, last_visible_count

    global scene_transition_start

    global stats_enabled

    global class_choice_open

    global homework_choice_open

    global pending_bad_ending

    global display_mood

    global tuesday_game_choice_open

    global console_event_stage
    
    global scene21_choice_open

    global thursday_dinner_route_active

    global thursday_dinner_settled
    global scene22_choice_open
    global scene22_energy_reward_given

    global scene22_choice_open
    global scene22_energy_reward_given
    global display_energy

    if dialogue_index >= len(dialogues):

        return



    name, expression, full_text = parse_dialogue_entry(dialogues[dialogue_index])



    # If the line is still typing, first reveal its remaining characters without advancing.

    if visible_character_count() < len(full_text):

        text_start = (

            pygame.time.get_ticks()

            - len(full_text) * CHAR_INTERVAL

        )

        last_visible_count = len(full_text)

        stop_voice()

        return



    # Once the full line is visible, the next input advances the dialogue index.

    dialogue_index += 1



    if dialogue_index < len(dialogues):

        reset_typewriter()

        return



    # Change scenes only after the current dialogue list has been fully consumed.

    if current_scene == "scene1":

        current_scene = "scene2"

        dialogues = scene2_dialogues

        dialogue_index = 0



    elif current_scene == "scene2":

        current_scene = "scene3"

        dialogues = scene3_dialogues

        dialogue_index = 0



    elif current_scene == "scene3":

        current_scene = "scene4"

        dialogues = scene4_dialogues

        dialogue_index = 0



    elif current_scene == "scene4":

        start_intertitle(

            "MONDAY",

            "scene5",

            scene5_dialogues
        )

        return



    elif current_scene == "scene5":

       current_scene = "scene6"

       dialogues = scene6_dialogues

       dialogue_index = 0





    elif current_scene == "scene6":


        # Saturday breakfast -> courtroom.
        if saturday_breakfast_active:
            start_saturday_court_transition()
            return

        # Friday's breakfast has ended.

        if friday_breakfast_active:
            friday_breakfast_finished = True
            friday_breakfast_active = False

            start_friday_school_transition()
            return


        # Thursday morning breakfast is finished.
        if new_thursday_breakfast_active:
            new_thursday_breakfast_finished = True
            new_thursday_breakfast_active = False

            # Enter Thursday's first lesson.
            class_number = 11
            current_scene = "scene7"

            dialogues = scene7_thursday_dialogues
            dialogue_index = 0

            class_choice_open = False
            begin_class()

            stop_voice()
            reset_typewriter()

            print("THURSDAY: Entering Class 11")
            return

        # Preserve Monday's original breakfast transition.
        current_scene = "scene6_to_7"
        scene_transition_start = pygame.time.get_ticks()

        dialogues = scene7_dialogues
        dialogue_index = 0

        stats_enabled = True
        return



    elif current_scene == "friday_school_intro":
        # Little F finishes talking excitedly.
        start_friday_montage()
        return

    elif current_scene == "friday_school_end":
        # Apply the complete school-day penalty only once.
        if not friday_montage_penalty_applied:
            change_stats(
                hunger_change=-10,
                energy_change=-10,
                mood_change=-10
            )

            display_hunger = hunger
            display_energy = energy
            display_mood = mood

            friday_montage_penalty_applied = True

            check_bad_ending()

            if pending_bad_ending is not None:
                start_bad_transition()
                return

        # Stop at the end of Friday's school day.
        # The evening storyline will be added later.

        # Wednesday's choice determines Friday night.
        if thursday_track_choice == "talk":
            start_friday_night_transition("scene25")

        elif thursday_track_choice == "ignore":
            start_friday_night_transition("scene13")

        else:
            print("FRIDAY ERROR: Scene 21 choice is missing")
            dialogue_index = len(dialogues)

        return



    elif current_scene == "scene25":
        # Jiang and Sun's Mom have finished welcoming Little F.
        start_friday_study_silence()
        return

    elif current_scene == "scene25_insult":
        # Sun's Mom has insulted Little F.
        # Apply the penalty only once.
        if not friday_study_penalty_applied:
            change_stats(
                energy_change=-20,
                mood_change=-20
            )

            display_energy = energy
            display_mood = mood
            friday_study_penalty_applied = True

            check_bad_ending()

            if pending_bad_ending is not None:
                start_bad_transition()
                return

        start_friday_night_transition("friday_bedroom")
        return


    elif current_scene == "friday_bedroom":
        friday_final_finished = True

        # Friday ends. Begin Saturday.
        start_saturday_transition()
        return


    # After Scene 7 introductory dialogue, reset class selection and show four choices.




    elif current_scene == "scene8":

        if class_number == 5:
            # Tuesday morning: Class 5 -> Class 6.
            start_tuesday_second_class_transition()
            return

        elif class_number == 6:
            # Tuesday afternoon: Class 6 -> Class 7.
            start_tuesday_class7_transition()
            return

        elif class_number < MAX_CLASSES:
            # Original Monday classroom loop.
            class_number += 1
            start_class_loop_transition()
            return

        elif class_number == 2:
            # Monday homework inspection.
            start_homework_event()
            return

        else:
            dialogue_index = len(dialogues)
            stop_voice()
            return



    
    elif current_scene == "scene15":
        # Tuesday morning: Continue to breakfast.
        start_tuesday_breakfast()

        print("TUESDAY: Scene 15 -> Scene 16")
        return



    elif current_scene == "scene16":

        if not tuesday_breakfast_finished:
            # Mom has finished speaking.
            # Show the three breakfast choices.
            tuesday_choice_open = True
            stop_voice()
            return

        else:
            # Dad has finished speaking.
            # Continue to Tuesday's first class.
            start_tuesday_school_transition()
            return


    

    elif current_scene == "scene7":

        if class_number == 8:
            # Teacher has finished the opening dialogue.
            # Little F speaks before falling asleep.
            dialogues = class8_sleep_dialogues
            dialogue_index = 0

            current_scene = "class8_sleep_dialogue"
            class_choice_open = False

            stop_voice()
            reset_typewriter()
            return

        # Preserve the normal classroom choice system.
        begin_class()
        class_choice_open = True
        stop_voice()
        return



    elif current_scene == "class8_sleep_dialogue":
        # Little F finishes complaining about being tired.
        start_class8_sleep_transition()
        return



    elif current_scene == "scene20":
        # Jiang has finished waking Little F.
        # Sleeping through the morning reduces Energy by 20.
        change_stats(energy_change=-20)

        # Immediately synchronize the visible Energy meter.
        display_energy = energy

        # Check whether the penalty triggers a bad ending.
        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

        # Continue to Thursday afternoon after the penalty.
        print("SCENE 20 COMPLETE: Energy -20")

        start_class9_transition()
        return


    elif current_scene == "scene21":
        # Little F has finished the running-track dialogue.
        # Open the two-choice menu.
        scene21_choice_open = True
        stop_voice()

        print("SCENE 21: Choice menu opened")
        return

    elif current_scene == "scene21_talk":
        enter_thursday_dinner_scene()
        return

    elif current_scene == "scene21_ignore":
        enter_thursday_dinner_scene()
        return

    elif current_scene == "scene20":
        start_class9_transition()
        return

    elif current_scene == "scene21":
        scene21_choice_open = True
        stop_voice()
        return


    elif current_scene == "scene22":
        # Ouyang has finished introducing the vape.
        scene22_choice_open = True
        stop_voice()

        print("SCENE 22: Accept / Decline opened")
        return

    elif current_scene == "scene22_accept_result":
        # Little F has finished coughing.
        if not scene22_energy_reward_given:
            change_stats(energy_change=20)
            display_energy = energy
            scene22_energy_reward_given = True

        check_bad_ending()
        if pending_bad_ending is not None:
            start_bad_transition()
            return

        enter_thursday_next_class_after_scene22()
        return

    elif current_scene == "scene22_decline_result":
        # Little F has refused the vape.
        enter_thursday_next_class_after_scene22()
        return



    elif current_scene == "thursday_sun_event":
        advance_sun_quiz_event()
        return

    elif current_scene == "scene23_a":
        # Teacher finishes accusing Little F.
        # Trigger the existing homework bad ending.
        pending_bad_ending = "bad_homework"
        start_bad_transition()
        return


    elif current_scene in ("scene23_b", "scene23_c"):
        # Quiz result dialogue has finished.
        # Continue to Scene 24.
        start_scene24()
        return

    elif current_scene in ("scene24_honest", "scene24_cheat"):
        # Result dialogue has finished.
        start_scene24_night_transition()
        return


    elif current_scene == "scene9":

        # Class 7 has returned from the console incident.
        if (
            class_number == 7
            and class7_post_console_phase == "dismissal"
        ):
            # The teacher has finished dismissing the class.
            start_post_console_transition("scene18")
            return

        # Class 7 opening: Show the special game choice.
        elif class_number == 7:
            begin_class()
            class_choice_open = False
            tuesday_game_choice_open = True
            stop_voice()
            return

        # Preserve the original classroom system.
        else:
            begin_class()
            class_choice_open = True
            stop_voice()
            return

    elif current_scene == "scene18":
        # Finish the classroom cleaning event.
        # Apply a one-time Hunger and Energy penalty.
        change_stats(
            hunger_change=-10,
            energy_change=-10
        )

        # Update the visible status meters.
        display_hunger = hunger
        display_energy = energy
        display_mood = mood

        # Check for a bad ending after the penalty.
        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

        # Continue to Tuesday evening dinner.
        tuesday_evening_active = True

        current_scene = "scene13"
        dialogues = scene13_tuesday_dialogues
        dialogue_index = 0

        stop_voice()
        reset_typewriter()

        print("TUESDAY: Scene 18 -> Scene 13")
        return




    elif current_scene == "scene10":

        if class_number == 9:
            # Thursday: Ouyang has finished teasing Little F.
            # Begin the fade into Class 10.
            start_class10_transition()
            return

        elif class_number == 3:
            # Monday: Preserve the original Class 3 -> Class 4 loop.
            start_afternoon_transition(next_class=True)
            return

        else:
            # Do not restart an unrelated class.
            stop_voice()
            return





    # After a branch finishes, begin the shared stat-settlement animation.

    elif current_scene in CLASS_BACKGROUNDS:

        if not settlement_active:

            start_class_settlement()

            stop_voice()

        return





    elif current_scene in BAD_ENDING_DIALOGUES:

        # All bad ending dialogues are finished

        start_credits_transition()

        return




    elif current_scene == "homework_intro":
        # Open the three-option menu after the teacher's introduction.
        homework_choice_open = True
        stop_voice()
        return

    elif current_scene in ("homework_a", "homework_c"):
        # Both incorrect choices trigger Bad Ending 04.
        pending_bad_ending = "bad_homework"
        start_bad_transition()
        return

    elif current_scene == "homework_b":
        print("HOMEWORK B ENDING REACHED")
        
        # The teacher has finished scolding Little F.
        # Apply the mood penalty only once.
        change_stats(mood_change=-10)

        # Update the visible mood meter.
        display_mood = mood

        # Check whether mood has reached zero.
        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

        # Continue to Scene 9 through the afternoon fade.
        start_afternoon_transition()
        return

    elif current_scene == "homework_survived":
        # Compatibility with the previous event flow.
        start_afternoon_transition()
        return


    elif current_scene in ("scene11", "scene12"):
        # Both Monday afternoon routes continue to dinner.
        print("AFTERNOON ROUTE FINISHED:", current_scene)

        start_evening_transition()
        return



    elif current_scene == "scene13":


        if friday_night_route == "home":
            # Mom has finished grounding Little F.
            stop_voice()
            start_credits_transition()
            return

        # Thursday dinner after the running-track event.
        if thursday_dinner_route_active:

            if not thursday_dinner_settled:
                change_stats(hunger_change=-20)
                thursday_dinner_settled = True
                display_hunger = hunger

                check_bad_ending()

                if pending_bad_ending is not None:
                    start_bad_transition()
                    return

            # Thursday has its own bedroom dialogue.
            dialogues = scene14_thursday_dialogues

        elif tuesday_evening_active:
            # Preserve Tuesday night.
            dialogues = scene14_tuesday_dialogues

        else:
            # Preserve Monday night.
            dialogues = scene14_dialogues

        current_scene = "scene14"
        dialogue_index = 0

        stop_voice()
        reset_typewriter()
        return


        print("DINNER -> BEDROOM:", current_scene)
        return



        if quiz_night_active:
            dialogue_index = len(dialogues)
            stop_voice()
            print("THURSDAY QUIZ NIGHT COMPLETE")
            return



    elif current_scene == "scene14":

        # Thursday quiz night -> Friday.
        if quiz_night_active:
            start_friday_transition()
            return

        # Previous bedroom route -> Thursday morning.
        elif thursday_dinner_route_active:
            start_new_thursday_transition()
            return

        # Tuesday night -> phone chat.
        elif tuesday_evening_active:
            start_scene19_transition()
            return

        # Original Monday -> Tuesday.
        else:
            start_tuesday_transition()
            return


    elif current_scene == "scene14":

        # Later bedroom route after the running-track event.
        if thursday_dinner_route_active:
            start_new_thursday_transition()
            return

        # Tuesday night continues to the phone chat.
        elif tuesday_evening_active:
            start_scene19_transition()
            return

        # Original Monday ending.
        else:
            start_tuesday_transition()
            return



        # Original Monday-to-Tuesday transition.
        start_tuesday_transition()
        return


    elif current_scene == "scene19":
        # Apply the phone-chat mood penalty once.
        change_stats(mood_change=-10)

        # Synchronize the visible mood bar.
        display_mood = mood

        check_bad_ending()

        if pending_bad_ending is not None:
            start_bad_transition()
            return

        # Continue to Thursday after the phone chat.
        stop_voice()
        start_thursday_transition()
        return



    elif current_scene == "thursday_mom":
        # Mom finishes shouting.
        # Wait one second before entering the classroom.
        start_thursday_mom_hold()
        return





    elif current_scene == "scene17":
        # Tuesday's console incident.
        if console_event_stage == "accusation":
            console_event_stage = "choice"
            dialogue_index = len(dialogues)
            stop_voice()
            print("CONSOLE EVENT: Choices opened")
            return

        elif console_event_stage == "choice":
            # Wait for the ownership selection.
            return

        elif console_event_stage == "result":
            # Apply the selected ending.
            finish_console_incident()
            return

        elif console_event_stage == "finished":
            return




    elif current_scene == "scene25":
        # Jiang and Sun's Mom have finished welcoming Little F.
        start_friday_study_silence()
        return

    elif current_scene == "scene25_insult":
        # Sun's Mom has insulted Little F.
        # Apply the penalty only once.
        if not friday_study_penalty_applied:
            change_stats(
                energy_change=-20,
                mood_change=-20
            )

            display_energy = energy
            display_mood = mood
            friday_study_penalty_applied = True

            check_bad_ending()

            if pending_bad_ending is not None:
                start_bad_transition()
                return

        start_friday_night_transition("friday_bedroom")
        return

    elif current_scene == "friday_bedroom":
        # Final Friday dialogue.
        friday_final_finished = True
        dialogue_index = len(dialogues)
        stop_voice()

        print("FRIDAY STUDY GROUP ROUTE COMPLETE")
        return


  

    elif current_scene == "scene26":
        # Opening testimony has finished.
        resolve_trial_evidence()
        return

    elif current_scene == "trial_evidence":
        # Little F remembers his evidence.
        if thursday_test_paper_owned:
            current_scene = "trial_inventory"
            trial_inventory_open = True
            stop_voice()
        else:
            set_trial_dialogues(
                "trial_no_evidence",
                trial_no_evidence_dialogues
            )
        return

    elif current_scene == "trial_no_evidence":
        # No passing test paper: negative ending.
        start_trial_ending_transition("scene29")
        return

    elif current_scene == "trial_present":
        # Little F successfully presents his test paper.
        start_trial_ending_transition("scene30")
        return


    elif current_scene == "scene30":
        # The final joke is over.
        # Fade to black and start the credits.
        print("GAME COMPLETE: Entering final credits")
        start_credits_transition()
        return





    reset_typewriter()







# Function: update_dialogue_sound — CORE AUDIO: Match character speech sounds to the typewriter progress.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def update_dialogue_sound():

    """Play sound effects for characters newly revealed by the typewriter."""

    global last_visible_count

    # Scene 19 contains silent phone messages.
    if current_scene == "scene19":
        return



    if dialogue_index >= len(dialogues):

        return



    name, expression, full_text = parse_dialogue_entry(dialogues[dialogue_index])



    count = min(

        visible_character_count(),

        len(full_text)

    )



    if count > last_visible_count:



        # Normally only one new character becomes visible during each update.

        # On a slow frame, play only the newest character instead of a backlog of sounds.

        letter = full_text[count - 1]



        play_letter_sound(name, letter)



        last_visible_count = count



# Function: draw_dialogue — CORE RENDERER: Draw name, dialogue text and portraits in supported scenes.
# Maintenance: comments only; test dependent scenes before changing executable logic.
def draw_dialogue():



    """
    Render the current speaker portrait, dialogue frame, and typed text.
    The selected expression is determined by the active dialogue tuple.
    """
    if dialogue_index >= len(dialogues):

        return



    name, expression, full_text = parse_dialogue_entry(

        dialogues[dialogue_index]

    )



    # Show speaker portraits in scenes that support expressive character artwork.

    # Enable character portraits in classroom and ending scenes.


    if current_scene in (
        "scene5", "scene6", "scene7", "scene8",
        "scene9", "scene10", "scene11", "scene12",
        "scene13", "scene14", "scene15", "scene16",
        "scene17", "scene18", "scene20",

        "scene7_eat", "scene7_chat",
        "scene7_sleep", "scene7_study",

        "class8_sleep_dialogue",
        "thursday_mom",
        "thursday_sun_event",

        "scene21", "scene21_talk", "scene21_ignore",

        "scene22",
        "scene22_accept_result",
        "scene22_decline_result",

        "scene23_a", "scene23_b", "scene23_c",
        "scene24","scene24_honest","scene24_cheat",
        "friday_school_intro",
        "friday_school_end",
        "scene25","scene25_insult",
        "friday_bedroom","scene30",
        

        "bad_hunger", "bad_energy", "bad_mood",
        "bad_homework",

        *HOMEWORK_EVENT_SCENES,
    ):





        portrait = load_portrait(name, expression)



        if portrait is not None:



            portrait_rect = portrait.get_rect(

                bottomright=(

                    box_rect.right - 60,

                    box_rect.top + 130

                )

            )



            screen.blit(portrait, portrait_rect)



    # Draw the dialogue box in front of the character portrait.

    screen.blit(dialogue_box, box_rect)



    count = min(

        visible_character_count(),

        len(full_text)

    )



    name_image = name_font.render(

        name, True, (255, 255, 255)

    )



    screen.blit(

        name_image,

        (box_rect.x + 24, box_rect.y + 24)

    )



    lines = wrap_text(

        full_text,

        BOX_WIDTH - 64

    )



    for row, (line, indices) in enumerate(lines):



        shown = "".join(

            char for char, original_index

            in zip(line, indices)

            if original_index < count

        )



        text_image = font.render(

            shown, True, (255, 255, 255)

        )



        screen.blit(

            text_image,

            (

                box_rect.x + 32,

                box_rect.y + 88 + row * 38

            )

        )







    # Wrap the complete line first so typewriter updates do not shift word boundaries.

    lines = wrap_text(

        full_text,

        BOX_WIDTH - 64

    )



    for row, (line, indices) in enumerate(lines):



        shown = "".join(

            char for char, original_index

            in zip(line, indices)

            if original_index < count

        )



        text_image = font.render(

            shown, True, (255, 255, 255)

        )



        screen.blit(

            text_image,

            (

                box_rect.x + 32,

                box_rect.y + 88 + row * 38

            )

        )



    if count >= len(full_text):



        hint = hint_font.render(

            "点击或按空格继续",

            True,

            (235, 220, 190)

        )



        screen.blit(

            hint,

            (

                box_rect.right - hint.get_width() - 28,

                box_rect.bottom - 30

            )

        )







# ==============================

# Main game loop: process input, update timers/audio, draw the scene, then flip.

# ==============================



running = True



# MAIN LOOP: Poll input, advance animations, draw the active scene and overlay UI.
while running:



    for event in pygame.event.get():
        # Debug keyboard input.


        # =====================================
        # FINAL TRIAL - INVENTORY INPUT
        # =====================================


        # =====================================
        # TRIAL INVENTORY - MOUSE INPUT
        # =====================================

        if current_scene == "trial_inventory":

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                paper_rect = get_trial_paper_rect()

                print("INVENTORY CLICK:", event.pos)
                print("PAPER RECT:", paper_rect)

                if paper_rect.collidepoint(event.pos):
                    print("PAPER SELECTED!")
                    select_trial_paper()

                else:
                    print("CLICK OUTSIDE PAPER SLOT")

            continue

        if event.type == pygame.KEYDOWN:
            print(
                "KEY PRESSED:",
                pygame.key.name(event.key),
                "| KEY CODE:",
                event.key
            )


        if event.type == pygame.QUIT:

            running = False


        # Scene 22 mouse selection.
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and current_scene == "scene22"
            and scene22_choice_open
        ):
            accept_rect = choice_accept_ui.get_rect(
                center=(WIDTH // 2, 470)
            )

            decline_rect = choice_decline_ui.get_rect(
                center=(WIDTH // 2, 580)
            )

            if accept_rect.collidepoint(event.pos):
                select_scene22_choice("accept")

            elif decline_rect.collidepoint(event.pos):
                select_scene22_choice("decline")

            continue

        # Handle console ownership choices.
        if (
            current_scene == "scene17"
            and console_event_stage == "choice"
        ):
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                if console_a_rect.collidepoint(event.pos):
                    select_console_option("a")

                elif console_b_rect.collidepoint(event.pos):
                    select_console_option("b")

                continue

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_a):
                    select_console_option("a")

                elif event.key in (pygame.K_2, pygame.K_b):
                    select_console_option("b")

                continue


        # Tuesday breakfast choice selection.
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and current_scene == "scene16"
            and tuesday_choice_open
        ):
            if tuesday_a_rect.collidepoint(event.pos):
                select_tuesday_option("a")

            elif tuesday_b_rect.collidepoint(event.pos):
                select_tuesday_option("b")

            elif tuesday_c_rect.collidepoint(event.pos):
                select_tuesday_option("c")

            # Prevent the same click from advancing dialogue.
            continue



        # Handle the single Class 7 choice.
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and current_scene == "scene9"
            and tuesday_game_choice_open
        ):
            if tuesday_game_rect.collidepoint(event.pos):
                select_tuesday_game()
            continue

        if (
            event.type == pygame.KEYDOWN
            and current_scene == "scene9"
            and tuesday_game_choice_open
        ):
            if event.key in (pygame.K_1, pygame.K_b):
                select_tuesday_game()
            continue

        # =====================================
        # DEVELOPER SCENE JUMP HOTKEYS
        # =====================================

        if DEBUG_MODE and event.type == pygame.KEYDOWN:


            # F1 or F8: Toggle the developer scene menu.
            if event.key in (pygame.K_F1, pygame.K_F8):
                debug_jump_open = not debug_jump_open
                debug_scene_input = ""

                print(
                    "DEBUG MENU:",
                    "OPEN" if debug_jump_open else "CLOSED"
                )
                continue

            # F2: Jump directly to Tuesday morning.
            if event.key == pygame.K_F2:
                debug_jump_to_scene("17")
                continue

            if debug_jump_open:

                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    print("DEBUG JUMP REQUEST:", repr(debug_scene_input))
                    debug_jump_to_scene(debug_scene_input)
                    debug_scene_input = ""
                    continue

                elif event.key == pygame.K_BACKSPACE:
                    debug_scene_input = debug_scene_input[:-1]
                    continue

                elif event.key == pygame.K_ESCAPE:
                    debug_jump_open = False
                    continue


                else:
                    # Accept scene numbers and debug keywords.
                    char = event.unicode

                    if char and char.isascii() and (
                        char.isalnum() or char == "_"
                    ):
                        debug_scene_input += char.lower()
                        print("DEBUG INPUT:", repr(debug_scene_input))

                    continue

        # Block gameplay mouse clicks while the debug menu is open.
        if debug_jump_open and event.type == pygame.MOUSEBUTTONDOWN:
            continue


        # =====================================
        # HOMEWORK B - PRIORITY DIALOGUE INPUT
        # =====================================

   
        if current_scene == "homework_b" and not debug_jump_open:

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ) or (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                print(
                    "HOMEWORK B INPUT:",
                    "index =", dialogue_index,
                    "total =", len(dialogues),
                    "choice =", homework_choice_open,
                    "settlement =", settlement_active
                )

                advance_dialogue()
                print("SCENE AFTER INPUT:", current_scene)
                continue




        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                # =====================================
                # SCENE 22 - ACCEPT / DECLINE
                # =====================================


                # SCENE 23 - QUIZ CHOICES
                if current_scene == "scene23" and scene23_choice_open:

                    if quiz_a_rect.collidepoint(event.pos):
                        select_scene23_choice("a")

                    elif quiz_b_rect.collidepoint(event.pos):
                        select_scene23_choice("b")

                    elif (
                        thursday_vape_choice == "accept"
                        and quiz_c_rect.collidepoint(event.pos)
                    ):
                        select_scene23_choice("c")

                    continue
                

                # =====================================
                # ORIGINAL GAME INPUT
                # =====================================

                if settlement_active:
                    continue

                # Keep all your existing mouse
                # handlers below this point.




                # Handle the three homework inspection choices.
                if homework_choice_open:

                    if homework_a_rect.collidepoint(event.pos):
                        select_homework_option("a")

                    elif homework_b_rect.collidepoint(event.pos):
                        select_homework_option("b")

                    elif homework_c_rect.collidepoint(event.pos):
                        select_homework_option("c")

                    continue

                # If the choice menu is open, interpret a click as a classroom activity selection.

                if class_choice_open:



                    if choice_chat_rect.collidepoint(event.pos):

                        select_class_option("chat")



                    elif choice_eat_rect.collidepoint(event.pos):

                        select_class_option("eat")



                    elif choice_sleep_rect.collidepoint(event.pos):

                        select_class_option("sleep")



                    elif choice_study_rect.collidepoint(event.pos):

                        select_class_option("study")



                # On the main menu, only start the story when the start-button area is clicked.

                elif current_scene == "menu":



                    if button_rect.collidepoint(event.pos):

                        current_scene = "transition"

                        transition_start = pygame.time.get_ticks()

                        play_background_music()



                # For normal scenes and endings, clicking advances the typewriter dialogue.




                elif current_scene in (
                    "scene1", "scene2", "scene3",
                    "scene4", "scene5", "scene6",
                    "scene7", "scene8",
                    "scene7_eat", "scene7_chat",
                    "scene7_sleep", "scene7_study",
                    "bad_hunger", "bad_energy", "bad_mood",
                    *HOMEWORK_EVENT_SCENES,
                    "bad_homework","scene9","scene10","scene11","scene12",
                    "scene13","scene14","scene15","scene16","scene17",
                    "scene18","scene19","thursday_mom","class8_sleep_dialogue",
                    "scene21","scene22","scene22_accept_result","scene22_decline_result",
                    "scene21_talk","scene23","scene24_honest","scene24_cheat",
                    "scene21_ignore","scene20","thursday_sun_event","scene23_a","scene23_b",
                    "scene23_c","scene24_honest","scene24_cheat","friday_school_intro",
                    "friday_school_end","scene30",
                
                    "scene25","scene25_insult","friday_bedroom","saturday_transition",
                    "saturday_court_transition","scene26",
                    "scene26","trial_evidence","trial_no_evidence","trial_present",
                ):
                    advance_dialogue()

            if current_scene == "scene21" and scene21_choice_open:
                mouse_pos = event.pos

                if "talk" in scene21_choice_rects and scene21_choice_rects["talk"].collidepoint(mouse_pos):
                    select_scene21_choice("talk")
                    continue

                if "ignore" in scene21_choice_rects and scene21_choice_rects["ignore"].collidepoint(mouse_pos):
                    select_scene21_choice("ignore")
                    continue

            
 





        elif event.type == pygame.KEYDOWN:



            if class_choice_open:



                key_to_choice = {

                    pygame.K_1: "chat",

                    pygame.K_2: "eat",

                    pygame.K_3: "sleep",

                    pygame.K_4: "study",

                }



                if event.key in key_to_choice:

                    select_class_option(

                        key_to_choice[event.key]

                    )



            elif event.key == pygame.K_SPACE:



                if not getattr(event, "repeat", False):



                    if current_scene == "wake_qte":

                        press_qte_space()



                    elif current_scene in (

                        "scene1", "scene2", "scene3",

                        "scene4", "scene5", "scene6",

                        "scene7", "scene8",

                        "scene7_eat", "scene7_chat",

                        "scene7_sleep", "scene7_study",

                        "bad_hunger", "bad_energy", "bad_mood",
                        "scene9", "scene10", "scene11", "scene12", "scene13", "scene14",
                        "scene15", "scene16", "scene17",
                        "scene18","homework_intro","class8_sleep_dialogue",
                        "scene21","scene21_talk","scene21_ignore",
                        "scene24_honest","scene24_cheat",
                        "homework_a",
                        "homework_b",
                        "homework_c",
                        "homework_survived",
                        "bad_homework","scene19","thursday_mom",
                        "friday_school_intro","friday_school_end",
                        "scene25","scene25_insult","friday_bedroom",
                        "saturday_transition","saturday_court_transition","scene26",
                        "scene26","trial_evidence","trial_no_evidence","trial_present",
                        "trial_inventory","trial_ending_transition",
                        "scene29","scene30",
                    ):

                           advance_dialogue()
            
            if current_scene == "scene21" and scene21_choice_open:
                if event.key in (pygame.K_a, pygame.K_1):
                    select_scene21_choice("ignore")
                    continue

                elif event.key in (pygame.K_b, pygame.K_2):
                    select_scene21_choice("talk")
                    continue





    # Update the pending classroom-branch transition without blocking the frame loop.

    if choice_transition_active:

        update_choice_transition()





    # ==============================

    # Advance displayed stat values and decide the next scene after settlement.

    # ==============================



    if settlement_active:

        update_class_settlement()



    # ==============================

    # Synchronize character speech effects with newly revealed dialogue letters.

    # ==============================




    if (
        not settlement_active
        and current_scene in (
            "scene1", "scene2", "scene3", "scene4",
            "scene5", "scene6", "scene7", "scene8",
            "scene9", "scene10", "scene11", "scene12",
            "scene13", "scene14", "scene15", "scene16",
            "scene17", "scene18", "scene20",

            "scene7_eat", "scene7_chat",
            "scene7_sleep", "scene7_study",

            "class8_sleep_dialogue",
            "thursday_mom",
            "thursday_sun_event",

            "scene21", "scene21_talk", "scene21_ignore",

            "scene22",
            "scene22_accept_result",
            "scene22_decline_result",

            "scene23_a", "scene23_b", "scene23_c",
             "scene24_honest","scene24_cheat",
            "scene25","scene25_insult","friday_bedroom",
             "scene26",   "trial_evidence",
            "trial_no_evidence",
            "trial_present","scene30",

            "bad_hunger", "bad_energy", "bad_mood",
            "bad_homework",
            "friday_school_intro","friday_school_end",

            "saturday_transition","saturday_court_transition","scene26",

            *HOMEWORK_EVENT_SCENES,
        )
        and not (
            current_scene == "scene17"
            and console_event_stage == "waiting"
        )
    ):
        update_dialogue_sound()




    # ==============================

    # Draw the active scene based on the current scene identifier.

    # ==============================



    if current_scene == "menu":

        screen.blit(cover, (0, 0))

        screen.blit(start_button, button_rect)





    elif current_scene == "transition":



        elapsed = pygame.time.get_ticks() - transition_start



        if elapsed < FADE_OUT_TIME:



            screen.blit(cover, (0, 0))

            screen.blit(start_button, button_rect)



            alpha = int(255 * elapsed / FADE_OUT_TIME)

            black_overlay.set_alpha(alpha)

            screen.blit(black_overlay, (0, 0))



        elif elapsed < FADE_OUT_TIME + BLACK_TIME:



            screen.fill((0, 0, 0))



        elif elapsed < FADE_OUT_TIME + BLACK_TIME + FADE_IN_TIME:



            screen.blit(scene1, (0, 0))



            fade_elapsed = (

                elapsed - FADE_OUT_TIME - BLACK_TIME

            )



            alpha = int(

                255 * (1 - fade_elapsed / FADE_IN_TIME)

            )



            black_overlay.set_alpha(alpha)

            screen.blit(black_overlay, (0, 0))



        else:



            current_scene = "scene1"

            reset_typewriter()



            screen.blit(scene1, (0, 0))

            draw_dialogue()



    elif current_scene == "scene1":



        screen.blit(scene1, (0, 0))

        draw_dialogue()

    elif current_scene == "scene2":



        screen.blit(scene2, (0, 0))

        draw_dialogue()

    elif current_scene == "scene3":



        screen.blit(scene3, (0, 0))

        draw_dialogue()

    elif current_scene == "scene4":

        screen.blit(scene4, (0, 0))

        draw_dialogue()

    elif current_scene == "intertitle":

        draw_intertitle()

    elif current_scene == "wake_qte":

        draw_qte()

    elif current_scene == "scene5":

        screen.blit(scene5, (0, 0))

        draw_dialogue()

    elif current_scene == "scene6":

        screen.blit(scene6, (0, 0))

        draw_dialogue()



    elif current_scene == "scene6_to_7":



        elapsed = pygame.time.get_ticks() - scene_transition_start



        if elapsed < SCENE_FADE_OUT:

            screen.blit(scene6, (0, 0))



            alpha = int(255 * elapsed / SCENE_FADE_OUT)

            black_overlay.set_alpha(alpha)

            screen.blit(black_overlay, (0, 0))



        elif elapsed < SCENE_FADE_OUT + SCENE_FADE_IN:

            screen.blit(scene7, (0, 0))



            fade_elapsed = elapsed - SCENE_FADE_OUT

            alpha = int(255 * (1 - fade_elapsed / SCENE_FADE_IN))



            black_overlay.set_alpha(alpha)

            screen.blit(black_overlay, (0, 0))



        else:

            current_scene = "scene7"

            reset_typewriter()



            screen.blit(scene7, (0, 0))

            draw_dialogue()



    elif current_scene == "thursday_mom":
        # Black background, Mom's angry portrait and dialogue.
        screen.fill((0, 0, 0))
        draw_dialogue()

    elif current_scene == "thursday_mom_hold":
        # Keep the screen completely black for one second.
        draw_thursday_mom_hold()

        # Play Mom's Animalese without showing her portrait.
        update_dialogue_sound()
        draw_dialogue()





    elif current_scene == "scene7":

        screen.blit(scene7, (0, 0))



        if class_choice_open:

            draw_class_choices()

        else:

            draw_dialogue()


    elif current_scene == "class8_sleep_dialogue":
        # Reuse the morning classroom background.
        screen.blit(scene7, (0, 0))
        draw_dialogue()

    elif current_scene == "class8_sleep_transition":
        # Gradually darken the screen.
        draw_class8_sleep_transition()

    elif current_scene == "scene20":
        # Show Jiang waking Little F.
        screen.blit(scene20, (0, 0))
        draw_dialogue()


    elif current_scene == "scene21_transition":
        # Fade from Class 10 to Scene 21.
        draw_scene21_transition()

    elif current_scene in (
        "scene21",
        "scene21_talk",
        "scene21_ignore"
    ):
        # Reuse the running-track background.
        screen.blit(scene21, (0, 0))

        if (
            current_scene == "scene21"
            and scene21_choice_open
        ):
            draw_scene21_choices()
        else:
            draw_dialogue()



    elif current_scene == "saturday_transition":
        draw_saturday_transition()

    elif current_scene == "saturday_court_transition":
        draw_saturday_court_transition()



    elif current_scene in (
        "scene26",
        "trial_evidence",
        "trial_no_evidence",
        "trial_present",
    ):
        draw_trial_scene()

    elif current_scene == "trial_inventory":
        draw_trial_inventory()

    elif current_scene == "trial_ending_transition":
        draw_trial_ending_transition()

    elif current_scene == "scene29":
        draw_scene29_ending()


    elif current_scene == "scene30":
        screen.blit(scene30, (0, 0))
        draw_dialogue()


    elif current_scene == "friday_night_transition":
        draw_friday_night_transition()

    elif current_scene == "scene25":
        screen.blit(scene25, (0, 0))
        draw_dialogue()

    elif current_scene == "friday_study_silence":
        draw_friday_study_silence()

    elif current_scene == "scene25_insult":
        screen.blit(scene25, (0, 0))
        draw_dialogue()

    elif current_scene == "friday_bedroom":
        screen.blit(scene4, (0, 0))
        draw_dialogue()



    elif current_scene == "class9_transition":
        # Wait before the afternoon classroom begins.
        draw_class9_transition()


    elif current_scene in CLASS_BACKGROUNDS:

        screen.blit(CLASS_BACKGROUNDS[current_scene], (0, 0))

        draw_dialogue()



    elif current_scene == "scene8":

        screen.blit(scene8, (0, 0))

        draw_dialogue()




    elif current_scene == "scene9":
        # Render the classroom background.
        screen.blit(scene9, (0, 0))

        # Class 7 uses one special video-game choice.
        if tuesday_game_choice_open:
            draw_tuesday_game_choice()

        # Classes 3 and 4 use the original four-choice menu.
        elif class_choice_open:
            draw_class_choices()

        # Display normal character dialogue.
        else:
            draw_dialogue()


    elif current_scene == "scene10":
        # Render the post-afternoon-class scene.
        screen.blit(scene10, (0, 0))
        draw_dialogue()


    elif current_scene == "class10_transition":
        # Render the fade between Thursday's lessons.
        draw_class10_transition()



    elif current_scene == "scene11":
        # Render the special after-class scene with Jiang.
        screen.blit(scene11, (0, 0))
        draw_dialogue()

    elif current_scene == "scene12":
        # Render the normal after-class scene.
        screen.blit(scene12, (0, 0))
        draw_dialogue()



    elif current_scene == "scene14":
        # Monday night: Reuse the original bedroom background.
        screen.blit(scene4, (0, 0))
        draw_dialogue()


    elif current_scene == "scene17":
        # Always display the dedicated background.
        screen.blit(scene17, (0, 0))

        if console_event_stage == "waiting":
            # Keep the background visible without dialogue.
            elapsed = pygame.time.get_ticks() - scene17_enter_time

            if elapsed >= SCENE17_DIALOGUE_DELAY:
                console_event_stage = "accusation"
                reset_typewriter()
                print("SCENE 17: Teacher dialogue begins")

        elif console_event_stage == "choice":
            # Show the two ownership choices.
            draw_console_choices()

        else:
            # Show the teacher or branch dialogue normally.
            draw_dialogue()



    elif current_scene == "thursday_transition":
        # Display the Thursday title on a black screen.
        draw_thursday_transition()

    elif current_scene == "thursday_mom":
        # Mom speaks off-screen against a black background.
        screen.fill((0, 0, 0))

        # Play Mom's normal Animalese voice.
        update_dialogue_sound()

        # Draw the dialogue box without a character portrait.
        draw_dialogue()




    elif current_scene == "tuesday_transition":
        # Show the Tuesday title card.
        draw_tuesday_transition()


    elif current_scene == "new_thursday_transition":
        draw_new_thursday_transition()


    elif current_scene == "friday_transition":
        draw_friday_transition()




    elif current_scene == "scene15":
        # Reuse the original morning bedroom background.
        screen.blit(scene5, (0, 0))
        draw_dialogue()


    elif current_scene == "scene16":
        # Reuse the original breakfast background.
        screen.blit(scene6, (0, 0))

        if tuesday_choice_open:
            draw_tuesday_choices()
        else:
            draw_dialogue()

    elif current_scene == "tuesday_school_transition":
        # Render the transition into Tuesday's classroom.
        draw_tuesday_school_transition()


    elif current_scene == "tuesday_class_transition":
        # Render the transition from Class 5 to Class 6.
        draw_tuesday_second_class_transition()

    elif current_scene == "tuesday_class7_transition":
        draw_tuesday_class7_transition()

    elif current_scene == "afternoon_transition":
        # Render the transition from the homework event
        # to the afternoon classroom.
        draw_afternoon_transition()


    elif current_scene == "post_console_transition":
        # Update and render the console-event fade.
        draw_post_console_transition()

    elif current_scene == "scene18":
        # Show Little F cleaning the classroom.
        screen.blit(scene18, (0, 0))
        draw_dialogue()


    elif current_scene == "scene19_transition":
        # Keep the screen black before Scene 19.
        draw_scene19_transition()

    elif current_scene == "scene19":
        # Show the phone background and typed chat messages.
        screen.blit(scene19, (0, 0))
        draw_dialogue()

    elif current_scene == "scene22_transition":
         draw_scene22_transition()

    elif current_scene == "scene22":
         screen.blit(scene22, (0, 0))

         if scene22_choice_open:
            draw_scene22_choices()
         else:
              draw_dialogue()

    elif current_scene == "scene22_vape_anim":
        draw_scene22_vape_anim()

    elif current_scene == "scene22_accept_result":
         screen.blit(scene22, (0, 0))
         draw_dialogue()

    elif current_scene == "scene22_decline_result":
          screen.blit(scene22, (0, 0))
          draw_dialogue()



    elif current_scene == "class_loop_transition":
        draw_class_loop_transition()


    elif current_scene == "bad_transition":

        draw_bad_transition()





    elif current_scene == "credits_transition":

        draw_credits_transition()



    elif current_scene == "credits":

        screen.blit(credits_image, (0, 0))







    elif current_scene == "bad_hunger":

        screen.blit(bad_hunger, (0, 0))

        draw_dialogue()



    elif current_scene == "bad_energy":

        screen.blit(bad_energy, (0, 0))

        draw_dialogue()



    elif current_scene == "bad_mood":

        screen.blit(bad_mood, (0, 0))

        draw_dialogue()




    elif current_scene == "friday_school_transition":
        draw_friday_school_transition()

    elif current_scene == "friday_school_intro":
        screen.blit(scene7, (0, 0))
        draw_dialogue()

    elif current_scene == "friday_montage":
        draw_friday_montage()

    elif current_scene == "friday_school_end":
        screen.blit(scene10, (0, 0))
        draw_dialogue()


    elif current_scene in HOMEWORK_EVENT_SCENES:

        # Reuse the original classroom background.
        screen.blit(scene7, (0, 0))

        # Show the choice images only after
        # the introduction dialogue is finished.
        if current_scene == "homework_intro" and homework_choice_open:
            draw_homework_choices()
        else:
            draw_dialogue()

    elif current_scene == "bad_homework":
        screen.blit(scene7, (0, 0))
        draw_dialogue()


    elif current_scene == "route_transition":
        draw_route_transition()


    elif current_scene == "evening_transition":
        # Play the fade from Scene 11/12 to Scene 13.
        draw_evening_transition()

    elif current_scene == "scene13":
        # Render the evening dinner scene.
        screen.blit(scene13, (0, 0))
        draw_dialogue()



    elif current_scene == "thursday_sun_event":
        screen.blit(scene9, (0, 0))
        draw_dialogue()

    elif current_scene == "scene23":
        screen.blit(scene23, (0, 0))
        draw_scene23_choices()

    elif current_scene == "scene23_accusation_wait":
        draw_scene23_accusation_wait()

    elif current_scene in ("scene23_a", "scene23_b", "scene23_c"):
        screen.blit(scene23, (0, 0))
        draw_dialogue()


    elif current_scene == "scene24_paper_anim":
        draw_scene24_paper_anim()

    elif current_scene in (
        "scene24_honest",
        "scene24_cheat"
    ):
        screen.blit(scene24, (0, 0))
        draw_dialogue()

    elif current_scene == "scene24_night_transition":
        draw_scene24_night_transition()


    # ==============================

    # Draw status meters on gameplay scenes that are configured to show them.

    # ==============================



    # =====================================
    # PERSISTENT STATUS HUD
    # =====================================

    # Hide the status HUD during the prologue,
    # fade transitions, black screens, and credits.
    HUD_HIDDEN_SCENES = {
        "menu",
        "intertitle",
        "wake_qte",
        "scene_transition",
        "class_loop_transition",
        "afternoon_transition",
        "bad_transition",
        "credits_transition",
        "credits",
        "route_transition",
        "evening_transition",
        "tuesday_transition",
        "tuesday_school_transition",
        "tuesday_class_transition",
        "tuesday_class7_transition",
        "scene17","class8_sleep_transition","class9_transition",
        "scene18","thursday_transition","thursday_mom",
        "thursday_mom_hold","class10_transition","new_thursday_transition",
        "post_console_transition","scene19_transition","scene24_night_transition",
        "friday_transition","friday_night_transition","friday_study_silence",
        "saturday_transition","saturday_court_transition","scene26",
        
        # Final courtroom and ending scenes
        "trial_evidence",
        "trial_no_evidence",
        "trial_present",
        "trial_inventory",
        "trial_ending_transition",
        "scene29",
        "scene30",

    }

    # Display the HUD only after gameplay stats are enabled.
    if stats_enabled and current_scene not in HUD_HIDDEN_SCENES:
        draw_status_ui()





    # Present the composed frame and cap the game loop at 60 frames per second.



    pygame.display.flip()

    clock.tick(60)



pygame.quit()