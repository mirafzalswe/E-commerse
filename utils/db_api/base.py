# from typing import Union
#
# import asyncpg
# from asyncpg import Connection
# from asyncpg.pool import Pool
#
# from data import config
#
#
# class Base:
#     def __init__(self):
#         self.pool:Union[Pool, None] = None
#
#
#     async def cretae(self):
#         self.pool = await asyncpg.create_pool(
#             user = config.USER,
#             password = config.PASSWORD,
#             host = config.HOST,
#             database = config.NAME
#         )
#
#     async def execute(self, command, *args,
#                       fetch: bool = False,
#                       fetchval: bool = False,
#                       fetchrow: bool = False,
#                       execute: bool = False):
#         async with self.pool.acquire() as connection:
#             connection: Connection
#             async with connection.transaction():
#                 if fetch:
#                     result = await connection.fetch(command, *args)
#                 elif fetchval:
#                     result = await connection.fetchval(command, *args)
#                 elif fetchrow:
#                     result = await connection.fetchrow(command, *args)
#                 elif execute:
#                     result = await connection.execute(command, *args)
#             return result
#
#     @staticmethod
#     def add_customers(self, full_name, address, phone):
#         sql = f'''INSERT INTO customers (full_name, address, phone)
#         VALUES ($1 ,$2, 3$) returning *'''
#         return await self.execute(sql,full_name, address, phone, fetchrow=True)