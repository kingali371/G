# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏭️", callback_data="skip_cb"),
            InlineKeyboardButton(text="⏹", callback_data="end_cb"),
            InlineKeyboardButton(
            text="الاوامر", url="https://t.me/L_H_V/1288"
            InlineKeyboardButton(
            text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊", url="https://t.me/L_H_V"
            InlineKeyboardButton(
            text="ضيف‌ آ‌لبوت لم‌جم‌وع‌تك ✅",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ضيف̀ آ̀لبوت لم̀جم̀وع̀́تك ✅",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="𓂄𓆩 اٰلـٰ̲ـہاٰوٰاٰمـٰ̲ـہرٰ 𓆪‌‌‏𓂁", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="ѕụᴘᴘᴏʀᴛ ɢʀᴏụᴘ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊", url="https://t.me/L_H_V"
        ),
        InlineKeyboardButton(text="ʙᴏᴛ ᴏᴡɴᴇʀ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ضيف̀ آ̀لبوت لم̀جم̀وع̀́تك ✅",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="ѕụᴘᴘᴏʀᴛ ɢʀᴏụᴘ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="الاوامر", url="https://t.me/L_H_V/1288"
        ),
        InlineKeyboardButton(text="ʙᴏᴛ ᴏᴡɴᴇʀ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="𓂄𓆩 ٱوٱمۘر ٱلتشغيۧل 𓆪‌‌‏𓂁",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="آ̀وآ̀م̀ر̀ آ̀لم̀ط̀́ور̀", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="م̀آ̀لك آ̀لبوت", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="B𝗔𝗖𝗞", callback_data="fallen_home"),
        InlineKeyboardButton(text="C𝗟𝗘𝗔𝗥", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="ѕụᴘᴘᴏʀᴛ ɢʀᴏụᴘ", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="B𝗔𝗖𝗞", callback_data="fallen_help"),
        InlineKeyboardButton(text="C𝗟𝗘𝗔𝗥", callback_data="close"),
    ],
]
