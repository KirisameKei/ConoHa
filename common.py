import json
import os

import discord

async def set_notice_ch(client1, message):
    """
    導入サーバすべてのお知らせチャンネルにお知らせを送信"""

    if not message.author.guild_permissions.administrator:
        await message.channel.send("このコマンドは管理者のみが使用できます")
        return

    with open("./datas/marisa_notice.json", mode="r", encoding="utf-8") as f:
        notice_ch_dict = json.load(f)

    if message.content == "/set_notice_ch":
        notice_ch_dict[f"{message.guild.id}"] = message.channel.id
        await message.channel.send("このチャンネルに全体通知を送信します")

    elif message.content.split()[1].lower() == "none":
        notice_ch_dict[f"{message.guild.id}"] = None
        await message.channel.send("全体通知受信を拒否しました")

    else:
        await message.channel.send("`/set_notice_ch`で実行チャンネルを通知チャンネルに、`/set_notice_ch None`で通知拒否")

    with open("./datas/marisa_notice.json", mode="w", encoding="utf-8") as f:
        notice_ch_json = json.dumps(notice_ch_dict, indent=4)
        f.write(notice_ch_json)
