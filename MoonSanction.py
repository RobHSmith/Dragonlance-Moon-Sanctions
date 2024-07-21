#Libraries
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import numpy

#Global variables
global response

#Get the discord bot token and server it's connected to
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

#Generate bot, call syntax ("!"), and permissions
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

#Connect bot to server on code start
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=SERVER)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

########################   Works for 351 AC in the Dragonlance setting, based on the moon phase chart for Dragonlance   ########################

#CurrentSanction command
@bot.command(name='CurrentSanction', help='Gives the current Sanction of each moon of Krynn and its effects')
async def current_sanction(ctx,day:int,month):
    year = 351 #AC
    SolinariDay0 = 35
    NuitariDay0 = 28
    LunitariDay0 = 1

    SolPeriod = 36
    NuiPeriod = 28
    LunPeriod = 8
    
    #Conversion
    monthList = ['Newkolt','Deepkolt','Brookgreen','Yurthgreen','Fleurgreen','Holmswelt','Fierswelt','Paleswelt','Reapember','Gildember','Darkember','Frostkolt']
    monthBase = monthList.index(month)

    #-----MATH-----#
    #Precode
    align1 = ''
    align2 = ''
    align3 = ''
    
    #All
    daysPassed = (year-1)*336 + (monthBase)*28 + day

    #Solinari
    SolMod = daysPassed % SolPeriod
    SolDay = SolinariDay0 + SolMod
    
    if SolDay > 36:
        SolDay = SolDay - 36

    if SolDay <= 3 or SolDay >= 31:
        SolinariStatus = 'Low Sanction\n'
    elif SolDay >= 4 and SolDay <= 12:
        SolinariStatus = 'Waxing\n'
    elif SolDay >= 13 and SolDay <= 21:
        SolinariStatus = 'High Sanction\n'
    else:
        SolinariStatus = 'Waning\n'

    #Nuitari - just a shifted month calendar, so much easier
    if day <= 3 or day >= 25:
        NuitariStatus = 'Waxing\n'
    elif day >= 4 and day <= 10:
        NuitariStatus = 'High Sanction\n'
    elif day >= 11 and day <= 17:
        NuitariStatus = 'Waning\n'
    else:
        NuitariStatus = 'Low Sanction\n'
    
    #Lunitari
    LunMod = daysPassed % LunPeriod
    LunDay = LunitariDay0 + LunMod

    if LunDay > 8:
        LunDay = LunDay - 8

    if LunDay == 1 or LunDay == 2:
        LunitariStatus = 'Low Sanction\n'
    elif LunDay == 3 or LunDay == 4:
        LunitariStatus = 'Waxing\n'
    elif LunDay == 5 or LunDay == 6:
        LunitariStatus = 'High Sanction\n'
    else:
        LunitariStatus = 'Waning\n'

    #Check for moon alignments
    if SolinariStatus != NuitariStatus:
        check1 = False
    else:
        check1 = True
    
    if SolinariStatus != LunitariStatus:
        check2 = False
    else:
        check2 = True
    
    if NuitariStatus != LunitariStatus:
        check3 = False
    else:
        check3 = True

    if check1:
        #convert Solinari day into day of quarter
        SolDayQuarter = SolDay + 6
        while SolDayQuarter > 9:
            SolDayQuarter = SolDayQuarter - 9

        #convert Nuitari day into day of quarter
        NuiDayQuarter = day+4
        while NuiDayQuarter > 7:
            NuiDayQuarter = NuiDayQuarter - 7

        if NuiDayQuarter == 1:
            if SolDayQuarter == 1 or SolDayQuarter == 2:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        elif NuiDayQuarter == 2:
            if SolDayQuarter == 2 or SolDayQuarter == 3:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        elif NuiDayQuarter == 3:
            if SolDayQuarter == 3 or SolDayQuarter == 4:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        elif NuiDayQuarter == 4:
            if SolDayQuarter == 4 or SolDayQuarter == 5 or SolDayQuarter == 6:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        elif NuiDayQuarter == 5:
            if SolDayQuarter == 6 or SolDayQuarter == 7:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        elif NuiDayQuarter == 6:
            if SolDayQuarter == 7 or SolDayQuarter == 8:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''
        else:
            if SolDayQuarter == 8 or SolDayQuarter == 9:
                align1 = 'Nuitari/Solinari Alignment'
            else:
                align1 = ''

    
    if check2:
        #convert Solinari day into day of quarter
        SolDayQuarter = SolDay + 6
        while SolDayQuarter > 9:
            SolDayQuarter = SolDayQuarter - 9

        if LunDay % 2 != 0 and SolDayQuarter <= 5:
            align2 = 'Lunitari/Solinari Alignment'
        elif LunDay % 2 == 0 and NuiDayQuarter >= 5:
            align2 = 'Lunitari/Solinari Alignment'
        else:
            align2 = ''
            check2 = False
    
    if check3:
        #convert Nuitari day into day of quarter
        NuiDayQuarter = day+4
        while NuiDayQuarter > 7:
            NuiDayQuarter = NuiDayQuarter - 7
        
        if LunDay % 2 != 0 and NuiDayQuarter <= 4:
            align3 = 'Lunitari/Nuitari Alignment'
        elif LunDay % 2 == 0 and NuiDayQuarter >= 4:
            align3 = 'Lunitari/Nuitari Alignment'
        else:
            align3 = ''
            check3 = False

    #Output builder
    if not check1 and not check2 and not check3:
        alignment = ''
    elif align1 == 'Nuitari/Solinari Alignment' and align2 == 'Lunitari/Solindari Alignment' and align3 == 'Lunitari/Nuitari Alignment':
        alignment = 'THE NIGHT OF THE EYE IS UPON YOU'
    else:
        alignment = align1 + align2 + align3

    #Output
    response = 'Lunitari: ' + LunitariStatus + 'Nuitari: ' + NuitariStatus + 'Solinari: ' + SolinariStatus + '\n' + alignment
    await ctx.send(response)

