import asyncio

async def on_ready():
  inputget.start()

async def ainput(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)
@tasks.loop(seconds=1)
async def inputget():
  if await ainput("Type \"Off\" to turn off bot: ").lower()=="off":
print("Bot offed")
await bot.logout() 
