import os



class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {}

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs,
ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ.
ɪ ᴡᴏʀᴋ ᴏɴ ʙᴏᴛʜ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ.</b>"""

    HELP_TXT = """<b>Hᴇʏ {}

Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""

    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ : {}</b>

<b>✯ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/Potter_00>POTTER 😈</a></b>

<b>✯ Uᴘᴅᴀᴛᴇs : <a href=https://t.me/potterhub>Potterhub ⚡</a></b>

<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ2.0.62 [Sᴛᴀʙʟᴇ]</b>"""

    SOURCE_TXT ="""
<b>Private source Made by @Pankajpandiyar.
</b>
"""
 
    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>Nᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>

~ Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
~ Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
~ Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ/ᴏғғ Aᴜᴛᴏ Dᴇʟᴇᴛᴇ & Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀs ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>

- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/potterhub)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>

<u><b>Nᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b></u>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<u><b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b></u>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ/ᴏғғ AᴜᴛᴏFɪʟᴛᴇʀ & Aᴜᴛᴏ Dᴇʟᴇᴛᴇ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ.
4. Usᴇ /set_template ᴛᴏ sᴇᴛ ʏᴘᴜʀ ᴄᴜsᴛᴏɴ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ"""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/connect</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    ADMIN_TXT = """
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /setskip - <code>Tᴏ sᴋɪᴘ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴡʜᴇɴ ɪɴᴅᴇxɪɴɢ ғɪʟᴇs.</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>"""

    STATUS_TXT = """<b>📂 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>
<b>👤 ᴜsᴇʀs:</b> <code>{}</code>
<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>
<b>📉 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

"""

    ADMIN_STATUS_TXT = """<b>⍟────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]────⍟</b>

<b>⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>

<b>☣️ ᴄᴘᴜ:</b> <code>{}%</code>

<b>☢️ ʀᴀᴍ:</b> <code>{}%</code>

<b>📊 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>

<b>👤 ᴜsᴇʀs:</b> <code>{}</code>

<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>

<b>♻️ ᴛᴏᴛᴀʟ:</b> <code>512 MB</code>

<b>🉐 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

<b>🆓 ғʀᴇᴇ:</b> <code>{}</code>

<b>⍟────[ @KD_Botz ]─────⍟</b>"""

    LOG_TEXT_G = """<b>#NewGroup
    
Gʀᴏᴜᴘ = {} (<code>{}</code>)

Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>

Aᴅᴅᴇᴅ Bʏ - {}</b>
"""
    LOG_TEXT_P = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""
    ALRT_TXT = """⚠️ 𝖧ᴇʏ !
    
𝖲ᴇᴀʀᴄʜ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
𝖣ᴏɴ'ᴛ 𝖢ʟɪᴄᴋ 𝖮ᴛʜᴇʀ𝗌 𝖱ᴇ𝗌ᴜʟᴛ𝗌 😬
"""

    OLD_ALRT_TXT = """⚠️ 𝖧ᴇʏ ! 
    
𝖸ᴏᴜ Aʀᴇ U𝗌ɪɴɢ Oɴᴇ Oғ Mʏ Oʟᴅ Mᴇ𝗌𝗌ᴀɢᴇ𝗌, 
    
Sᴇɴᴅ Tʜᴇ Rᴇǫᴜᴇ𝗌ᴛ Aɢᴀɪ
"""

    CUDNT_FND = """<b> मूवी का सही नाम लिखे \जैसे - Pushpa 2021 ✅ \n Pushpa Hindi Movie ❌ \n webSeries के लिए mirzapur S01 ✅\n Mirzapur season 1 ❌❌.

</b>
"""

    I_CUDNT = """
<b>Sᴏʀʀʏ

I Cᴏᴜʟᴅ Nᴏᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ
Pʟᴇᴀsᴇ Cʜᴇᴄᴋ Yᴏᴜʀ Sᴘᴇʟʟɪɴɢ 🤧</b>
"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...
"""

    MVE_NT_FND = """<b>Mᴏᴠɪᴇ Nᴏᴛ Fᴏᴜɴᴅ...

Rᴇᴀsᴏɴs
𝟷) O.T.T Oʀ DVD Nᴏᴛ Rᴇʟᴇᴀsᴇᴅ

𝟸) Tʏᴘᴇ Nᴀᴍᴇ Wɪᴛʜ Yᴇᴀʀ

𝟹) Mᴏᴠɪᴇ Is Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ Dᴀᴛᴀʙᴀsᴇ 
Rᴇᴘᴏʀᴛ Hᴇʀᴇ @potter_help_bot</b>
"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ...
"""
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : Potter 😈
• ᴜꜱᴇʀɴᴀᴍᴇ : @potter_00
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/potter_00'>Potter 😈</a></b>
"""

    KD_IMDB = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>
"""

    KD_MISC = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
