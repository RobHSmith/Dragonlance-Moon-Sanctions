# Dragonlance-Moon-Sanctions
Code to generate a Discord server output detailing the current day's moon phases/alignments in the Dragonlance setting. The code must be running for the bot to interact with Discord. Changing the "year" variable should only change the shift in the calendar (e.g. determining if 3 Yurthgreen has Nuitari in High Sanction or is Waxing).

Built using directions from https://realpython.com/how-to-make-a-discord-bot-python/#converting-parameters-automatically to create a Discord bot. 

Commands:
!CurrentSanction **day month_name** - gives the current sanction of Lunitari, Nuitari, and Solinari
!detail **moon_phase** - gives the changes to Arcane spellcasting for that phase
        **Alignment: moon_1/moon_2** - gives the changes to Arcane spellcasting for that moon alignment
