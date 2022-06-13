from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


but1 = KeyboardButton('Smart-contract')
but2 = KeyboardButton('Frequently Asked Questions')
but3 = KeyboardButton('Sources of the TON')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(but1).add(but2).add(but3)

"""" Main Keyboards part """

""" Keyboard for topics """
kb_smartc = ReplyKeyboardMarkup(

    keyboard=[

    [
        KeyboardButton(text='What is Smart-Contract?'),
        KeyboardButton(text='What languages used for smart-contract?')
    ],

    [
        KeyboardButton(text='How can deploy deploy smart-contract?'),
    ],

    [
        KeyboardButton(text='Back')
    ]

    ],
    resize_keyboard=True

)


""" Keyboard for questions """
kb_questions = ReplyKeyboardMarkup(

    keyboard=[

    [
        KeyboardButton(text='What is the Ton?'),
        KeyboardButton(text='How does TVM work?')
    ],

    [
        KeyboardButton(text='Basic tools for TON developers'),
    ],

    [
        KeyboardButton(text='Different TON and Everscale'),
        # KeyboardButton(text='Inline menu'),
    ],

    [
        KeyboardButton(text='Back')
    ]

    ],
    resize_keyboard=True

)

""" Keyboard for sources """
kb_origins = ReplyKeyboardMarkup(

    keyboard=[

    [
        KeyboardButton(text='TON News'),
        KeyboardButton(text='TON Chat')
    ],

    [
        KeyboardButton(text='Sources for developers'),
    ],

    [
        KeyboardButton(text='Back'),
    ],

    ],

    resize_keyboard=True

)


"""" InlineKeyboards part """

""" InlineKeybaord for TonNews """
ikb_tonnews = InlineKeyboardMarkup(
    
    row_width=3,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='Дайте TON', url='https://t.me/givemetonru'),
            InlineKeyboardButton(text='Новости TON', url='https://t.me/tonnews_ru'),
            InlineKeyboardButton(text='TON Crypto News', url='https://t.me/tonc_news'),
        ]
    ]
)

""" InlineKeybaord for TonNews """
ikb_tonchat = InlineKeyboardMarkup(
    
    row_width=3,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='TON Дев Чат', url='https://t.me/tondev'),
            InlineKeyboardButton(text='TON Smart-Contracts Chat', url='https://t.me/tonsc_chat'),    
        ]
    ]
)

""" InlineKeybaord for TonNews """
ikb_origins = InlineKeyboardMarkup(
    
    row_width=3,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='TON Whitepaper', url='https://github.com/tonlabs/TON-Solidity-Compiler/blob/master/API.md'),   
            InlineKeyboardButton(text='TVM Whitepaper', url='https://ton-blockchain.github.io/docs/tvm.pdf'),
            InlineKeyboardButton(text='TON GitHub', url='https://github.com/ton-blockchain') 
        ]
    ]
)

""" InlineKeyboards for ton tools """
ikb_tools = InlineKeyboardMarkup(
    
    row_width=3,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='tonos-cli(tonlabs)', url='https://github.com/tonlabs/tonos-cli'),   
            InlineKeyboardButton(text='tondev(tonlabs)', url='https://github.com/tonlabs/ton-dev-cli'),
            InlineKeyboardButton(text='toncli(destinar)', url='https://github.com/disintar/toncli') 
        ]
    ]
)

""" InlineKeyboards for Smart Contract"""
ikb_sclang = InlineKeyboardMarkup(
    
    row_width=3,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='FunC', url='https://ton.org/docs/#/func'),   
            InlineKeyboardButton(text='Fift', url='https://ton.org/docs/#/compile?id=fift'),
        ]
    ]
)

ikb_deploy = InlineKeyboardMarkup(
    
    row_width=1,

    inline_keyboard = [
        [
            InlineKeyboardButton(text='Deploy your first smart-contract on FunC', url='https://github.com/romanovichim/TonFunClessons_ru/blob/main/1lesson/firstlesson.md'),  
        ]
    ]
)