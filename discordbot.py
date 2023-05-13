# インストールした discord.py を読み込む
import discord
from discord.ext import commands
from discord import app_commands
import asyncio

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)
TOKEN = '自分のトークン'
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)
#test
# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

#メッセージ削除
@bot.command()
async def purge(ctx,target:int):
    chan = ctx.message.channel
    #メッセージを入力した数＋入力したコマンドを削除
    deleted = await chan.purge(limit=target+1)
    msg = await ctx.send(f"{len(deleted)-1}件メッセージを削除しました")
    #2秒後にn件メッセージを削除しましたも消す
    await asyncio.sleep(2)
    await msg.delete()
    

bot.run(TOKEN)

