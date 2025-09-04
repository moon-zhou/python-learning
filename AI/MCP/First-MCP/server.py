#!/usr/bin/env python3

from fastmcp import FastMCP

# 初始化 FastMCP 服务器
mcp = FastMCP("ASCII Art Generator")

@mcp.tool()
def generate_ascii_art(text: str) -> str:
    """
    根据输入文本生成简单的ASCII艺术字图案
    
    Args:
        text: 需要转换为ASCII艺术字的文本
        
    Returns:
        str: 生成的ASCII艺术字图案
    """
    # 简单的ASCII艺术字生成器
    art_dict = {
        'A': [
            "  A  ",
            " A A ",
            "AAAAA",
            "A   A",
            "A   A"
        ],
        'B': [
            "BBBB ",
            "B   B",
            "BBBB ",
            "B   B",
            "BBBB "
        ],
        'C': [
            " CCC ",
            "C   C",
            "C    ",
            "C   C",
            " CCC "
        ],
        'D': [
            "DDDD ",
            "D   D",
            "D   D",
            "D   D",
            "DDDD "
        ],
        'E': [
            "EEEEE",
            "E    ",
            "EEEE ",
            "E    ",
            "EEEEE"
        ],
        'F': [
            "FFFFF",
            "F    ",
            "FFFF ",
            "F    ",
            "F    "
        ],
        'G': [
            " GGG ",
            "G   G",
            "G    ",
            "G  GG",
            " GGG "
        ],
        'H': [
            "H   H",
            "H   H",
            "HHHHH",
            "H   H",
            "H   H"
        ],
        'I': [
            "IIIII",
            "  I  ",
            "  I  ",
            "  I  ",
            "IIIII"
        ],
        'J': [
            "JJJJJ",
            "   J ",
            "   J ",
            "J  J ",
            " JJ  "
        ],
        'K': [
            "K   K",
            "K  K ",
            "KKK  ",
            "K  K ",
            "K   K"
        ],
        'L': [
            "L    ",
            "L    ",
            "L    ",
            "L    ",
            "LLLLL"
        ],
        'M': [
            "M   M",
            "MM MM",
            "M M M",
            "M   M",
            "M   M"
        ],
        'N': [
            "N   N",
            "NN  N",
            "N N N",
            "N  NN",
            "N   N"
        ],
        'O': [
            " OOO ",
            "O   O",
            "O   O",
            "O   O",
            " OOO "
        ],
        'P': [
            "PPPP ",
            "P   P",
            "PPPP ",
            "P    ",
            "P    "
        ],
        'Q': [
            " QQQ ",
            "Q   Q",
            "Q   Q",
            "Q  QQ",
            " QQQQ"
        ],
        'R': [
            "RRRR ",
            "R   R",
            "RRRR ",
            "R  R ",
            "R   R"
        ],
        'S': [
            " SSS ",
            "S   S",
            " SSS ",
            "    S",
            "SSSS "
        ],
        'T': [
            "TTTTT",
            "  T  ",
            "  T  ",
            "  T  ",
            "  T  "
        ],
        'U': [
            "U   U",
            "U   U",
            "U   U",
            "U   U",
            " UUU "
        ],
        'V': [
            "V   V",
            "V   V",
            "V   V",
            " V V ",
            "  V  "
        ],
        'W': [
            "W   W",
            "W   W",
            "W M W",
            "WW WW",
            "W   W"
        ],
        'X': [
            "X   X",
            " X X ",
            "  X  ",
            " X X ",
            "X   X"
        ],
        'Y': [
            "Y   Y",
            " Y Y ",
            "  Y  ",
            "  Y  ",
            "  Y  "
        ],
        'Z': [
            "ZZZZZ",
            "   Z ",
            "  Z  ",
            " Z   ",
            "ZZZZZ"
        ],
        ' ': [
            "     ",
            "     ",
            "     ",
            "     ",
            "     "
        ]
    }
    
    # 转换为大写
    text = text.upper()
    
    # 生成ASCII艺术字
    result_lines = ["", "", "", "", ""]
    for char in text:
        if char in art_dict:
            char_art = art_dict[char]
            for i in range(5):
                result_lines[i] += char_art[i] + " "
        else:
            # 如果字符不存在，用问号替代
            for i in range(5):
                result_lines[i] += " ??? "
    
    return "\n".join(result_lines)

