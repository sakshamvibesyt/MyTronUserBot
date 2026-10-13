"""Group plugin"""

import asyncio

from pyrogram.raw import functions
from pyrogram.types import Message

from main import app
from main.core.enums import UserType


@app.on_cmd(
    commands=["bgroup", "bgp"],
    usage="Create a basic group.",
    disable_for=UserType.SUDO
)
async def basicgroup_handler(_, m: Message):
    """Create a basic group."""
    args = m.text.split(maxsplit=2)

    if len(args) < 2:
        return await app.send_edit(
            "Usage: `.bgroup mygroupname`",
            delme=4
        )

    grpname = args[1]
    users = args[2].split() if len(args) > 2 else ["@TheRealPhoenixBot"]

    try:
        await app.send_edit(f"Creating a new basic group: `{grpname}`")
        group = await app.create_group(title=grpname, users=users)
        chat = await app.get_chat(group.id)

        await app.send_edit(
            f"**Created a new basic group:** [{grpname}]({chat.invite_link})"
        )
    except Exception as e:
        await app.error(e)


@app.on_cmd(
    commands=["sgroup", "sgp"],
    usage="Create a super group.",
    disable_for=UserType.SUDO
)
async def supergroup_handler(_, m: Message):
    """Create a supergroup."""
    args = m.text.split(maxsplit=2)

    if len(args) < 2:
        return await app.send_edit(
            "Usage: `.sgroup mygroupname`",
            delme=4
        )

    grpname = args[1]
    about = args[2] if len(args) > 2 else ""

    try:
        await app.send_edit(f"Creating a new supergroup: `{grpname}`")
        group = await app.create_supergroup(
            title=grpname,
            description=about
        )
        chat = await app.get_chat(group.id)

        await app.send_edit(
            f"**Created a new supergroup:** [{grpname}]({chat.invite_link})"
        )
    except Exception as e:
        await app.error(e)


@app.on_cmd(
    commands=["unread", "un"],
    usage="Set a chat as unread, read it later.",
    disable_for=UserType.SUDO
)
async def unreadchat_handler(_, m: Message):
    """Mark a chat as unread."""
    try:
        await asyncio.gather(
            m.delete(),
            app.invoke(
                functions.messages.MarkDialogUnread(
                    peer=await app.resolve_peer(m.chat.id),
                    unread=True
                )
            ),
        )
    except Exception as e:
        await app.error(e)


@app.on_cmd(
    commands="channel",
    usage="Create a channel.",
    disable_for=UserType.SUDO
)
async def channel_handler(_, m: Message):
    """Create a channel."""
    args = m.text.split(maxsplit=2)

    if len(args) < 2:
        return await app.send_edit(
            "Usage: `.channel channel_name`",
            delme=4
        )

    chname = args[1]
    about = args[2] if len(args) > 2 else ""

    try:
        await app.send_edit(f"Creating your channel: `{chname}`")
        response = await app.create_channel(
            title=chname,
            description=about
        )

        if response:
            chat = await app.get_chat(response.id)
            await app.send_edit(
                f"**Created a new channel:** [{chname}]({chat.invite_link})",
                disable_web_page_preview=True
            )
        else:
            await app.send_edit("Couldn't create a channel.")
    except Exception as e:
        await app.error(e)
