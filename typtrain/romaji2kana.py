def parse(romaji):
    romaji = romaji.replace(" ", "")
    parsed = ""
    for i in range(len(romaji)):
        parsed += romaji[i]
        if romaji[i] == "-":
            parsed += " "
        if romaji[i] in ["a", "i", "u", "e", "o"]:
            parsed += " "
            if i and romaji[i - 1] in ["a", "i", "u", "e", "o"]:
                parsed = parsed[:-1] + " " + parsed[-1]
        else:
            if not i:
                continue
            if romaji[i] != "n" and romaji[i - 1] == romaji[i]:
                parsed = parsed[:-2] + " ltu " + parsed[-1]
            if romaji[i] not in ["h", "n", "s", "t", "w", "y"]:
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i] == "h" and romaji[i - 1] not in ["c", "d", "s", "t", "u"]:
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i] == "n" and romaji[i - 1] != "n":
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i] == "s" and romaji[i - 1] != "t":
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i] == "t" and romaji[i - 1] not in ["l", "x"]:
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i] == "w" and romaji[i - 1] not in ["k", "s", "n"]:
                parsed = parsed[:-1] + " " + parsed[-1]
            if romaji[i - 1] == "n" and romaji[i] not in ["n", "y", "w"]:
                parsed = parsed[:-1] + " " + parsed[-1]
            ncnt = 0
            for j in range(i - 1, -1, -1):
                if romaji[j] != "n":
                    break
                ncnt += 1
            if ncnt:
                if ncnt == int(ncnt / 2) * 2:
                    parsed = parsed[:-1] + " " + parsed[-1]
    parsed = parsed.strip()
    return parsed.split()


