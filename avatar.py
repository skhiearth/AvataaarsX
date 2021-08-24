import py_avataaars as pa
from PIL import Image
from random import randrange
from artGenerator import main

# Options
list_skin_color = ['TANNED', 'YELLOW', 'PALE',' LIGHT', 'BROWN', 'DARK_BROWN', 'BLACK']
list_top_type = ['NO_HAIR','EYE_PATCH','HAT','HIJAB','TURBAN',
                'WINTER_HAT1','WINTER_HAT2','WINTER_HAT3',
                'WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB',
                'LONG_HAIR_BUN','LONG_HAIR_CURLY','LONG_HAIR_CURVY',
                'LONG_HAIR_DREADS','LONG_HAIR_FRIDA','LONG_HAIR_FRO',
                'LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
                'LONG_HAIR_SHAVED_SIDES','LONG_HAIR_MIA_WALLACE',
                'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2',
                'LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_01',
                'SHORT_HAIR_DREADS_02','SHORT_HAIR_FRIZZLE',
                'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY',
                'SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
                'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES',
                'SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
list_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN',
                'BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
list_hat_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02',
                'HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE',
                'PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']

list_facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
list_facial_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED']
list_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
list_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
list_accessories_type = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
list_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
list_clothe_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']

# List of created avatars
allIterations = []

def getRandomIndices(number):
# Get random indexes 
    index_skin_color = randrange(0, len(list_skin_color))
    index_top_type = randrange(0, len(list_top_type))
    index_hair_color = randrange(0, len(list_hair_color))
    index_hat_color = randrange(0, len(list_hat_color))
    index_facial_hair_type = randrange(0, len(list_facial_hair_type))
    index_facial_hair_color= randrange(0, len(list_facial_hair_color))
    index_mouth_type = randrange(0, len(list_mouth_type))
    index_eye_type = randrange(0, len(list_eye_type))
    index_eyebrow_type = randrange(0, len(list_eyebrow_type))
    index_accessories_type = randrange(0, len(list_accessories_type))
    index_clothe_type = randrange(0, len(list_clothe_type))
    index_clothe_color = randrange(0, len(list_clothe_color))
    index_clothe_graphic_type = randrange(0, len(list_clothe_graphic_type))

    current_iteration = [index_skin_color, index_top_type, index_hair_color, index_hat_color, index_facial_hair_type,
    index_facial_hair_color, index_mouth_type, index_eye_type, index_eyebrow_type, index_accessories_type, index_clothe_type,
    index_clothe_color, index_clothe_graphic_type]

    if(current_iteration in allIterations):
        getRandomIndices(number)
    else:
        avatar = pa.PyAvataaar(
            style=eval('pa.AvatarStyle.CIRCLE'),
            skin_color=eval('pa.SkinColor.%s' % list_skin_color[index_skin_color]),
            top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % list_top_type[index_top_type]),
            hair_color=eval('pa.HairColor.%s' % list_hair_color[index_hair_color]),
            hat_color=eval('pa.ClotheColor.%s' % list_hat_color[index_hat_color]),
            facial_hair_type=eval('pa.FacialHairType.%s' % list_facial_hair_type[index_facial_hair_type]),
            facial_hair_color=eval('pa.FacialHairColor.%s' % list_facial_hair_color[index_facial_hair_color]),
            mouth_type=eval('pa.MouthType.%s' % list_mouth_type[index_mouth_type]),
            eye_type=eval('pa.EyesType.%s' % list_eye_type[index_eye_type]),
            eyebrow_type=eval('pa.EyebrowType.%s' % list_eyebrow_type[index_eyebrow_type]),
            nose_type=pa.NoseType.DEFAULT,
            accessories_type=eval('pa.AccessoriesType.%s' % list_accessories_type[index_accessories_type]),
            clothe_type=eval('pa.ClotheType.%s' % list_clothe_type[index_clothe_type]),
            clothe_color=eval('pa.ClotheColor.%s' % list_clothe_color[index_clothe_color]),
            clothe_graphic_type=eval('pa.ClotheGraphicType.%s' % list_clothe_graphic_type[index_clothe_graphic_type])
        )

        avatar.render_png_file('Avatars/avatar{}.png'.format(number))
        main(number)

if __name__ == "__main__":
    for i in range(1, 10):
        getRandomIndices(i)
        i = i + 1