"""

    KD_FILSTR = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Fɪʟᴇ Sᴛᴏʀᴇ Mᴏᴅᴜʟᴇ ⍟</b>

» ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ ғᴏʀ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /link <code>- ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.<code>
• /batch <code>- ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇᴅɪᴀ.<code>

<b>Exᴀᴍᴘʟᴇ:</b>
<code>/batch https://t.me/potterhub/1 
https://t.me/potterhub/9</code>
"""

    KD_CNL = """
<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟</b>

<b>🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ.</b>
"""

    FORCE_SUB = """
**⚠️ ᴘʟᴇᴀsᴇ ғᴏʟʟᴏᴡ ᴛʜɪs ʀᴜʟᴇs ⚠️

ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʀʏ ᴀɢᴀɪɴ.

ɪ'ʟʟ sᴇɴᴅ ʏᴏᴜ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴘʀɪᴠᴀᴛᴇʟʏ.**
"""
    
    BANP_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>⍟ #BannedUser ⍟</b>
"""
    UNBANP_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>⍟ #UnBannedUser ⍟</b>
"""
    BANG_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #BannedGroup ⍟</b>
"""
    UNBANG_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #UnBannedGroup ⍟</b>
"""

    REQINFO2 = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Black Adam 2022

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01 or Loki S01 E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    PAGEINFO = """
ᴘᴀɢᴇs ᴍᴇᴀɴs 10 ғɪʟᴇs ɪɴ ᴏɴᴇ ᴘᴀɢᴇ

ɪғ ʏᴏᴜ ɴᴏᴛ sᴇᴇ ʏᴏᴜʀ ғɪʟᴇs ᴏɴ ᴛʜɪs ᴘᴀɢᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ᴘᴀɢᴇ.

Powered by :- potterhub
"""

    SPLMD = """
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Black Adam or Black Adam 2022

sᴇʀɪᴇs ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01 or Loki S01 E01

🚯ᴅᴏɴ'ᴛ ᴜsᴇ ➠ ':(!,./)

Powered by :- Potterhub
"""
    
    REQUEST_TXT = """
<u><b>📫 Rᴇǫᴜᴇsᴛ Dᴇᴛᴀɪʟs :</b></u>

<b>🔖 Mᴇssᴀɢᴇ :</b><code>{}</code>

<b>🕵️ Rᴇǫᴜᴇsᴛᴇᴅ Bʏ :</b> <b>{} [ <code>{}</code> ] </b>
"""

    REQUEST2_TXT = """
<i><b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Hᴀs Bᴇᴇɴ Aᴅᴅᴇᴅ!
Pʟᴇᴀsᴇ Wᴀɪᴛ Fᴏʀ Sᴏᴍᴇ Tɪᴍᴇ.</b></i>
"""

    SGROUP_TXT = """
<b>Dᴇᴀʀ, {}

<code>{}</code> Rᴇsᴜʟᴛs Aʀᴇ Aʟʀᴇᴀᴅʏ Aᴠᴀɪʟᴀʙʟᴇ Fᴏʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ <code>{}</code> Iɴ <a href=https://t.me/{}>Oᴜʀ Bᴏᴛ</a>.</b>
"""

    DONE_UPLOAD = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Cᴏᴍᴘʟᴇᴛᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
"""

    REQ_REJECT = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Rᴇᴊᴇᴄᴛᴇᴅ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Sᴀᴍᴇ Rᴇǫᴜᴇsᴛ, Nᴏᴛ Iɴ Fᴏʀᴍᴀᴛ !!
"""

    REQ_NO = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Nᴏᴛ Rᴇʟᴇᴀsᴇᴅ Oʀ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ !!
