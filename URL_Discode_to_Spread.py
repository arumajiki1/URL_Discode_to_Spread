
import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# ***.json　は各自ダウンロードしたjsonファイル名に変更してください
credentials = ServiceAccountCredentials.from_json_keyfile_name('url-discode-to-spread-bedb4869acb2.json', scope)
gc = gspread.authorize(credentials)

# スプレッドシートのキーを入れてください
SPREAD_SHEET_KEY = "1elydjBIjmI1Rp-D7SXWnmF_mWhNHnIHEHtNa9XtAS7M"
worksheet = gc.open_by_key(SPREAD_SHEET_KEY).worksheet('皆のおすすめゲーム')

#DiscordのBotのTokenを入れてください。
DISCORD_TOKEN = "MTA1MzM0MjM3OTQ3NTc0NjkyNg.GTTrvE.hWmUhnH8vf2yJZnKyAvN1bYQZjY6Q6thHW9T-w"
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

client.run(DISCORD_TOKEN)