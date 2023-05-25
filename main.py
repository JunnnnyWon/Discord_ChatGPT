#백상진 봇
#2023.02.15
#지역변수 무시하기.

import openai
import argparse
import discord
import asyncio
from discord import Member
from discord.ext import commands
import os
import sys
YOUR_API_KEY = ""
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pyaudio
import wave
import sounddevice as sd
load_dotenv()

def chatGPT(prompt, API_KEY=YOUR_API_KEY):
    
    # set api key
    openai.api_key = API_KEY

    # Call the chat GPT API
    completion = openai.Completion.create(
			  engine = 'text-davinci-003'     # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
			, prompt = prompt
			, temperature = 0.5 
			, max_tokens = 4000
			, top_p = 1
			, frequency_penalty = 0
			, presence_penalty = 0)

    return completion['choices'][0]['text']

def main():
    prompt = message_content
    message.channel.send(chatGPT(prompt).strip())


token = ""
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("login")
    print(bot.user.name)
    print(bot.user.id)
    print("---------------------")

@bot.event
async def on_message(message):
    message_content = message.content
    if "!질문" in str(message.content):
        message_content.strip("!질문")
        prompt = message_content
        answer = (chatGPT(prompt))
        await message.reply(answer)
        print(answer,"\n")

        print("유저 : ", message.author,"\n채널 : ", message.channel,"\n원형 메세지 콘텐츠 : ",message.content)


channel_id = 1030892271572369499

@bot.event
async def on_message(message):
    message_content = message.content
    channel = bot.get_channel(channel_id)
    if "!백업" in str(message.content):
        await message.reply('기존 백업을 삭제하고 새로운 백업을 시작합니다.')
        with open('log.txt','w') as file:
            file.write('')
        file = open('log.txt',mode='w', encoding='utf-8')

        
        # 1시간전의 메세지 기록
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=1)

        async for message in channel.history(limit=None,oldest_first=True,before=end_time, after=start_time):
            message_content = message.content
            file.write(message_content)
            file.write('\n')

        filepath = 'C:/Users\jack0\OneDrive\바탕 화면\Vs\log.txt'
        directory = os.path.dirname(filepath)
        backup_complete = ('백업 완료 / 경로 : ',directory)
        await message.reply(backup_complete)         





bot.run(token)