#Command to show call options for bot
@bot.command(name='detail',help='Gives details of Waxing, Alignment: Solinari/Lunitari, etc.')
async def detail(ctx,*,phase):
    #Convert for case-irrespective matching
    phase = str.casefold(phase)

    if phase == str.casefold('Waxing'):
        saveThrow = 'Normal\n'
        addSpells = '1\n'
        effLevel = 'As Cast\n'
    elif phase == str.casefold('High Sanction') or phase == str.casefold('HighSanction'):
        saveThrow = '+1\n'
        addSpells = '2\n'
        effLevel = '+1\n'
    elif phase == str.casefold('Waning'):
        saveThrow = 'Normal\n'
        addSpells = '0\n'
        effLevel = 'As Cast\n'
    elif phase == str.casefold('Low Sanction') or phase == str.casefold('LowSanction'):
        saveThrow = '-1\n'
        addSpells = '0\n'
        effLevel = '-1\n'
    elif phase == str.casefold('Alignment: Solinari/Lunitari') or phase == str.casefold('Alignment:Solinari/Lunitari') or phase == str.casefold('Alignment: Lunitari/Solinari') or phase == str.casefold('Alignment:Lunitari/Solinari'):
        saveThrow = '+1\n'
        addSpells = '+1\n'
        effLevel = '+1\n'
    elif phase == str.casefold('Alignment: Solinari/Nuitari') or phase == str.casefold('Alignment: Solinari/Nuitari') or phase == str.casefold('Alignment: Nuitari/Solinari') or phase == str.casefold('Alignment:Nuitari/Solinari'):
        saveThrow = '+1\n'
        addSpells = '0\n'
        effLevel = 'As Cast\n'
    elif phase == str.casefold('Alignment: Lunitari/Nuitari') or phase == str.casefold('Alignment:Lunitari/Nuitari') or phase == str.casefold('Alignment: Nuitari/Lunitari') or phase == str.casefold('Alignment:Nuitari/Lunitari'):
        saveThrow = '+1\n'
        addSpells = '+1\n'
        effLevel = '+1\n'
    elif phase == str.casefold('Alignment: Night of the Eye') or phase == str.casefold('Alignment:Night of the Eye') or phase == str.casefold('Alignment:NightoftheEye'):
        saveThrow = '+2\n'
        addSpells = '+2\n'
        effLevel = '+1\n'
    else:
        await ctx.send('Not a phase')   
    
    details = 'Spell Save DC: ' + saveThrow + 'Additional Spells: ' + addSpells + 'Effective Spell Level: ' + effLevel
    await ctx.send(details)

#Error throws
@current_sanction.error
async def current_sanction_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Missing arguments')

@detail.error
async def detail_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Missing arguments')


#Run bot
bot.run(TOKEN)