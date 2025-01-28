from prisma import Prisma

db = Prisma(auto_register=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(db.connect())
    