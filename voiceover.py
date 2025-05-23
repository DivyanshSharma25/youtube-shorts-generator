class voiceover():
    def make_audio(self,text,filename):
        import asyncio
        import edge_tts
        from pydub import AudioSegment

        voices = [ 'en-US-ChristopherNeural','en-US-GuyNeural']
        voice = voices[1]
        output_file = filename.split('.')[0]+'.mp3'

        async def amain():
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(output_file)

     #   loop = asyncio.get_event_loop_policy().get_event_loop()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(amain())
        finally:
            loop.close()
            

        audio = AudioSegment.from_mp3(output_file)
        audio.export(filename, format="wav")