"""

    DONE_ALREADY = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
""" 
    
    DONE_UPLOAD2 = """
<b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Sᴜᴄᴇssғᴜʟʟʏ Uᴘʟᴏᴀᴅᴇᴅ Sᴇᴀʀᴄʜ Aɢᴀɪɴ..🙃</b>
"""

    REQ_REJECT2 = """
<b>Rᴇǫᴜᴇsᴛ Rᴇᴊᴇᴄᴛᴇᴅ 🚫 !!

Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Mᴀʏʙᴇ Iɴ Tʜᴇ Rᴇǫᴜᴇsᴛ Lɪsᴛ Oʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Is Mᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ. Kɪɴᴅʟʏ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ Oʀ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    REQ_NO2 = """
<b>Sᴏʀʀʏ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ 😔,
Kɪɴᴅʟʏ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    DONE_ALREADY2 = """
<b>Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ ❗,
Kɪɴᴅʟʏ Cʜᴇᴄᴋ Tʜᴇ Bᴏᴛ Bᴇғᴏʀᴇ Rᴇǫᴜᴇsᴛɪɴɢ.</b>
"""

    CAP_DLT_TXT = """
<b>Tʜᴇ Rᴇꜱᴜʟᴛꜱ Fᴏʀ ☞ <code>{}</code></b>

<b>Rᴇǫᴜᴇsᴛᴇᴅ Bʏ ☞ {}</b>

<b>‣ Tʜɪs Mᴇssᴀɢᴇ Wɪʟʟ ʙᴇ Aᴜᴛᴏ-Dᴇʟᴇᴛᴇᴅ Aғᴛᴇʀ 𝟷𝟶 Mɪɴᴜᴛᴇs.</b>
"""

    CAP_TXT = """
<b>Tʜᴇ Rᴇꜱᴜʟᴛꜱ Fᴏʀ ☞ <code>{}</code></b>

<b>Rᴇǫᴜᴇsᴛᴇᴅ Bʏ ☞ {}</b>

<u><b>Hᴇʏ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tʜᴇ Fɪʟᴇs Yᴏᴜ Wᴀɴᴛ Aɴᴅ Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ.</b></u>
"""

    FILE_CHANNEL_TXT = """
<b>🏷️ Tɪᴛʟᴇ :- <code>{}</code>

⚙️ Sɪᴢᴇ :- {}

🕵️‍♂️ Rᴇǫᴜᴇsᴛᴇᴅ Bʏ :- {}

🔅 Pᴏᴡᴇʀᴇᴅ Bʏ :- {}

<a href='t.me/{}'>‣ Tʜɪs Mᴇssᴀɢᴇ Wɪʟʟ ʙᴇ Aᴜᴛᴏ-Dᴇʟᴇᴛᴇᴅ Aғᴛᴇʀ 𝟷𝟶 Mɪɴᴜᴛᴇs. Kɪɴᴅʟʏ Fᴏʀᴡᴀʀᴅ Yᴏᴜʀ Fɪʟᴇs Tᴏ Sᴀᴠᴇᴅ.</a></b>"""

    FILE_READY_TXT = """
<b>Hᴇʏ {}
 
📫 Yᴏᴜʀ Fɪʟᴇ Is Sᴇɴᴛ Tᴏ Cʜᴀɴɴᴇʟ, 
Cʜᴇᴄᴋ Dᴏᴡɴ Tᴏ Vɪᴇᴡ.

📂 Fɪʟᴇ Nᴀᴍᴇ :- <code>{}</code>

⚙️ Fɪʟᴇ Sɪᴢᴇ :- {}</b>
"""

MALIK2 = """#verification_1

<b>Hay.</b> {}. 

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ. ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴛʜᴇ ᴠᴇʀɪғʏ ʟɪɴᴋ🔗 ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ⌛️..\n\n<b>इस बॉट को इस्तेमाल करने के लिए आपको रोजाना 2 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे</b>"""

SECOND_VERIFICATION_TEXT = """#verification 2

<b>Hay. {}. 

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ ᴛᴀᴘ ᴏɴ ᴛʜᴇ  ᴠᴇʀɪғʏ ʟɪɴᴋ 🖇️ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛᴏɴɪɢʜᴛ 12:00ᴀᴍ\n\n<b>इस बॉट को इस्तेमाल करने के लिए आपको रोजाना 2 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे</b>"""

SECOND_VERIFICATION_TEXT = os.environ.get('SECOND_VERIFICATION_TEXT', SECOND_VERIFICATION_TEXT)


MALIK7 = """Hay. {}. 

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ ғɪʀꜱᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ, ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ᴛʜᴇ ᴜᴘᴄᴏᴍɪɴɢ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ...\n\nᴘʟᴇᴀꜱᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ"""



SECOND_VERIFY_COMPLETE_TEXT = """Hay. {}. 

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪғɪᴇᴅ ғᴏʀ ᴛᴏɴɪɢʜᴛ 12:00ᴀᴍ ... ᴇɴɪᴏʏ ʏᴏᴜʀ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ʏᴏᴜʀ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ🧑‍🎤 ...

ᴘʟᴇᴀꜱᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ"""








