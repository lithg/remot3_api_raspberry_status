import sys
import time
import telepot
from verifica import *
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

idMsgEu = 591460761
idMsgPai = 574125243
idMsgHeber = 597994050
idMsgJosimar = 450548015

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='GERAR RELATÓRIO MCC', callback_data='press')],
               ])

    bot.sendMessage(chat_id, 'Clique no botao abaixo para gerar o status dos MCC(s)', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Gerando...')
    try:
        if from_id == idMsgEu:
            bot.sendMessage(idMsgEu, 'Guilherme, segue status atualizado do MCC: ')

        if from_id == idMsgPai:
            bot.sendMessage(idMsgPai, 'Guilherme, segue status atualizado do MCC: ')

        if from_id == idMsgHeber:
            bot.sendMessage(idMsgHeber, 'Heber, segue status atualizado do MCC: ')

        if from_id == idMsgJosimar:
            bot.sendMessage(idMsgJosimar, 'Josimar, segue status atualizado do MCC: ')

        bot.sendPhoto(from_id, open('status.png', 'rb'))
    except Exception as ex:
        print(ex)



bot = telepot.Bot('700156789:AAEuyIhBAxxz4pi_RDFKcc8zwnhftgWSp68')
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
def TeleMsgOn():
    bot.sendMessage(idMsgEu, 'Guilherme, algum MCC ficou ONLINE novamente!')
    bot.sendPhoto(idMsgEu, open('status.png', 'rb'))

    bot.sendMessage(idMsgPai, 'Guilherme, algum MCC ficou ONLINE novamente!')
    bot.sendPhoto(idMsgPai, open('status.png', 'rb'))

    bot.sendMessage(idMsgHeber, 'Heber, algum MCC ficou ONLINE novamente!')
    bot.sendPhoto(idMsgHeber, open('status.png', 'rb'))

    bot.sendMessage(idMsgJosimar, 'Josimar, algum MCC ficou ONLINE novamente!')
    bot.sendPhoto(idMsgJosimar, open('status.png', 'rb'))

def TeleMsgOff():
    bot.sendMessage(idMsgEu, 'Guilherme, algum MCC ficou OFFLINE!\n Por favor, verificar o relatório!')
    bot.sendPhoto(idMsgEu, open('status.png', 'rb'))

    bot.sendMessage(idMsgPai, 'Guilherme, algum MCC ficou OFFLINE!\n Por favor, verificar o relatório!')
    bot.sendPhoto(idMsgPai, open('status.png', 'rb'))

    bot.sendMessage(idMsgHeber, 'Heber, algum MCC ficou OFFLINE!\n Por favor, verificar o relatório!')
    bot.sendPhoto(idMsgHeber, open('status.png', 'rb'))

    bot.sendMessage(idMsgJosimar, 'Josimar, algum MCC ficou OFFLINE!\n Por favor, verificar o relatório!')
    bot.sendPhoto(idMsgJosimar, open('status.png', 'rb'))



print('Listening ...')


while 1:
    time.sleep(10)