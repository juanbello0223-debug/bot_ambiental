import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot de contaminación conectado")


@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que te informa sobre la contaminación ambiental.")
    await ctx.send("Usa !contaminacion para aprender sobre el tema.")


@bot.command()
async def contaminacion(ctx):
    mensaje = """
    🌎 CONTAMINACIÓN AMBIENTAL

    La contaminación ocurre cuando sustancias dañinas
    afectan nuestro medio ambiente.

    🌫️ Aire: humo de carros y fábricas.
    💧 Agua: basura y químicos en los ríos.
    🗑️ Suelo: residuos y plásticos.

    🌱 ¿Cómo podemos ayudar?
    - Reciclar.
    - Ahorrar agua.
    - Usar menos plástico.
    - No arrojar basura.
    """
    await ctx.send(mensaje)


@bot.command()
async def consejo(ctx):
    await ctx.send("🌱 Consejo: utiliza una botella reutilizable para reducir el plástico.")


@bot.command()
async def consejo2(ctx):
    await ctx.send("Consejo: si tienes dudas acerca de la clasificación de una basura... ¡preguntale a tu bot de confianza!")



@bot.command()
async def basura(ctx, color):
    if color == "blanca":
        with open('proyecto_bot_ambiental/white trashcan.jpg', 'rb') as f:
            picture = discord.File(f)
    elif color == "verde":
        with open('proyecto_bot_ambiental/green trashcan.jpg', 'rb') as f:
            picture = discord.File(f)
    elif color == "negra":
        with open('proyecto_bot_ambiental/black trash can.jpg', 'rb') as f:
            picture = discord.File(f)



    
       
    await ctx.send(file=picture)


@bot.command()
async def ecoreceta(ctx,):
    cocinero = """

Recuerda, hasta las zobras de comida tienen un objetivo en este planeta!!!

pequeña receta de hoy: chips de papa
 
Ingredientes:

Cáscaras de papas limpias y secas (puedes mezclar también con cáscaras de zanahoria).

1 cucharadita de aceite de oliva o vegetal.

Sal, pimienta o especias al gusto (pimentón en polvo, orégano, etc.).

Preparación (en 5 minutos):

Seca muy bien las cáscaras con una servilleta de papel (esto es clave para que queden crocantes).

Colócalas en un bol, añádele el aceite y tus especias favoritas, y mézclalas bien con las manos.

Llévalas al microondas en un plato apto durante 3 a 4 minutos (revisando a mitad de tiempo), o si prefieres al horno/freidora de aire a 200°C por unos 6-8 minutos hasta que doren y queden crujientes.


y se abren los telones
.... 
chips de papa a la orden para el netflix!!!!






"""
    await ctx.send(cocinero)

@bot.command()
async def chiste(ctx):
    await ctx.send("¿Sabes cuál es el colmo de una planta?, que la dejen plan-tada")




bot.run("TOKEN AQUI")