@mcp.tool()
def generate_simple_ascii_art(text: str) -> str:
    """
    生成简化的ASCII艺术字
    
    Args:
        text: 需要转换为ASCII艺术字的文本
        
    Returns:
        str: 生成的简化ASCII艺术字图案
    """
    # 简化版本的ASCII艺术字生成器
    patterns = {
        'A': [
            " /\\ ",
            "/__\\",
            "|  |",
            "|  |"
        ],
        'B': [
            "___ ",
            "|_  )",
            " / / ",
            "/___|"
        ],
        'C': [
            " ____",
            "|__  ",
            "   \\ ",
            "|___/"
        ],
        'D': [
            "____ ",
            "|  _ \\",
            "| | | |",
            "|_| |_|"
        ],
        'E': [
            " ____",
            "| ___|",
            "|___ \\",
            "|____/"
        ],
        'F': [
            " ____",
            "| ___|",
            "|___ \\",
            "    /_/"
        ],
        'G': [
            " ____",
            "|  _ \\",
            "| |_| |",
            "|____/"
        ],
        'H': [
            "|  |",
            "|  |",
            "|__|",
            "|  |"
        ],
        'I': [
            " _ ",
            "| |",
            "| |",
            "|_|"
        ],
        'J': [
            "   _ ",
            "  | |",
            "  | |",
            "\\_| |"
        ],
        'K': [
            "| |",
            "| |",
            "| |",
            "|_|"
        ],
        'L': [
            "|  ",
            "|  ",
            "|  ",
            "|__"
        ],
        'M': [
            "|\\/|",
            "|  |",
            "|  |",
            "|  |"
        ],
        'N': [
            "|\\ |",
            "| \\|",
            "|  |",
            "|  |"
        ],
        'O': [
            " ___ ",
            "/ _ \\",
            "\\___/"
        ],
        'P': [
            " ___ ",
            "| _ \\",
            "|___/",
            "|    "
        ],
        'Q': [
            " ___ ",
            "/ _ \\",
            "\\_,_|"
        ],
        'R': [
            " ___ ",
            "| _ \\",
            "| . |",
            "|_||_|"
        ],
        'S': [
            " ___",
            "/ __|",
            "\\__ \\",
            "|___/"
        ],
        'T': [
            "___",
            " | ",
            " | ",
            " |_|"
        ],
        'U': [
            " _ _ ",
            "| | |",
            "|___|"
        ],
        'V': [
            "__",
            "\\ \\",
            " > >",
            "/_/"
        ],
        'W': [
            "_ _ _",
            "\\ \\ \\",
            " > > >",
            "/_/_/"
        ],
        'X': [
            "\\ /",
            " X ",
            "/ \\"
        ],
        'Y': [
            "\\ /",
            " Y ",
            " | ",
            " |_|"
        ],
        'Z': [
            "___",
            " / /",
            "/_/ ",
            "|___|"
        ],
        ' ': [
            "   ",
            "   ",
            "   ",
            "   "
        ]
    }
    
    # 转换为大写
    text = text.upper()
    
    # 生成ASCII艺术字
    result_lines = ["", "", "", ""]
    for char in text:
        if char in patterns:
            char_art = patterns[char]
            for i in range(len(char_art)):
                result_lines[i] += char_art[i] + " "
        else:
            # 如果字符不存在，用问号替代
            for i in range(4):
                result_lines[i] += " ? "
    
    return "\n".join(result_lines)

if __name__ == "__main__":
    # 运行服务器
    mcp.run()