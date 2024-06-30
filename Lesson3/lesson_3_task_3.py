from address import Address
from mailing import Mailing

to_address = Address('559966', 'St. Petersburg',
                     'Nevsky prospect', '125', '11')
from_address = Address('629002', 'Salekhard', 'Respubliki', '555', '999')

mailing = Mailing(to_address, from_address, '500', 'RU1623548')


print("Отправление", mailing.track, "из", mailing.from_address.index,
      mailing.from_address.city, mailing.from_address.street,
      mailing.from_address.house, "-", mailing.from_address.flat,
      "в", mailing.to_address.index, mailing.to_address.city,
      mailing.to_address.street, mailing.to_address.house,
      "-", mailing.to_address.flat, ". Стоимость", mailing.cost, "рублей")
