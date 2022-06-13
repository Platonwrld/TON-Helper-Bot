from create_bot import dp, bot
from aiogram import Dispatcher, types
from keyboards import kb_client, kb_questions, kb_origins, ikb_tonnews, ikb_tonchat, ikb_origins, ikb_tools, kb_smartc, ikb_sclang, ikb_deploy
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, InputFile


async def command_start(message : types.Message):

    try:
        await bot.send_photo(message.from_user.id, types.InputFile('media/greeting.png'), caption=f'Hello, {message.from_user.full_name}!\nTon helper ready to help you', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Type there: \nhttp://t.me/ton_helper_for_dev_bot')

async def get_topics(message : types.Message):
    await message.answer(text='Topics', reply_markup=kb_smartc)

async def get_menu(message: types.Message):
    await message.answer('Go', reply_markup=kb_questions)


""" For question in kb_questions"""
async def get_kb_quests(message: types.Message):
    await message.answer('What question you interested?', reply_markup=kb_questions)

async def replies_1(message : types.Message): 
            await message.reply('The The Open Network (TON) is a fast, secure and scalable blockchain and network project, capable of handling millions of transactions per second ifnecessary, and both user-friendly and service provider-friendly.')

async def replies_2(message : types.Message): 
            await message.reply('The primary purpose of the Telegram Open Network Virtual Machine (TON VM or TVM) is to execute smart-contract code in the TON Blockchain.TVM must support all operations required to parse incoming messages andpersistent data, and to create new messages and modify persistent data.')

async def replies_3(message : types.Message): 
            await message.reply('Basic tools', reply_markup=ikb_tools)

async def replies_4(message : types.Message): 
            await message.reply('Everscale (EVER) and The Open Network (TON) blockchains are indeed very similar, as the Durov brothers idea and workings are behind both. The rebranding of Everscale shows that the company wants to develop independently from the history of TON and the Gram token. The Open Network, on the other hand, continues to use the original domain and wants to implement all the ideas of the Durov brothers. ')

async def reply_back(message : types.Message): 
            await message.reply('Back', reply_markup=kb_client)

""" For sources kb """
async def get_kb_origins(message: types.Message):
    await message.answer('What question you interested?', reply_markup=kb_origins)

async def replies_5(message : types.Message): 
    await message.reply('TON News', reply_markup=ikb_tonnews)

async def replies_6(message : types.Message): 
    await message.reply('Chats for devs', reply_markup=ikb_tonchat)

async def replies_7(message : types.Message): 
    await message.reply('Sources', reply_markup=ikb_origins)

async def replies_8(message : types.Message): 
    await message.reply('Back', reply_markup=kb_client)

""" Handlers for smart-contracts quastions """
async def replies_9(message : types.Message):
    await message.reply('A smart contract is a self-executing contract with the terms of the agreement between buyer and seller being directly written into lines of code. The code and the agreements contained therein exist across a distributed, decentralized blockchain network.')

async def replies_10(message : types.Message):
    await message.reply('FunC, which will be compiled into the Fift assembler and run in the TON Virtual Machine (TVM). How TVM and the Fift language work is well described in the official documentation. The basic language in which smartcontracts are written is FunC. Lets say you write a smartcontract in FunC, after that you compile the code in Fift-assembler. The compiled smart contract remains to be published. To do this, you need to write a code in Fift, which will take as input the smart contract code and some other parameters, and the output will be a file with the extension .boc (which means bag of cells), and, depending on how we write it, a private key and an address, which is generated from the smart contract code.', reply_markup=ikb_sclang)
async def replies_11(message : types.Message): 
    await message.reply('Deploy your first smart-contract', reply_markup=ikb_deploy)


def register_handlers_client(dp : Dispatcher):

    # Handler for /start
    dp.register_message_handler(command_start, commands=['start'])
    # Replies on question from kb_menu
    dp.register_message_handler(get_topics, text='Smart-contract')
    dp.register_message_handler(get_menu, Command('start'))
    dp.register_message_handler(get_kb_quests, text='Frequently Asked Questions')
    dp.register_message_handler(replies_1, text='What is the Ton?')
    dp.register_message_handler(replies_2, text='How does TVM work?')
    dp.register_message_handler(replies_3, text='Basic tools for TON developers')
    dp.register_message_handler(replies_4, text='Different TON and Everscale')
    dp.register_message_handler(reply_back, text='Back')
    # Replies for sources
    dp.register_message_handler(get_kb_origins, text='Sources of the TON')
    dp.register_message_handler(replies_5, text='TON News')
    dp.register_message_handler(replies_6, text='TON Chat')
    dp.register_message_handler(replies_7, text='Sources for developers')
    dp.register_message_handler(replies_8, text='Back')
    """ Basic answers for questions about smart-contract """
    dp.register_message_handler(replies_9, text='What is Smart-Contract?')
    dp.register_message_handler(replies_10, text='What languages used for smart-contract?')
    dp.register_message_handler(replies_11, text='How can deploy deploy smart-contract?')