def convert(romaji):
    parsed = parse(romaji)
    trans = {
        "a": "ア",
        "i": "イ",
        "u": "ウ",
        "e": "エ",
        "o": "オ",
        "ka": "カ",
        "ki": "キ",
        "ku": "ク",
        "ke": "ケ",
        "ko": "コ",
        "kya": "キャ",
        "kyi": "キィ",
        "kyu": "キュ",
        "kye": "キェ",
        "kyo": "キョ",
        "kwa": "クヮ",
        "kwi": "クィ",
        "kwu": "クゥ",
        "kwe": "クェ",
        "kwo": "クォ",
        "sa": "サ",
        "si": "シ",
        "su": "ス",
        "se": "セ",
        "so": "ソ",
        "sya": "シャ",
        "syi": "シ",
        "syu": "シュ",
        "sye": "シェ",
        "syo": "ショ",
        "sha": "シャ",
        "shi": "シ",
        "shu": "シュ",
        "she": "シェ",
        "sho": "ショ",
        "swa": "スヮ",
        "swi": "スィ",
        "swu": "スゥ",
        "swe": "スェ",
        "swo": "スォ",
        "ta": "タ",
        "ti": "チ",
        "tu": "ツ",
        "te": "テ",
        "to": "ト",
        "tya": "チャ",
        "tyi": "チィ",
        "tyu": "チュ",
        "tye": "チェ",
        "tyo": "チョ",
        "tha": "テャ",
        "thi": "ティ",
        "thu": "テュ",
        "the": "テェ",
        "tho": "テョ",
        "tsa": "ツァ",
        "tsi": "ツィ",
        "tsu": "ツ",
        "tse": "ツェ",
        "tso": "ツォ",
        "ca": "カ",
        "ci": "シ",
        "cu": "ク",
        "ce": "セ",
        "co": "コ",
        "cha": "チャ",
        "chi": "チ",
        "chu": "チュ",
        "che": "チェ",
        "cho": "チョ",
        "cya": "チャ",
        "cyi": "チィ",
        "cyu": "チュ",
        "cye": "チェ",
        "cyo": "チョ",
        "qa": "クァ",
        "qi": "クィ",
        "qu": "ク",
        "qe": "クェ",
        "qo": "クォ",
        "na": "ナ",
        "ni": "ニ",
        "nu": "ヌ",
        "ne": "ネ",
        "no": "ノ",
        "n": "ン",
        "nn": "ン",
        "nya": "ニャ",
        "nyi": "ニィ",
        "nyu": "ニュ",
        "nye": "ニェ",
        "nyo": "ニョ",
        "nwa": "ヌヮ",
        "nwi": "ヌィ",
        "nwu": "ヌゥ",
        "nwe": "ヌェ",
        "nwo": "ヌォ",
        "ha": "ハ",
        "hi": "ヒ",
        "hu": "フ",
        "he": "ヘ",
        "ho": "ホ",
        "hya": "ヒャ",
        "hyi": "ヒィ",
        "hyu": "ヒュ",
        "hye": "ヒェ",
        "hyo": "ヒョ",
        "fa": "ファ",
        "fi": "フィ",
        "fu": "フ",
        "fe": "フェ",
        "fo": "フォ",
        "fya": "フャ",
        "fyi": "フィ",
        "fyu": "フュ",
        "fye": "フェ",
        "fyo": "フョ",
        "ma": "マ",
        "mi": "ミ",
        "mu": "ム",
        "me": "メ",
        "mo": "モ",
        "mya": "ミャ",
        "myi": "ミィ",
        "myu": "ミュ",
        "mye": "ミェ",
        "myo": "ミョ",
        "ya": "ヤ",
        "yi": "イ",
        "yu": "ユ",
        "ye": "イェ",
        "yo": "ヨ",
        "ra": "ラ",
        "ri": "リ",
        "ru": "ル",
        "re": "レ",
        "ro": "ロ",
        "rya": "リャ",
        "ryi": "リィ",
        "ryu": "リュ",
        "rye": "リェ",
        "ryo": "リョ",
        "wa": "ワ",
        "wi": "ウィ",
        "wu": "ウ",
        "we": "ウェ",
        "wo": "ヲ",
        "ga": "ガ",
        "gi": "ギ",
        "gu": "グ",
        "ge": "ゲ",
        "go": "ゴ",
        "gya": "ギャ",
        "gyi": "ギィ",
        "gyu": "ギュ",
        "gye": "ギェ",
        "gyo": "ギョ",
        "za": "ザ",
        "zi": "ジ",
        "zu": "ズ",
        "ze": "ゼ",
        "zo": "ゾ",
        "zya": "ジャ",
        "zyi": "ジィ",
        "zyu": "ジュ",
        "zye": "ジェ",
        "zyo": "ジョ",
        "ja": "ジャ",
        "ji": "ジ",
        "ju": "ジュ",
        "je": "ジェ",
        "jo": "ジョ",
        "jya": "ジャ",
        "jyi": "ジィ",
        "jyu": "ジュ",
        "jye": "ジェ",
        "jyo": "ジョ",
        "da": "ダ",
        "di": "ヂ",
        "du": "ヅ",
        "de": "デ",
        "do": "ド",
        "dha": "デャ",
        "dhi": "ディ",
        "dhu": "デュ",
        "dhe": "デェ",
        "dho": "デョ",
        "dya": "ヂャ",
        "dyi": "ヂィ",
        "dyu": "ヂュ",
        "dye": "ヂェ",
        "dyo": "ヂョ",
        "ba": "バ",
        "bi": "ビ",
        "bu": "ブ",
        "be": "ベ",
        "bo": "ボ",
        "bya": "ビャ",
        "byi": "ビィ",
        "byu": "ビュ",
        "bye": "ビェ",
        "byo": "ビョ",
        "va": "ヴァ",
        "vi": "ヴィ",
        "vu": "ヴ",
        "ve": "ヴェ",
        "vo": "ヴォ",
        "vya": "ヴャ",
        "vyi": "ヴィ",
        "vyu": "ヴュ",
        "vye": "ヴェ",
        "vyo": "ヴョ",
        "pa": "パ",
        "pi": "ピ",
        "pu": "プ",
        "pe": "ペ",
        "po": "ポ",
        "pya": "ピャ",
        "pyi": "ピィ",
        "pyu": "ピュ",
        "pye": "ピェ",
        "pyo": "ピョ",
        "xa": "ァ",
        "xi": "ィ",
        "xu": "ゥ",
        "xe": "ェ",
        "xo": "ォ",
        "xya": "ャ",
        "xyi": "ィ",
        "xyu": "ュ",
        "xye": "ェ",
        "xyo": "ョ",
        "la": "ァ",
        "li": "ィ",
        "lu": "ゥ",
        "le": "ェ",
        "lo": "ォ",
        "lya": "ャ",
        "lyi": "ィ",
        "lyu": "ュ",
        "lye": "ェ",
        "lyo": "ョ",
        "ltu": "ッ",
        "xtu": "ッ",
        "ltsu": "ッ",
        "xtsu": "ッ",
        "-": "ー",
    }
    res = ""
    for c in parsed:
        kana = trans.get(c)
        if kana:
            res += kana
        else:
            res += c
    return res
