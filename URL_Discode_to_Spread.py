import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# ***.json　は各自ダウンロードしたjsonファイル名に変更してください
credentials = ServiceAccountCredentials.from_json_keyfile_name('url-discode-to-spread-bedb4869acb2.json', scope)
gc = gspread.authorize(credentials)

# スプレッドシートのキーを入れてください
worksheet = gc.open_by_key(process.env.SPREAD_SHEET_KEY).worksheet('皆のおすすめゲーム')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):  # メッセージを受け取ったときの挙動

    if message.author.bot:  # Botのメッセージは除く
        return

    values_list = []
    row = 0

    #　Discordに送られたメッセージ内容を3つ目のシートのセルに入力
    values_list = worksheet.col_values(4) #D列の値全取得
    row = len(values_list) + 1 #D列の行数+1、空白行のはず
    worksheet.update_cell(row, 4, message.content) #セル(row, 4)に入力

client.run(process.env.TOKEN)
