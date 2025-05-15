from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///teste.db')
print('Engine criado com sucesso!')
