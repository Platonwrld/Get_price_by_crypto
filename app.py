# в дополнение этой программы для обеспечения функционала получения цены другой валютной пары и в последствии вывода информации я бы 
# реализовал следующую логику: сделал бы ввод данных о валютной паре через input(если нужно их получить от клиента), 
# затем функция будет принимает эту пару и далее делать запрос с этой паре в url-e, затем будет возвращать информацию о цене


import asyncio
import aiohttp



async def get_price():
    async with aiohttp.ClientSession() as session:
        
        async with session.get('https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT') as response:

            if response.status == 200:
                data = await response.json()
                return float(data["price"])
            else:
                raise Exception('Не удалось получить цену')


async def main():
    max_price = 0
    
    while True:
        price = await get_price()
        
        print(price, max_price)
        
        if price > max_price:
            max_price = price
        if price < max_price * 0.99:
            print(f'Цена упала на 1% по отношению к максимальной цене за последний час: {price}')
            
        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
